from operator import is_not


class student:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        if type(self.age) != int:
            print("age must be given in numbers")
        elif type(self.name)!= str:
            print("name must be given in string")
        else:
            print("valid age and name")
age=int(input())
name=input()
s=student(age,name)

class student1:
    def __init__(self,age,name):
        self.age=age
        self.name=name

        if self.age__class__ != int:
            print("enter the age in number")
        elif self.name__class__!=str:
            print("enter the name in string format")
        else:
            print("valid name and age")
age=int(input())
name=input()
s=student1(age,name)


class student3:
    def __init(self,age,name):
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