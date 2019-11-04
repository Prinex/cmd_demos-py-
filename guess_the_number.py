import time
import random
import os

# Starting / Exiting the game
# initializing the random number and the number of tries
randomNumber = random.randint(1, 100)
tries = 7

def game():
	while True:
		option = str(input("Press S/E (to start or stop the game): "))
		
		if option.upper() == 'S':
			print("The game is starting...\n")
			time.sleep(1.5)
			return initialize(tries)
			
		elif option.upper() == 'E':
			print("Exiting the game...\n")
			time.sleep(1.5)
			break

		elif option == "":
			print("Please select an option.")
			return game()
		else:
			print("That's not a valid option. Please try Again...")
			return game()

	return None

# Initializing the game
def initialize(tries):
	print("The current number of tries: " + str(tries))
	myNumber = int(input("Enter a number between [1, 100]: "))
	return check(myNumber, tries)


def reinitialize(tries):
	
	myNumber = int(input("Enter a number between [1, 100]: "))
	return check(myNumber, tries)
	

# Checking the equality between random number and your number
def check(myNo, tries):
	for i in range(tries, 0, -1):
		
		if myNo == randomNumber:
			print("CORRECT!")
			return restart()

		elif tries == 1:
			print("You lost... The number was " + str(randomNumber))
			return restart()

		elif myNo != randomNumber:
			tries -= 1
			print("WRONG!")
			print("You have " + str(tries) + " more tries.")
			if myNo < randomNumber:
				print("Hint: The number is greater than yours...\n")
				return reinitialize(tries)

			else:
				print("Hint: The number is less than yours...\n")
				# reinitializing your input
				return reinitialize(tries)
	return None
		
# restarting the game
def restart():
	randomNumber = random.randint(1, 100)
	tries = 7
	print("Restarting the game...")
	time.sleep(2.2)
	os.system("cls")
	return game()

game()
