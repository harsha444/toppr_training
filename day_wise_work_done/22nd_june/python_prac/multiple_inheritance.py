class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming")

    def greet(self):
        print(self.name + " from Sea")

class Amulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + " is walking")

    def greet(self):
        print(self.name + " from land")

# When there is a multiple inheritance, the class that you pass first gets higher priority
# So. pingu.greet() gives a result of pingu from sea since we passed Aquatic first
class Penguin(Aquatic, Amulatory):
    def __init__(self, name):
        super().__init__(name)

pingu = Penguin("pingu")
print(pingu.name)
pingu.greet()
