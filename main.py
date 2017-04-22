import battle
import hero
import random

def game():
	name=raw_input("What is your name? ")
	player=hero.Hero(name)
	print("		Welcome to the Brutal Game, "+player.name+"!")

	player.status()
	battleStatus = raw_input("Enter Shop (s) / Enter Arena (a) / Exit (x)? ")
	while not (battleStatus is "x") and (player.health>0):
		if (battleStatus is "s"):
			print("		Welcome to the Battle Shop! How can we help you?")
			purchase = raw_input("Buy a potion for 50g (p) / Buy a weapon for 100g (w) / Exit shop (x)? ")
			if (purchase is "p"):
				print("		You drank a potion to increase your health!")
				player.gold-=50
				player.drinkPotion()
			elif (purchase is "w"):
				print("		You've added a new weapon to your arsenal to increase your skills!")
				player.gold-=100
				player.getWeapon()
		elif (battleStatus is "a"):
			print("		Now entering the Arena!")
			fightNow(player)
		elif (battleStatus is "x"):
			break
		player.status()
		battleStatus = raw_input("Enter Shop (s) / Enter Arena (a) / Exit (x)? ")
	
def fightNow(active):
	active.status()

	enemyHealth=random.randrange(int(active.health))
	enemySkills=random.randrange(int(active.skills))
	enemyGold=random.randrange(int(active.gold))
	print("Enemy status...")
	print("	Health: "+str(enemyHealth))
	print("	Skills: "+str(enemySkills))
	print("	Gold: "+str(enemyGold))
	
	fightStatus=""

	while (active.health>0) and (enemyHealth>0) and (fightStatus!="e"):
		fightStatus=raw_input("Attack (a) / Defend (d) / Escape (e) ? ")
		if (fightStatus is "a"):
			print("		You attack! Your enemy attacks back!")
			enemyHealth-=active.skills
			active.health-=enemySkills
		elif (fightStatus is "d"):
			print("		Your enemy attacks! You deflect the blow!")
			active.health-=(enemySkills/10)
			active.skills+=(active.health/10)
		elif (fightStatus is "e"):
			break
		print("Enemy status...")
		print("	Health: "+str(enemyHealth))
		print("	Skills: "+str(enemySkills))
		print("	Gold: "+str(enemyGold))
		active.status()
	if (enemyHealth<=0):
		active.gold+=enemyGold
		print("		You have defeated your enemy and taken their gold as a reward!")
	if (active.health<=0):
		print("		Oh, no! You have perished in battle...")


game()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("This silly game created by: Alacr1ty")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#decision=raw_input("Start a new game? (y/n): ")
#while not (decision is "n") or (decision is "N"):
#	if (decision is "y") or (decision is "Y"):
#		game()
#	else:
#		decision=raw_input("Start a new game? (y/n): ")

