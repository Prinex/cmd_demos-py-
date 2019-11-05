import random
import time
import os


words = ['rainbow', 'computer', 'science', 'programming',  
         'python', 'mathematics', 'player', 'condition',  
         'reverse', 'water', 'board', 'geeks']


def gameOn():
	# generating a random word
	
	random_word = random.choice(words)
	return check(random_word)
	

# printing the words an starting the game after 4 seconds
def initializeGame():
	print("Guess the word: " + '\n')
	for i in range(len(words) - 1):
		print(words[i]) 
	print('\n')

	print("The game will start in: ")
	for i in range(4, 0, -1):
		print(str(i))
		time.sleep(i)
	print("Game ON" + '\n')
	time.sleep(1)
	os.system('cls')

	return gameOn()


def check(rand_word):
	tries = 12
	
	
	print("Guess the characters: ")
	print("You have " + str(tries) + " tries")
	myGuesses = ""
	while tries != 0:

		failed = 0
		
			

		for char in rand_word:
			if char in myGuesses:
				print(char)
			else:
				print('_')
				failed += 1
			
		if failed == 0:
			print("You win! The word is: ", rand_word)
			break
		
		guess = input("Guess the characters: ")
		

		if guess in rand_word:
			myGuesses += guess
		
		if guess == "":
			print("Please guess a character")

		if guess not in rand_word:
			tries -= 1
			print("Wrong")
			print("tries left: " + str(tries))
		
		if tries == 0:
			print("You loose... The word was: ", rand_word)
			break


	return None 
		



initializeGame()