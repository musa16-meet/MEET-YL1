class Animal:
	def __init__(self,name,age,color,size):
		self.name =name
		self.age =age
		self.color =color
		self.size =size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
		#print(self.food)
		#print(self.dream)

	def eat_food(self,food):
		print("the Animal", self.name ,"is eating ",food)

	def sleep_dream(self,hours,dream):
		print("the Animal",self.name, "is sleeping for ", hours, "hours and dreaming of ",dream)
	

dog=Animal("sadek",22,"Yellow","tiny")
lion=Animal("nofar", 1 , "orange","big")

dog.print_all()
dog.eat_food("pizza")
dog.sleep_dream(10,"playing in the roof")
lion.print_all()
lion.eat_food("maqluba")
lion.sleep_dream(5,"hanging out with his friends")



