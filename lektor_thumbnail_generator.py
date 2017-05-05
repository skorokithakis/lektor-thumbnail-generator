# -*- coding: utf-8 -*-
import shutil

from lektor.build_programs import AttachmentBuildProgram, buildprogram
from lektor.context import get_ctx
from lektor.db import Image
from lektor.imagetools import computed_height, get_image_info, process_image
from lektor.pluginsystem import Plugin
from werkzeug.utils import cached_property


@buildprogram(Image)
class ResizedImageBuildProgram(AttachmentBuildProgram):
    def build_artifact(self, artifact):
        ctx = get_ctx()
        plugin = ctx.env.plugins['thumbnail-generator']
        config = plugin.config

        artifact.ensure_dir()
        AttachmentBuildProgram.build_artifact(self, artifact)

        if not config:
            return

        source_img = artifact.source_obj.attachment_filename

        with open(source_img, 'rb') as f:
            _, w, h = get_image_info(f)

        # For every section in the config, we need to generate one image.
        for item, conf in config.items():
            width = int(conf["max_width"])
            height = int(conf.get("max_height", "0"))

            if not height:
                height = computed_height(source_img, width, w, h)

            df = artifact.source_obj.url_path
            ext_pos = df.rfind(".")
            dst_filename = "%s-%s.%s" % (df[:ext_pos], item, df[ext_pos + 1:])

            def closure(dst_filename, source_img, width, height, resize_image=True):
                # We need this closure, otherwise variables get updated and this
                # doesn't work at all.
                @ctx.sub_artifact(artifact_name=dst_filename, sources=[source_img])
                def build_thumbnail_artifact(artifact):
                    artifact.ensure_dir()
                    if not resize_image:
                        shutil.copy2(source_img, artifact.dst_filename)
                    else:
                        process_image(ctx, source_img, artifact.dst_filename, width, height)

            # If the image is larger than the max_width, resize it, otherwise
            # just copy it.
            resize_image = w > width or h > height
            closure(dst_filename, source_img, width, height, resize_image)


class ThumbnailGeneratorPlugin(Plugin):
    name = u'thumbnail-generator'
    description = u'Add your description here.'
    image_exts = ['png', 'jpg', 'jpeg', 'gif']

    @cached_property
    def config(self):
        conf = self.get_config()
        return {section: conf.section_as_dict(section) for section in conf.sections()}
