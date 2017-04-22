import random
import hero

def game():
	highest=main.bob.skills
	answer=random.randrange(highest)

	guess=raw_input("enter your goddamn number, bitch: ")

	while not (int(guess) is answer):
		if (int(guess)<answer):
			print("Answer higher, maing")
		elif (int(guess)>answer):
			print("answer lower than that, daw...")
		guess=raw_input("enter your goddamn number, bitch: ")
	main.bob.skills+=10
	print("You got that shit, yo!!!")