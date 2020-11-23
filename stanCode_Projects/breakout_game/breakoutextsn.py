"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphicsextsn import BreakoutGraphics

# 120 frames per second.
FRAME_RATE = 1000 / 120
NUM_LIVES = 3
is_start = False


def main():
    graphics = BreakoutGraphics()

    # Animation loop!
    while True:
        pause(FRAME_RATE)
        # the switch for controlling the ball to move after clicking
        if graphics.start:
            graphics.ball.move(graphics.get_ball_x_velocity(), graphics.get_ball_y_velocity())
            graphics.check_hit_wall()
            graphics.touch_thing()
            graphics.check_what_object()

            if graphics.dead():
                pass
            elif graphics.win():
                break




if __name__ == '__main__':
    main()
