'''class computer:
    def config(self):
        print("yes")
lenova=computer()
computer.config()
dell=computer()
dell.config()'''





###CONSTRUCTOR
class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
       # print("ID: %id \name:%s" %self.id,selfname)
        print(self.id,self.name)
emp1=Employee("jhon",3456786)
emp2=Employee("david",987656)
emp1.display()
emp2.display()
