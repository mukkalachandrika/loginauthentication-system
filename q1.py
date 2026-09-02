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
