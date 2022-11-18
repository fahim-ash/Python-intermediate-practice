# abstractmehtod for a method
# cant instantitate with abstractproperty
# abstract class must have one abstarct method
# we can use abstractproperty also
import abc
from abc import ABC,abstractmethod

class Grandfather(ABC):
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    @abstractmethod # @abstractproperty needs @property to modify
    def full_name(self):
        print (self.firstname+self.lastname)
        
class Son(Grandfather):

    def full_name(self):
        return self.firstname+self.lastname


a=Son("mr","kashem")
print(a.full_name())