class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return("Human named " + self.first + " " + self.last)

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age = 0)
        return "You can't add that"

j = Human("Jessy", "Mortana", 47)
k = Human("Kevin", "O'brien", 33)

print(j)
print(len(j))
print(j+k)
