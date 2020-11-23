"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    color_dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]
    """
    # rgb of each pixel
    pixel_r = 0
    pixel_g = 0
    pixel_b = 0
    # how many pixels in the list[pixels]
    n = 0
    for pixel in pixels:
        n += 1
        pixel_r += pixel.red
        pixel_g += pixel.green
        pixel_b += pixel.blue
    pixel_avg = [pixel_r//n, pixel_g//n, pixel_b//n]
    return pixel_avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # get the mean rgb value of the list[pixels]
    pixel_avg = get_average(pixels)

    # position value for storing each pixel rgb value
    n = 0
    red = 0
    green = 0
    blue = 0
    # output the value to each variable: red, green, blue
    for pixel_val in pixel_avg:
        n += 1
        if n == 1:
            red += pixel_val
        elif n == 2:
            green += pixel_val
        elif n == 3:
            blue += pixel_val

    # for storing the shortest distance
    best_pixel_dist = 1000
    best_pixel = None
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, red, green, blue)
        if pixel_dist < best_pixel_dist:
            best_pixel_dist = pixel_dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # For storing pixels from images
    pixels = []
    x = 0
    y = 0
    img = None
    # Start finding the best pixel among pixels of the list[images]
    while True:
        for img in images:
            pixel = img.get_pixel(x, y)
            pixels += [pixel]
            # When all the pixels in the direct coordination has been collected, find the best one
            # and fill it on the result whiteboard
            if len(pixels) == len(images):
                result_pixel = result.get_pixel(x, y)
                best_pixel = get_best_pixel(pixels)
                result_pixel.red = best_pixel.red
                result_pixel.green = best_pixel.green
                result_pixel.blue = best_pixel.blue
                pixels = []
                # change to next column
                if x < img.width-1:
                    x += 1
                # change to next row
                else:
                    y += 1
                    x = 0
        # situation: last pixel, to prevent OBOB
        if x == img.width-1 and y == img.height-1:
            for img in images:
                pixel = img.get_pixel(x, y)
                pixels += [pixel]
                if len(pixels) == len(images):
                    result_pixel = result.get_pixel(x, y)
                    best_pixel = get_best_pixel(pixels)
                    result_pixel.red = best_pixel.red
                    result_pixel.green = best_pixel.green
                    result_pixel.blue = best_pixel.blue
                    pixels = []
            break
    print("Displaying image!")
    result.show()
    ######## YOUR CODE ENDS HERE ###########


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
