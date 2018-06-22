class User:
	active_users = 0 # Class Attribute
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def full_name(self):
		return (self.first, " ", self.last)
	def initials(self):
		return (self.first[0], " ", self.last[0])
	def likes(self, thing):
		return (self.first+" likes "+thing)
	def logout(self):
		User.active_users -= 1
		return (self.first+" logged out")

user1 = User("sri", "harsha", 21)
user2 = User("raj", "kamal", 20)
print(user1.first, user1.last, user1.age)

# _name => private 
#__name => name mangling
#__name__ => dunder methods which are used to override existing python methods. Not a good idea using this convention in our own methods


class Person:
	def __init__(self):
		self.name = "Tony"
		self._secret = "hi"
		self.__msg = "I like turtles!"
	# def doorman(self, guess):
	# 	if(guess == self._secret):
	# 		print("cool")

p = Person()

print(p.name)
print(p._secret)
# print(p.__msg) #Name mangling is done here, how msg is changed can be seen in dir below
print(dir(p))

# Adding instance methods

print(user1.likes("ice cream"))

print(User.active_users) #Class attributes

class Pet:
	pets_allowed = ("dog", "cat", "mouse", "hampster")

	def __init__(self, name, species):
		if species not in Pet.pets_allowed:
			raise ValueError("It is not a valid species")
		self.name = name
		self.species = species
	def set_species(self, species):
		if species not in Pet.pets_allowed:
			raise ValueError("It is not a valid species")
		self.species = species

cat = Pet("snuffy", "cat")
dog = Pet("mark", "dog")
# tiger = Pet("akira", "tiger")
cat.set_species("tiger")

# Class methods
# Methods that are not concerned with instances, but class itself
# (with the @classmethod decorator)
