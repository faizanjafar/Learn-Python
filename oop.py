
class Person:
    """asdasdasd"""
    def __init__(self, name, age):
        print("person")
        self.name = name
        self.age = age

    def sleeping(self):
        print("Sleeping.....")

    def eating(self):
        print("Eating.....")
    
    def __repr__(self):
        return "asdlkadsjflkj"

class Person2:
    """asdasdasd"""
    def __init__(self, name, age):
        print("person2")
        self.name = name
        self.age = age

    def sleeping(self):
        print("Sleeping..... person2")

    def eating(self):
        print("Eating..... person2")
    
    def __repr__(self):
        return "asdlkadsjflkj"


class Student(Person2,Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

s = Student("Ali",20,267)
s.sleeping()
s.eating()
print(s.__dir__())