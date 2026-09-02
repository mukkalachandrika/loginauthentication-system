
class student3:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        if not isinstance(self.age,int):
            print("enter valid input")
        elif not isinstance(self.name,str):
            print("enter valid input")
        else:
            print("valid age and number")
age=int(input())
name=input()
s2=student3(age,name)