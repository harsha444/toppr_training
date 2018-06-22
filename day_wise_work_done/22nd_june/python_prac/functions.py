import random
# doc strings->essential when using complex functions

def say_hello():
	"""A simple fucntion that returns the string hello"""
	return "Hello!"

print(say_hello.__doc__) # returns docstring in it

print(random.randint.__doc__) #gives doc in that function

# *args => Special operator which we can pass to fucntions. Gathers remaining arguments as tuple
# It is just a parameter, we can call it whenever we want

def sum_all_nums(num1, *args):
	print(num1)
	total = 0
	print(args) #is a tuple of all args
	for num in args:
		total+=num
	return total

sum_all_nums(1,2,3,4,5)

# **kwargs =>Special operator we can pass to functions.
# Gathers remaining keyword arguments as a dictionary

def fav_colors(**kwargs):
	print(kwargs)
	for person, color in kwargs.items():
		print(person, color)


fav_colors(colt="purple", ruby="red", ethel="teal")

# Ordering parameters

def display_info(a, b, *args, instructor="Colt", **kwargs):
	# print(args)
	return [a,b,args,instructor,kwargs]
print(display_info(1,2,3, last_name="Steele", job = "Instructor"))

# Unpacking tuples (use a * operator)

def sum_all_values(*args):
	total = 0
	for i in args:
		total+=i
	return total

l = [1,2,3,4,5] #or (1,2,3,4,5)
print(sum_all_values(*l)) # passing l will give an error

#Unpacking dictionaries - Use ** for that

def display_names(**kwargs):
	return(kwargs)

d = {"first":"Harsha", "second":"Sue"}

print(display_names(**d)) #Passing d will give an error