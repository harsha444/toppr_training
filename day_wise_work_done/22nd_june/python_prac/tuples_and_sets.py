# Tuples - immmutable
x = (1,2,3)
# x[0] = 4  # will throw an error

# Tuples can be used as keys in dictionaries
locations = {
	(35.5,31.2) : "Tokyo Office",
	(21.8, 54.6) : "Bombay Office"
}

print(locations[(21.8, 54.6)])
# There can be nested tuples, just like lists

# Sets - group of unique items, no ordering=> no accessing through index values

s = set({1,2,3,4,5,5,5})
print("set: ", s)

print(4 in s)

# Changing list to set and set to list is done by direct wrapping

# Set methods and set math

s = set([1,2,3])
s.add(4)
print("after adding: ", s)

s.remove(4) # or .discard()
print("after removing: ", s)

# copy

another_s = s.copy()
print("copy of s: ", another_s)

# clear 

another_s.clear()
print("clear: ", another_s)

# Set math - intersection, symmetric_difference, union

s1 = set([1,2,3])
s2 = set([3,4,5])
print(s1 | s2)

print(s1 & s2)

print(s1 - s2)