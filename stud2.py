class student1:
    def __init__(self, age, name):
        self.age = age
        self.name = name

        if self.age.__class__ != int:
            print("enter the age in number")
        elif self.name.__class__ != str:
            print("enter the name in string format")
        else:
            print("valid name and age")


age = int(input())
name = input()
s = student1(age, name)
