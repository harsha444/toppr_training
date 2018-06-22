# 1
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

combined = {list1[i]:list2[i] for i in range(len(list1))}
print("combined: ", combined)

# 2
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

person_dict = {k:v for k,v in person}
print("person_dict: ", person_dict)

# 3
vowels = "aeiou"
vowels_dict1 = {k:0 for k in vowels}
print("method 1: ",vowels_dict1)

vowels_dict2 = {}.fromkeys(vowels, 0)
print("method 2: ", vowels_dict2)

# 4 ascii dictionary

ascii_dict = {count: chr(count) for count in range(65, 91)}
print(ascii_dict)

