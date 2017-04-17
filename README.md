Lektor Thumbnail Generator
==========================

This plugin automatically generates thumbnails for any images in your Lektor
content. The difference between this plugin and the `thumbnail` filter is that
this is geared towards content, i.e. you don't need to have any references to
the images in your templates at all.


Usage
-----

Use this plugin if you want to be able to link to full-size images in your
content, but still want thumbnails to be generated for the link itself. For
example, you may have an image called `cat.jpg`, and to link to it in the
*content* (not the template), but also show a thumbnail.

You can do that like so:

~~~
<a href="cat.jpg"><img src="cat-small.jpg" /></a>
~~~


Installation
------------

To install the plugin, just add `lektor-thumbnail-generator` to your plugins
from the command line:

~~~
lektor plugins add lektor-thumbnail-generator
~~~

If you have trouble, see the [plugin
installation](https://www.getlektor.com/docs/plugins/) section of the Lektor
documentation.

Then, create a config file called `configs/thumbnail-generator.ini` and add
a few sections for images. The section names can be whatever you want, the
final images will be called `imagename-sectionname.ext`. For example, this
config file:

~~~
[small]
max_width = 30

[medium]
max_width = 400
max_height = 400

[woowee]
max_width = 2000
~~~

Will take a file called `cat.jpg` and create the files `cat-small.jpg`,
`cat-medium.jpg` and `cat-woowee.jpg`. All the files will be created, regardless
of whether the original file is smaller, so you can link without worrying
whether a file will exist or not. If the original file is smaller than the width
you have specified, the file will only be copied, and will not be resized.

Unfortunately, due to the way Lektor's thumbnail system works, files *will* be
scaled up if they're too small. The `max_width`/`max_height` parameters work
like for the [Lektor
thumbnail](https://www.getlektor.com/docs/api/db/record/thumbnail/) command.
