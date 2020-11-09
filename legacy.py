def resize_images_safely(directory):
    # define location to save image
    save_to = target + os.path.basename(os.path.normpath(directory))
    print("Saving location: %s" % save_to)

    # create saving location
    try:
        os.mkdir(save_to)
    except OSError:
        print("Creation of the directory %s failed" % save_to)
    else:
        print("Successfully created the directory %s " % save_to)

    # define command for resizing
    command = "mogrify \
    -shave 5x5 \
    -background white \
    -gravity center   \
    -resize {} -extent {} \
    -interlace Plane \
    -gaussian-blur 0.05 \
    -quality {}% \
    -path {} \
    -format jpg *.jpg;".format(args.size, args.size, args.quality, '"' + save_to + '"')

    print("Resizing (overwrite) in: %s" % directory)
    # execeute command
    os.system(command)

    # imagemagick command for squaring ALL images inside a directory but not it's subdirectories
    subprocess.run(
        [f"mogrify", "-shave", "5X5", "-gravity", "center", "-resize", f"{args.size}", "-extent", f"{args.size}",
         "-interlace", "Plane", "-quality", f"{args.quality}%", "-format", "jpg", "*.*"])