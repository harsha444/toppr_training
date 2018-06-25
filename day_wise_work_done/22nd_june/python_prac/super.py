class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self, sound):
        return ("This animal makes a " + self.sound)

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
    def play(self):
        print(self.name + " plays with " + self.toy)


blue = Cat("snoopy", "scottish", "String")
blue.play()

class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return("There are currently "+ str(self.active_users) + " on the site")

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1

    def full_name(self):
        return(self.first + " " + self.last)

    def is_senior(self):
        return self.age >= 65

class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return (self.full_name() + " removed a post from " + self.community)

jasmine = Moderator("Jasmine", "O really", 32, "Piano")
print(jasmine.full_name())
print(jasmine.remove_post())
