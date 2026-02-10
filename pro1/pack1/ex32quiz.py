from abc import *

class Employee(metaclass=ABCMeta):  #추상클래스
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    @abstractmethod
    def pay(self):  #추상메소드
        pass

    @abstractmethod
    def pata_print(self):  #추상메소드
        pass
    def irumnai_print(self):   #이름, 나이 출력용
        print('이름:'+self.irum+ ',나이:'+str(self.nai), end = ' ')

class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu =ilsu
        self.ildang = ildang

    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self):
        super().irumnai_print()
        print(', 월급: 'str(self.pay()))

