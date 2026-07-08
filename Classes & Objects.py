# Class is made by class keyword:
class Person:
    name='Harry'
    age=23
    occupation='Software Developer'

    def info(self):
        print(f'{self.name} is a {self.age} years old  {self.occupation}')
        
# Objects of class are mad in the following way:
a=Person()
b=Person()
b.name='David'
b.age=27
b.occupation='Web Developer'
c=Person()
c.name='John'
c.age=30
c.occupation='Python Developer'
a.info()
b.info()
c.info()
