## Image squared
Bulk transform your images to squares from your command line. Useful for ecommerce.

## How to use

This script uses imagemagick behind the scenes to actually square images.

1) Install imagemagick

```brew install imagemagick```

If you need to support tiff files run

``brew reinstall imagemagick --with-libtiff``

2) CD into the directory of images you want to transform

3) Run the script

``python path/to/script/ImageSquared.py``