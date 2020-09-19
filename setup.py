from setuptools import setup

setup(
    name="lektor-thumbnail-generator",
    version="0.5.0",
    author=u"Stavros Korokithakis,,,",
    author_email="hi@stavros.io",
    url="https://github.com/skorokithakis/lektor-thumbnail-generator/",
    description="This plugin automatically generates thumbnails for any images in your Lektor content. The difference between this plugin and the `thumbnail` filter is that this is geared towards content, i.e. you don't need to have any references to the images in your templates at all.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=["lektor_thumbnail_generator"],
    entry_points={
        "lektor.plugins": [
            "thumbnail-generator = lektor_thumbnail_generator:ThumbnailGeneratorPlugin",
        ]
    },
)
