att=0
def dec1(func):
    def wrapper(*args,**kwargs):
        global att
        att=att+1
        func(*args,**kwargs)
    return wrapper
@dec1
def login(username,password):
    print("Login attempted by",username)
    @track_attempt
    @login_required
    def start_exam(username, password, exam_name):
        print("Exam started for", username)
        print("Exam name:", exam_name)
    start_exam("admin", "1234", "Python")
    start_exam("admin", "1234", "Java")
    start_exam("user", "5678", "Python")
    print("Total exam attempts:", attempts)



class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

        if type(self.age) != int:
            print("Error: Age must be an integer")
        elif type(self.name) != str:
            print("Error: Name must be a string")
        else:
            print("Valid age and name")


age = int(input("Enter age: "))
name = input("Enter name: ")

p = Person(age, name)

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

        if not isinstance(self.age, int):
            print("Error: Age must be an integer")
        elif not isinstance(self.name, str):
            print("Error: Name must be a string")
        else:
            print("Valid age and name")


age = int(input("Enter age: "))
name = input("Enter name: ")

p = Person(age, name)

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

        if self.age.__class__ != int:
            print("Error: Age must be an integer")
        elif self.name.__class__ != str:
            print("Error: Name must be a string")
        else:
            print("Valid age and name")


age = int(input("Enter age: "))
name = input("Enter name: ")

p = Person(age, name)