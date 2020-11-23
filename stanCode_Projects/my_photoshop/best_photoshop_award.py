"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


def main():
    """
    The concept of my masterpiece:
        Apply what I've learned in Assignment4: blur
        Inspired by 'The dress debate': Is the dress white and gold or black and blue
        Also inspired by the great 'Shakespeare': To be or not to be?
    """
    # file reading
    me = SimpleImage('image_contest/blur me.png')
    wb = SimpleImage('image_contest/大whiteboard.jpg')
    back = SimpleImage('image_contest/background.jpg')

    # make me as big as the white part where I'm gonna fit in
    me.make_as_big_as(wb)

    # combine me and the background
    combined_img = combine(me, back)
    combined_img.show()


def combine(me, back):
    # make sure when back.width found the right x(in the whiteboard area) me_x can start with 0
    me_x = -64
    me_y = 0
    # loop the background, when find the whiteboard area, start replacing back_pixel into me_pixel
    for x in range(back.width):
        for y in range(back.height):
            if 64 < x < 629 and 139 < y < 512:
                # whiteboard pixel
                back_pixel = back.get_pixel(x, y)
                # me pixel
                me_pixel = me.get_pixel(me_x, me_y)

                back_pixel.red = me_pixel.red
                back_pixel.green = me_pixel.green
                back_pixel.blue = me_pixel.blue

                me_y += 1
        me_x += 1
        me_y = 0
    return back



if __name__ == '__main__':
    main()
