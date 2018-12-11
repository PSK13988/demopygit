from Student import Student


# function for saying hello
def say_hello(name):
    print("Hello Welcome, " + name)


student = Student("Mike", "NIIT", 30, "Male")

say_hello(student.name)
