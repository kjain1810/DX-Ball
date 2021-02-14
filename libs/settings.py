from colorama import Back, Fore

BOARD_HEIGHT = int(20)  # Height of the board
BOARD_WIDTH = int(40)  # Width of the board
BLOCK_WIDTH = int(3)  # Widh of 1 block
INIT_PADDLE_LENGTH = int(5)  # Lenght of paddle on each new life
PADDLE_OUTPUT = Back.WHITE + Fore.BLACK + "==="  # Output of the paddle
SLEEPTIME = 1  # Sleep time on life lost message

PROB_PADDLE_EXPAND = 0.1  # Probability of breaking brick release expand paddle
PROB_PADDLE_SHRINK = 0.1  # Probability of breaking brick release shrink paddle
PROB_PADDLE_GRAB = 0.1  # Probability of breaking brick release grab paddle
PROB_BALL_MULTIPLIER = 0.1  # Probability of breaking brick release ball multiplier
PROB_BALL_FAST = 0.1  # Probability of breaking brick release fast ball
PROB_BALL_THRU = 0.1  # Probability of breaking brick release thru ball

MIN_PADDLE_LENGTH = 3  # Minimum length of the paddle
MAX_PADDLE_LENGTH = 21  # Maximum length of the paddle

MAX_BALL_VELOCITY = 5  # Maximum velocity of the ball
