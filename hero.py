class Hero:
	'''
	Hero Class
	'''
	def __init__(self,name):
		self.name=name
		self.health=50
		self.skills=20
		self.gold=500
	
	def status(self):
		print(self.name+"'s status...")
		print("	Health: "+str(self.health))
		print("	Skills: "+str(self.skills))
		print("	Gold: "+str(self.gold))

	
	def drinkPotion(self):
		self.health+=25

	def getWeapon(self):
		self.skills+=10