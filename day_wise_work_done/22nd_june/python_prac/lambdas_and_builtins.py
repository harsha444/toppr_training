# lambdas are anonymous functions

def square(num): return num*num #Normal function

square2 = lambda num: num*num

add = lambda a,b: a + b

print(add(2,3)) #5
print(square.__name__) #function
print(square2.__name__) #lambda
print(add.__name__) #lambda

# Map => A standard function that accepts at least 2 args, a function and a iterable.

l = list(range(0,10))
mul2 = lambda n: n*2

res = list(map(mul2, l))
print(res)
# for i in res:
# 	print(i)

# Filter - Returns filtered object which can be converted to other iterables.
# Object contains  only the values that return true to the lambda

evens = lambda n: n%2 == 0

res = list(filter(evens, l))

print(res)

users = [
	{"user":"samuel", "tweets": ["I love cake", "Something else"]},
	{"user":"raj", "tweets": ["I love cake"]},
	{"user":"prabash", "tweets": []},
	{"user":"mani", "tweets": []},
]

inactive = lambda detail: len(detail["tweets"]) == 0

inactive_users = list(filter(inactive, users))

print("inactive_users: ", inactive_users)

# Combining map and filter

inactive_users = list(map(lambda detail:detail["user"].upper(), filter(lambda detail: len(detail["tweets"])==0, users)))

print(inactive_users)

# Comprehension

inactive_users2 = [user["user"].upper() for user in users if not user["tweets"]]
print(inactive_users2)

# all and any

evens = [2,3,4,5,6,7,8]

res = all([n%2==0 for n in [2,4,7]])
print(res)

# sorted() => can be used wth any iterables

print(sorted(users, key=lambda user:user['user']))

songs = [
	{"title": "happy birthday", "playcount":1},
	{"title": "Survive", "playcount":6},
	{"title": "YMCA", "playcount":99},
	{"title": "Toxic" , "playcount":31}
]

print(sorted(songs, key=lambda n: n["playcount"]))
# min and max
print(min(songs, key=lambda n: n["playcount"])["title"])

# Zip - makes an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples, where i-th tuple contains the i-th element from each of the argument sequences or iterables.

first_zip = zip([1,2,3],[4,5,6])
print(list(first_zip))
print(dict(first_zip))

# Unpacking 
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*five_by_two)))

# Complex zip examples

mids = [80, 91, 78]
finals = [98,89,34]

final_grades = [max(num) for num in zip(mids, finals)]
print(final_grades)