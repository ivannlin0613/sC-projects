"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3       # Maximum chances for player to play


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # only three lives
        self.num_lives = NUM_LIVES
        # win img
        self.img = GImage('WIN!!.png')

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Start button
        self.button_back = GRect(250, 50)
        self.button_back.filled = True
        self.button_back.fill_color = 'darkgrey'
        self.window.add(self.button_back, x=(self.window.width - self.button_back.width) // 2, y=352.5)

        self.button = GRect(250, 50)
        self.button.filled = True
        self.button.fill_color = 'grey'
        self.window.add(self.button, x=(self.window.width-self.button.width)//2, y=350)

        self.button_word = GLabel('CLICK TO START')
        self.button_word.font = '-30'
        self.window.add(self.button_word, x=(self.window.width-self.button_word.width)//2,
                        y=350+self.button_word.height+10)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)//2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width//2-ball_radius, y=window_height//2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = self.set_ball_x_velocity()
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.control_paddle)

        # the switch of the game
        self.start = False

        # Score board.
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-22'
        self.window.add(self.score_label, x=0, y=self.score_label.height+5)

        # how many lives
        self.life1 = GLabel('❤️')
        self.life1.font = '-20'
        self.window.add(self.life1, self.window.width-self.life1.width, self.life1.height+7)

        self.life2 = GLabel('❤️')
        self.life2.font = '-20'
        self.window.add(self.life2, self.window.width-self.life2.width*2, self.life2.height+7.35)

        self.life3 = GLabel('❤️')
        self.life3.font = '-20'
        self.window.add(self.life3, self.window.width-self.life3.width*3, self.life3.height+7.35)

        # Draw bricks.
        x = 0
        # to change row
        space = 0
        self.change = 0
        self.color = 'red'
        # 5 colors
        for i in range(brick_rows//2):
            # each color 2 rows
            for j in range(2):
                # x bricks
                for k in range(brick_cols):
                    self.brick = GRect(brick_width, brick_height, x=0+x, y=brick_offset+space)
                    x += (brick_width+brick_spacing)
                    self.brick.filled = True
                    self.brick.fill_color = self.color
                    self.brick.color = self.color
                    self.window.add(self.brick)
                x = 0
                space += (brick_height + brick_spacing)
            self.change_color()

    def change_color(self):
        """
        a method for making different color of the bricks
        :return: color
        """
        self.change += 1
        if self.change == 1:
            self.color = 'orange'
        elif self.change == 2:
            self.color = 'yellow'
        elif self.change == 3:
            self.color = 'green'
        elif self.change == 4:
            self.color = 'blue'

    def control_paddle(self, m):
        """
        This method controls the paddle by moving your mouse inside the window.
        The midpoint of the paddle follows the mouse
        :param m: mouse event
        """
        if self.paddle.width//2 <= m.x <= self.window.width-self.paddle.width//2:
            self.paddle.x = m.x-self.paddle.width//2

    def start(self, m):
        """
        The switch of this game
        """
        self.window.remove(self.button)
        self.window.remove(self.button_back)
        self.window.remove(self.button_word)
        if self.num_lives > 0:
            self.start = True

    def set_ball_x_velocity(self):
        """
        This method gives random dx for the ball whenever the ball starts moving.
        """
        # ball start w/ different dx speed
        self.__dx = random.randint(1, MAX_X_SPEED)
        # ball start w/ different direction
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    # getter: ball dx
    def get_ball_x_velocity(self):
        return self.__dx

    # getter: ball dy
    def get_ball_y_velocity(self):
        return self.__dy

    def touch_thing(self):
        """
        This method checks whether the ball has touched something.
        No, keep moving
        Yes, return the thing to next place to check what is the thing
        """
        # object sensor: left up, right up, left down, right down
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
        obj4 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

        # check whether ball touch object
        if obj1 is None:
            if obj2 is None:
                if obj3 is None:
                    if obj4 is None:
                        pass
                    else:
                        return obj4
                else:
                    return obj3
            else:
                return obj2
        else:
            return obj1

    def check_hit_wall(self):
        """
        This method checks whether the ball hits the top, left or right wall and changes
        its direction dx = -dx
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width-self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def check_what_object(self):
        """
        This method checks what object did the ball hit
        """
        if self.touch_thing() is self.paddle:
            # avoid the situation: when the ball touches the edge of paddle, it will stuck in the paddle, up and down
            if self.__dy > 0:
                self.__dy = -self.__dy
            else:
                pass
        elif self.touch_thing() is self.score_label:
            pass
        elif self.touch_thing() is self.img:
            pass
        elif self.touch_thing() is not None:
            self.window.remove(self.touch_thing())
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            self.__dy = -self.__dy
        elif self.touch_thing() is self.life1 or self.life2 or self.life3:
            pass

    # def bonus_ball(self):
    #     while self.ball.y < self.window.height//2:
    #         self.ball.fill_color = 'red'

    def win(self):
        """
        This method shows an image and label if the user wins the game by clearing
        all the bricks
        """
        if self.score == 100:
            win = GLabel('WIN!!')
            win.font = 'Times-50'
            self.window.add(win, 50, 235)
            self.window.add(self.img, 10, 25)
            self.window.remove(self.ball)

    def dead(self):
        """
        This method will check whether the ball falls below the window and will show a
        label 'Gameover' when there's no lives left.
        """
        if self.ball.y >= self.window.height:
            self.window.remove(self.ball)
            self.num_lives -= 1
            if self.num_lives > 0:
                self.reset_ball()
                # lives left
                if self.num_lives == 2:
                    self.window.remove(self.life3)
                elif self.num_lives == 1:
                    self.window.remove(self.life2)
            else:
                # last life
                if self.num_lives == 0:
                    self.window.remove(self.life1)
                lose = GLabel('GAMEOVER!!!')
                lose.font = 'Trattatello-60-italic'
                self.window.add(lose, x=(self.window.width-lose.width)//2, y=(self.window.height+lose.height)//2)

    def reset_ball(self):
        """
        This method resets the ball to the middle of the window and assign a new speed
        in order to reset the game.
        """
        self.ball = GOval(self.ball.width, self.ball.width, x=(self.window.width-self.ball.width)//2,
                          y=(self.window.height-self.ball.width)//2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.start = False
        self.set_ball_x_velocity()




