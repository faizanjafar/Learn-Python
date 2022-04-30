

class Person():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Teacher(Person):
    def __init__(self,name, age):
        Person.__init__(self,name)
        self.age = age
    
    def get_name(self):
        return self.name + " Teacher"

class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self,name)
        self.age = age
        self.roll = roll
    
    def get_name(self):
        return self.name + " Student"

class Cls(Teacher, Student):
    def __init__(self, name, age, roll):
        Teacher.__init__(self,name, age)
        Student.__init__(self,name, age, roll)
    
c = Cls("Ali", 10, 200)
print(c.get_name())