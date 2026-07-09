class railwayForm:
    name=''
    age=0
    destination=""
    train_no=0
    # This is a default contructor. It invokes automaticallly when an object is created
    def __init__(self):
        print("I am a default Constructor")
    # This is a parametarized constructor. It requires some arguments which are given when an object is created
    def __init__(self,name,age,destination,train_no):
        self.name=name
        self.age=age
        self.destination=destination
        self.train_no=train_no

    def displayInfo(self):
        print(f'The name of passenger is: {self.name}')
        print(f'The age of passenger is: {self.age}')
        print(f'The destination of passenger is: {self.destination}')
        print(f'The Train no. of passenger is: {self.train_no}')

passenger1=railwayForm()
passenger2=railwayForm()
passenger3=railwayForm()

myPassenger1=railwayForm("Harry",27,"Mumbai",7281)
myPassenger2=railwayForm("David",18,"Delhi",5626)
myPassenger3=railwayForm("John",42,"Goa",6217)
passenger1.displayInfo()
passenger2.displayInfo()
passenger3.displayInfo()

