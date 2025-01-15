class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('barking')

class Cat(Mammal):
    def be_annoying(self):
        print('annoying')
    
cat1 = Cat()
cat1.be_annoying()