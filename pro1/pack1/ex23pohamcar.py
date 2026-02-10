#여러 개의 부품 객체를 조립해 완성차 생성
#클래스의 포함 관계 사용 (자원의 재활용)
#다른 클래스(객체)를 마치 자신의 멤버처럼 선언하고 사용

#import ex23pohamhandle
from ex23pohamhandle import PohamHandle

class PohamCar:
    turnShowMessage = "정지"

    def __init__(self,ownerName):
        #ownerName = ownerName
        self.ownerName = ownerName
        self.handle = PohamHandle()  #클래스의 포함관계

    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)  #handle의 rightTurn을 불러야하니까 self.handle.rightTurn임 -> 클래스의 포함관계. 클래스 속 메소드 등등..?
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q ==0:
            self.turnShowMessage = 0

if __name__ =='__main__':
    tom=PohamCar('미스터 톰')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은'+tom.turnShowMessage + ' ' + str(tom.handle.quantity))

    john=PohamCar('미스터 존')
    john.turnHandle(-20)
    print(john.ownerName + '의 회전량은'+john.turnShowMessage + ' ' + str(john.handle.quantity))

    # john.turnHandle(0)
    # print(john.ownerName + '의 회전량은'+ john.turnShowMessage + ' 0')
