tasks = ['Install python', 'Learn python', 'Take a break']
print("tasks:", tasks)

# A way of creating lists
numbers = list(range(1,10))
print("numbers:", numbers)

for i in range(len(numbers)):
	print(numbers[i])

# using in 

colors = ["Purple", "Red", "White", "Black"]

print("Black" in colors)

# List methods
data = [1, 2, 3]
data.append(0)
print("Appended_data: ",data)
data.sort()
print("sorted data: ", data)
# using .append(), we can append one item, or a collection of items as a list
# To append items from a list individually, use .extend()

data.extend([4, 5, 6, 7])

print("Extended data: ",data)
print("length of list: ", len(data))

# Insert to insert in a postion of list

first_list = [1, 2, 3, 4]
first_list.insert(2, "hi")
print("After insertion: ", first_list)

# clear - Removes all items in list at once

first_list.clear()

print("Emptied list: ",first_list)
# pop -> Removes the item at given position in the list, and return it.
# if no index is specified, removes and returns the last item in the list

first_list = [1, 2, 3, 4]
first_list.pop()
print("After popping: ",first_list) 
first_list.pop(1)
print("After popping index 1 ele: ", first_list)

# remove - removes the first item from the list whose value is x.
# Throws an error if not found

first_list = [1,2,3,4,4,4,4]
first_list.remove(3)
print("after removing 3", first_list)

# index - returns index of a specified item in the list
# We can also specify a starting point, and ending point. To where the search must start from.

numbers = [5,6,7,8,5,9,10]
print("6 index: ", numbers.index(6)) # returns 1
print(numbers.index(5, 2)) #starts to search 5 from index 2
print(numbers.index(5,2,5)) # searches 5 from index 2 till index 5

# Count - returns the number of times x appears in a list

numbers = list(range(0,10))
print("number 1 Count: ",numbers.count(1)) #returns 1

# reverse - inplace reversal of elements

numbers.reverse()
print("reversed: ", numbers)

# Sort()

print("Sorted: ", numbers.sort())

# join - joins list/string items

words = ["Coding", "is", "fun"]

joined = ' '.join(words)
print(joined)

# Slices
numbers = list(range(0,10))
print(numbers[0:7:2])

# list comprehensions [__for__n__]
nums = list(range(10))

mul10 = [x*10 for x in nums]

print("mul10: ",mul10)

# Conditional logic:
evens = [num for num in nums if num%2 == 0]
print("evens: ",evens)

with_vowels = "This is so much fun"

no_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print("no_vowels: ", no_vowels)