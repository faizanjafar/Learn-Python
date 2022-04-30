from functools import cached_property
# @classmethod
# @property
# @staticmethod
# @cached_property

class Student():
    name = None
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    @classmethod
    def create_from_roll(cls, roll):
        cls.name = "Moin"
        cls.age = 20
        cls.roll = roll
        return cls

    @staticmethod
    def print_hello(name):
        print("Hello ",name)

    @property
    def get_name(self):
        return self.name
    
    @cached_property
    def get_age(self):
        print('calling get age')
        return self.age

stu = Student("ali",20,267)
print(stu.get_age)
print(stu.get_age)

stu.__dict__.pop('get_age')
print(stu.get_age)
print(stu.get_age)
