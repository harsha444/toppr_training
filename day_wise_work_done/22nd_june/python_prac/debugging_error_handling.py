# raising an error

# raise NameError("blah")

def colorize(text, color):
	colors = ("red", "cyan", "blue", "green", "magenta")
	if(type(text) is not str):
		raise TypeError("text must be a str")
	if(color not in colors):
		raise ValueError("color is not in our color list")
	print(text, color)

colorize("hello", "red")

# Try and Except

try:
	foobar
except:
	print("PROBLEM!")
print("After the try")

# 

def get(d, key):
	try:
		return d[key]
	except KeyError:
		return None

d = {"name": "Harsha"}

print(get(d, "city"))

# Else, Finally
while(1):
	try:
		num = int(input("Please enter a number: "))
	except:
		print("That's not a number")
	else: #Else will run when except does not 
		print("Nice, that's a number")
		break
	finally:
		print("Gets printed no matter what ")

def divide(a, b):
	try:
		result = a/b
	except:
		print("Please enter valid value for b")
	else:
		print("result is: ", result)

divide(1, 0)