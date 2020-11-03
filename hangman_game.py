import random
def hangman():
	
	word = random.choice(["autumn", "wind", "school", "love", "thor", "pokemon", "rain", "ocean", "stranger", "happiness"])
	valid_letters = "abcdefghijklmnopqrstuvwxyz"
	turns = 10
	guess_made = ""
	
	while len(word) > 0:
		main = ""
		missed = 0
		
		for letter in word:
			if letter in guess_made:
				main = main + letter
			else:
				main = main + "_" + " "
		if main == word:
			print(main)
			print("You won!")
			break
		
		print("Guess the word: ", main)
		guess = input()
		
		if guess in valid_letters:
			guess_made = guess_made + guess
		else:
			print("Enter a valid character")
			guess = input()
		
		if guess not in word:
			turns = turns - 1
			if turns == 9:
				print(turns, "attempts left")
				print(" ---------- ")
			if turns == 8:
				print(turns, "attempts left")
				print(" ---------- ")
				print("     0      ")
			if turns == 7:
				print(turns, "attempts left")
				print(" ---------- ")
				print("     0      ")
				print("     |      ")
			if turns == 6:
				print(turns, "attempts left")
				print(" ---------- ")
				print("     0      ")
				print("     |      ")
				print("    /       ")
			if turns == 5:
				print(turns, "attempts left")
				print(" ---------- ")
				print("     0      ")
				print("     |      ")
				print("    / \     ")
			if turns == 4:
				print(turns, "attempts left")
				print(" ---------- ")
				print("   \ 0      ")
				print("     |      ")
				print("    / \     ")
			if turns == 3:
				print(turns, "attempts left")
				print(" ---------- ")
				print("   \ 0 /    ")
				print("     |      ")
				print("    / \     ")
			if turns == 2:
				print(turns, "attempts left")
				print(" ---------- ")
				print("   \ 0 /|   ")
				print("     |      ")
				print("    / \     ")
			if turns == 1:
				print(turns, "attempts left")
				print("Last breaths counting. Take care!")
				print(" ---------- ")
				print("   \ 0_|/    ")
				print("     |      ")
				print("    / \     ")
			if turns == 0:
				print("You lost.")
				print("You let a kind man die.")
				print(" ---------- ")
				print("     0_|    ")
				print("    /|\     ")
				print("    / \     ")
				break	

name = input("Enter your name: ")
print("Welcome,", name)
print("-------------------")
print("Try to guess the word in less than 10 attempts.")
hangman()
print()