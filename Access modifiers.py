# Public Variable 
class Student:
    def __init__(self,n):
        self.num=n
    def show(self):
        print(f"The number is :{self.num}")

st=Student(3)
st.show()

# Private Attributes
class Employee:
    def __init__(self,name,id) -> None:
        self.name=name
        self.__id=id

e=Employee('Harry',23)
print(e.name)

# print(e.__id) #This will throw an error because it can't be accessed directly
print(e._Employee__id) #But it can be accessed indirectly by name mangling

# Protected Attriutes
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())   
print(dir(obj)) #This method tells that which functions or aattributes can be executed by obj
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())