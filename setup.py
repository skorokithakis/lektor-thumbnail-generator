from setuptools import setup

setup(
    name='lektor-thumbnail-generator',
    version='0.3',
    author=u'Stavros Korokithakis,,,',
    author_email='hi@stavros.io',
    license='MIT',
    py_modules=['lektor_thumbnail_generator'],
    entry_points={
        'lektor.plugins': [
            'thumbnail-generator = lektor_thumbnail_generator:ThumbnailGeneratorPlugin',
        ]
    }
)
