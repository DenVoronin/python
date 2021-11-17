class Animal:
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print("Cat say mew")

class Cow(Animal):
    def voice(self):
        print("Cow say mooo~")

class Fish(Animal):
    def voice(self):
        print("Fish say ...")

cat = Cat()
cat.voice()

cow = Cow()
cow.voice()

fish = Fish()
fish.voice()
