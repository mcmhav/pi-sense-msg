from sense_hat import SenseHat
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Pi sense hat messenger.')
parser.add_argument(
	'message',
	type=str,
        help='message to be displayed',
)
parser.add_argument(
        'sleep_time',
        type=float,
	nargs='?',
        help='how long to sleep between letters',
	default=0.4,
)

args = parser.parse_args()


def show_message(message, sleep_time):
	print('Showing message:', message)

	sense = SenseHat()

	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 255, 0)
	white = (255, 255, 255)
	yellow = (255, 255, 0)

	for letter in message:
		sense.show_letter(letter, red)
		sleep(sleep_time)

	sense.clear()

if __name__ == '__main__':
    show_message(args.message, args.sleep_time)

