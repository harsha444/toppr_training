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