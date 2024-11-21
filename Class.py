"""class myclass():
    def __init__(self):
        self.name="Maideen"
        self.age=21
    def display(self):
        print(self.name)
        print(self.age)
obj=myclass()
obj.display()"""

class myclass1:
    def parent(self):
        print("This is parent class")
    def display(self):
        print("Display function")
class child(myclass1):
    print("This is v]child class")

obj=child()
obj.parent()
obj.display()
