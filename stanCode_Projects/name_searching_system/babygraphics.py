"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE+interval*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # vertical line associated to certain years
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    # inside area for plotting names and ranks
    plot_area = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2
    # for the actual y_coordinate of rank
    interval = plot_area/1000
    # storing the first coordinate for the line drawing
    temp_x = 0
    temp_y = 0
    # for color changing
    j = 0
    for name in lookup_names:
        # dict: {years, ranks}
        baby_info = name_data[name]
        # if all four colors have been used: reset
        if j > 3:
            j = 0
        # color for each name
        color = COLORS[j]

        # loop all years and check whether each year is in baby_info or not
        for i in range(len(YEARS)):
            year = YEARS[i]
            year = str(year)
            if year not in baby_info:
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
                y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                # case: draw line--> start from i == 1
                if i > 0:
                    canvas.create_line(temp_x, temp_y, x_coordinate, y_coordinate, fill=color, width=LINE_WIDTH)
                    temp_x = x_coordinate
                    temp_y = y_coordinate
                    canvas.create_text(temp_x+TEXT_DX, temp_y, text=f'{name} *', anchor=tkinter.SW, fill=color)
                # case: first coordinate(x, y)
                else:
                    temp_x = x_coordinate
                    temp_y = y_coordinate
                    canvas.create_text(temp_x+TEXT_DX, temp_y, text=f'{name} *', anchor=tkinter.SW, fill=color)
            else:
                x_coordinate1 = get_x_coordinate(CANVAS_WIDTH, i)
                y_coordinate1 = int(baby_info[year])*interval+GRAPH_MARGIN_SIZE
                # case: draw line--> start from i == 1
                if i > 0:
                    canvas.create_line(temp_x, temp_y, x_coordinate1, y_coordinate1, fill=color, width=LINE_WIDTH)
                    temp_x = x_coordinate1
                    temp_y = y_coordinate1
                    canvas.create_text(temp_x+TEXT_DX, temp_y, text=f'{name} {baby_info[year]}', anchor=tkinter.SW, fill=color)
                # case: first coordinate(x, y)
                else:
                    temp_x = x_coordinate1
                    temp_y = y_coordinate1
                    canvas.create_text(temp_x+TEXT_DX, temp_y, text=f'{name} {baby_info[year]}', anchor=tkinter.SW, fill=color)
        j += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
