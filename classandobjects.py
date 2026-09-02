class A:
    pass
obj1=A()
print(type(obj1))
obj2=A()
print(id(obj1))
print(id(obj2))

class A:
    a=20
obj=A()
print(A.a)

class phone:
    software='android'
    count=0
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        phone.count += 1

phone1=phone('samsung','100000')
print(phone1.price)
print(phone1.brand)
print(phone1.count)
print(phone1.software)



class A:
    x=20
    def __init__(self, y):
        self.y=y
obj1=A("hey")
obj2=A("Hello")
obj3=A("hi")
print(A.__dict__)
print(obj1.__dict__)
print(obj2.__dict__)
obj1.x=100
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
obj2.__dict__['z']=40
print(obj2.__dict__)

print("Data in obj1")
print(obj1.x)
print(obj1.y)
print("Data in obj2")
print(obj1.x)
print(obj2.y)
print("Data in obj3")
print(obj3.x)
print(obj3.y)
A.x=40
print(obj1.x)
print(obj2.x)
print(obj3.x)
obj1.x=100
print(obj1.x)
print(obj2.x)
print(obj3.x)
class A:
    x=20
    def __init__(self,y):
        self.y=y
        self.x=40
class A:
    x=20
    count=0
    def __init__(self):
        self.y=120
        self.z=40
        self.a=140
        A.count+=1



obj=A()
class student:
    student='chandrika'
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1


student1=student("chandrika",21)
student2=student("chandu",23)
print(student1.__dict__)
print(student2.__dict__)
print(student1.name)
print(student1.age)
print(student1.count)
print(student1.student)


#1
class Employee:
    company="TechCorp"
    employee_count=0
    def __init__(self, name, department, salary, experience):
        self.name=name
        self.department=department
        if salary<0:
            self.salary=0
        else:
            self.salary=salary
        if experience<0:
            self.experience=0
        else:
            self.experience=experience
        if self.experience>5:
            self.bonus=self.salary*15/100
        elif self.experience>=3:
            self.bonus=self.salary*10/100
        else:
            self.bonus=self.salary*5/100
        self.final_salary=self.salary+self.bonus
        self.pay_details={
            "name":self.name,
            "salary":self.salary,
            "experience":self.experience,
            "bonus":self.bonus,
            "final_salary":self.salary
        }
        Employee.employee_count+=1
        self.employee_id=Employee.employee_count
emp1=Employee("chandrika","IT",100000,8)
emp2=Employee("chandu","Accounts",70000,6)
print(emp1.__dict__)
print(emp2.__dict__)



#2
class MobilePurchase:
    store_name="Smart Mobiles"
    purchase_count=0
    def __init__(self, customer, brand, price, storage, quantity):
        self.customer=customer
        self.brand=brand
        if price<=0:
            self.price=0
        else:
            self.price=price
        if quantity<=0:
            self.quantity=0
        else:
            self.quantity=quantity
        if storage in[64, 128, 256, 512]:
            self.storage=storage
        else:
            self.storage=64
        self.total_price=self.price*self.quantity
        if self.total_price>50000:
            self.discount=self.total_price*10/100
        else:
            self.discount=self.total_price*5/100
        self.final_price=self.total_price - self.discount
        self.purchase_details={
            "customer":self.customer,
            "brand":self.brand,
            "price":self.price,
            "storage":self.storage,
            "quantity":self.quantity,
            "total_price":self.total_price,
            "discount":self.discount,
            "final_price":self.final_price
        }
        MobilePurchase.purchase_count+=1
p1=MobilePurchase("chandrika","iphone",100000,128,1)
p2=MobilePurchase("sneha","Samsung",30000,126,3)
print(p1.__dict__)
print(p2.__dict__)


#3
class Product:
    store="Shopeasy"
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.product_details={
            "name":self.name,
            "price":self.price,
            "quantity":self.quantity,
            "total_price":self.price*self.quantity
        }

p1=Product("Laptop",50000,3)
p2=Product("keyboard",1300,4)
p1.price=56000
p1.product_details["price"]=60000
print(p1.__dict__)


#thursday practice
class BankAccount:
    bank_name = "ABC Bank"
    def _init_(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        if balance < 0 :
            self.balance = 0
        else:
            self.balance = balance
account1 =BankAccount("Alice", 67543987490, 1000)
account2 =BankAccount("Bob", 6737223234, 500)
def display(obj):
    # print(obj._dict_)
    print("Bank name : " ,obj.bank_name)
    print("Account Holder : ",obj.account_holder)
    print("Account Number :" ,obj.account_number)
    print("Account Balance : ",obj.balance)
display(account1)
display(account2)

