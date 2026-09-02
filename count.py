class A:
    x=20
    count=0
    def __init__(self):
        self.y=120
        self.z=40
        self.a=140
        A.count+=1
obj=A()
print(A.count)


class user:
    def __init__(self,age):
        if(age>18):
            self.age=age
        else:
            print("age must be greater than 18")
user1=user(11)
