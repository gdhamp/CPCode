# Circuit Playground NeoPixel
import time
import board
import digitalio



def main():
	button = digitalio.DigitalInOut(board.BUTTON_A)
	button.switch_to_input(pull=digitalio.Pull.DOWN)


	while True:
		count = 0

		if button.value:
			while button.value:
				count += 1
				continue
		print(count)


if __name__=="__main__":
	main()
