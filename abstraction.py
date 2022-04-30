from abc import ABCMeta, abstractclassmethod

class Base(metaclass=ABCMeta):

    @abstractclassmethod
    def some_method(self):
        ...
    
class CLS(Base):
    def some_method(self):
        print("asdsa")

c = CLS()
# b = Base()
