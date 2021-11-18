i=0
class Animal:
    
    def __init__(self):
        if issubclass (self.__class__, Animal):
           global i
           i+=1
        
      
    def voice(self):
        pass

    def test():
        print(i)

        
class Cat(Animal):
   
    def __init__(self):
        super().__init__()
    def voice(self):  
        print("Cat say mew")

class Cow(Animal):
    def __init__(self):
        super().__init__()
    def voice(self):
        print("Cow say mooo~")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def voice(self):
        print("Fish say ...")

cat = Cat()
cat.voice()

cow = Cow()
cow.voice()

fish = Fish()
fish.voice()

Animal.test()
