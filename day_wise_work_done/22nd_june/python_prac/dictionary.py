# 2 ways of creating a dictionary
cat = {"name":"blue", "age":3.5, "color":"white"}
cat2 = dict(name="kitty", age=2)
print(cat2)

# Accessing data in dictionary
print(cat["name"], cat2["name"])

# Iterating Dictionaries
# There are a couple of ways, since we have keys, values, and both.
# values -> .values() method
student = {
	"name":"Harsha",
	"owns_dog":False,
	"num_courses":4,
	"fav_lang":"Python",
	"is_hilarious":False,
	31:"My favourite number!"
}

print(student.values())

for i in student.values():
	print(i)

# Keys => .keys()
print(student.keys())
for i in student.keys():
	print(i)

# Accessing both:

for key,value in student.items():
	print(key,":", value)

# Checking if a key is in dict
if "name" in student: # or student.keys()
	print(True)

# Checkign if a value is in dict

if "Harsha" in student.values():
	print(True)

# Dictionary methods
student_copy = student.copy()

print(student_copy)

student_copy.clear()
print(student_copy)

student_copy = student.copy()
print(student_copy)

# == checks for values, is checks for memory

print(student_copy is student) # False since not the same memory

print(student_copy == student) # True since same values

# fromkeys - creates key-value pairs from comma separated values
# Mainly used to give default values
# We have to use a iterable(list) as first arg. else it will iterate through the letters

new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], 'unknown')

print("new_user: ", new_user)

new_user = new_user.fromkeys(['gender'], 'unknown')
print("new_user_with_gender: ", new_user) #initializes a new dict

# get => Retrieves a key in an object and return None instead of KeyError if key doesn't exist

print(student.get("name"))

# pop - takes in a key as an argument and deletes that key-value pair

x = student_copy.pop("name")
print("After pop: ", student_copy)
print(x) #should have the value in name

# popitem() - Removes a random item

student_copy.popitem()
print("After random poping: ",student_copy)

# Update keys and values in a dictionary with another set of key vaue pairs

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)

print(second) #prints {'a':1,....}

second['a'] = "cool" #updates our a in second

second.update(first) #overrides our updates again

second.update({}) #doesn't do anything, it can only update or override things. Can' remove existing ones

# Dictionary comprehensions
# Syntax: {__:__ for__in__}
# iterates over keys by default
# To iterate over keys and values, use .items()

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key:value**2 for key,value in numbers.items()}

print("squared_numbers: ", squared_numbers)

test1 = {num:num**2 for num in [1,2,3,4,5]}
print(test1)

str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(len(str1))}
print("combo:", combo)
#Conditional logic
num_list = [1,2,3,4]

num_dict = {num:("Even" if num%2 == 0 else "Odd") for num in num_list}
print("num_dict", num_dict)
