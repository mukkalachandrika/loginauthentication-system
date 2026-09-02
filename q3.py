attempts = 0
def login_required(func):
    def wrapper(username, password, exam_name):
        if username == "admin" and password == "1234":
            return func(username, password, exam_name)
        else:
            print("Invalid credentials")
    return wrapper
def track_attempt(func):
    def wrapper(*args, **kwargs):
        global attempts
        attempts=attempts+1
        return func(*args, **kwargs)
    return wrapper
@track_attempt
@login_required
def start_exam(username, password, exam_name):
    print("Exam started for", username)
    print("Exam name:", exam_name)
    start_exam("admin", "1234", "Python")
    start_exam("admin", "1234", "Java")
    start_exam("user", "5678", "Python")
    print("Total exam attempts:", attempts)



balance = 10000
def authenticate(func):
    def wrapper(*args, **kwargs):
        username = args[0]
        pin = args[1]

        if username == "admin" and pin == "1234":
            return func(*args, **kwargs)
        else:
            print("Invalid credentials")
    return wrapper
@authenticate
def withdraw(username, pin, amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
withdraw("admin", "1234", 2000)
withdraw("user", "1111", 1000)
withdraw("admin", "1234", 3000)
