import os
import argparse
import subprocess

# Parse Arguments
parser = argparse.ArgumentParser(description='Resize images and compress them')

parser.add_argument("-s", dest="size", help="Define the new size of the picture, default 2048X2048",
                    default="2048X2048",
                    type=str)
parser.add_argument("-q", dest="quality", help="define the compressed quality, default 90", default="90",
                    type=str)
parser.add_argument("-overwrite", dest="overwrite", type=bool,
                    help="flag for overwriting source files, default true", default=True)
args = parser.parse_args()

print("Options: Size %s, Quality %s" % (args.size, args.quality))
# Which directory do you want to start with?
working_dir = os.getcwd()


def resize_images_overwrite(directory: str):
    print("Squaring images in: %s" % directory)

    # imagemagick command for squaring ALL images inside a directory but not it's subdirectories
    subprocess.run(
        [f"mogrify", "-shave", "5X5", "-gravity", "center", "-resize", f"{args.size}", "-extent", f"{args.size}",
         "-interlace", "Plane", "-quality", f"{args.quality}%", "-format", "jpg", "*.*"])



# Get all the subdirectories of working_dir recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(working_dir)]

# because imagemagick can't run recursively, we need to iterate over every subdirectory and run the script
for directory in directories:
    # Change working Directory
    os.chdir(directory)
    print("Changing directory: %s" % directory)
    # Run your function
    if (args.overwrite):
        resize_images_overwrite(directory)
