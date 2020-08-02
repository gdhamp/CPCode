# Circuit Playground NeoPixel
import time
import board
import digitalio
import neopixel

numPixels = 10

pixels = neopixel.NeoPixel(board.NEOPIXEL, numPixels, brightness=0.2, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


def clearLEDs():
	pixels.fill(OFF)
	pixels.show()



def main():
	button = digitalio.DigitalInOut(board.BUTTON_A)
	button.switch_to_input(pull=digitalio.Pull.DOWN)

	index = 0
	color = BLUE

	while True:

		if button.value:
#			clearLEDs()
			pixel[index-1] = OFF
			pixels[index] = color
			pixels.show()
			index += 1
			if index == numPixels:
				index = 0
				if color == BLUE:
					color = RED
				else:
					color = BLUE
			while button.value:
				continue


if __name__=="__main__":
	main()
