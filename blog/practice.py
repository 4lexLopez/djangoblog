# django-admin startproject myproject
# python manage.py migrate
# python manage.py runserver


# djang-admin startproject myproject
# python manage.py migrate
# python manage.py runserver

# source ./bin/activate

# django-admin startproject myproject
# python manage.py migrate
# python manage.py runserver
# django-admin startapp myapp

# django-admin startproject myproject
# django-admin startapp myapp
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

class Person:
    def __init__(self, a, b):
        self.fname = a
        self.lname = b

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    def greet(self):
        return f"hi I'm {self.fname}"
    
class Student(Person):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.grade = c

    def greet(self):
        return f"HEllo! I'm {self.lname}, I'm in {self.grade} grade"
    
p1 = Person("a","b")
print(p1)

print(p1.greet())

s1 = Student("c", 'd', 3)
print(s1.greet())