class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display_details(self):
        print(f"The name of employee is: {self.name} and the Id is: {self.id}")
    
class Programmer(Employee):
    def show_language(self):
        print("The default Lanhuage of programmer is Python")

emp=Employee('Harry',52)
emp2=Programmer('David',72)
emp.display_details()
emp2.display_details()
emp2.show_language()