# Inheritance

class Animal:
	cool = True

	def make_sound(self, sound):
		print("This animal says: " + sound)


class Cat(Animal):
	pass

cat = Cat()
cat.make_sound("meow")

# properties

class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	# def set_age(self, new_age):
	# 	if(new_age < 0):
	# 		self._age = 0
	# 	else:
	# 		self._age = new_age
	
	# def get_age(self):
	# 	return self._age

	# We can use properties instead of these ^
	# We can directly access age now like harsha.age
	@property
	def age(self):
		return self._age

harsha = Human("sri", "harsha", 21)
# print(harsha.get_age())
# harsha.set_age(20)
# print(harsha.get_age())

print(harsha.age)