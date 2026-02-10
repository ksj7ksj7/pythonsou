class Car:   #자동차 설계도.
    handle = 1
    speed = 0

    def __init__(self, name, speed):   #(self, name, speed)라고 쓴 곳은 모두 지역변수라는 의미임
        self.name = name  # 현재 객체의 name에게 name(지역변수) 인자값 치환
        self.speed = speed  #speed는 생성된 객체, self. speed 는새로 만들어진 객체

    def showData(self):
        km = "킬로미터"
        msg = "속도: " + str(self.speed) + km   #speed를 문자열로 해서 리턴하고 있음
        return msg
    
    def printHandle(self):  #메소드는 반드시 self를 가지고 있어야 함
        return self.handle   #클래스 내 멤버 부를 때는 꼭 .을 찍어줘야 함 self.handle처럼 

print(Car.handle)  #원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10 )  #생성자 호출 후 객체 생성(인스턴스화 했다는 것을 의미) / 얘는 def __init__(self, name, speed)에게 감. name은 tom 주소를 갖고, speed는 10 주소 갖고 self는 car1 주소를 갖게 됨
#Car이라는 원형클래스로 인해서 car1이라는 오브젝이 만들어짐. car1은 객체의 주소를 기억하고 있는 것임. self는 car1의 주소를 기억하게 됨. 그래서 위의 줄에 self에 해당하는 게 ()안에 없었던 것
#원형클래스Car에서 멤버필드는 handle=1,speed=0이었는데, car1 오브젝에서는 멤버필드가 'name=tom, speed=10'인 것.
print('car1 객체 주소:', car1)
print('car1:', car1.name, '  ', car1.speed, car1.handle)
car1.color = '파랑'  #원래는 color 멤버가 없었는데 car1.color로 car1에 color 멤버를 추가한 것임. 00.XX는 00속의 XX를 의미   #각각의 객체마다 고유의 멤버를 추가 할 수 있음 대신 그 객체에서만 가질 수 있음
print('car1.color:',car1.color)


car2 =Car('john',20)  #생성자 호출 후 객체 생성(인스턴스화)
print('car2 객체 주소:', car2)
print('car2: ', car2.name, car2.speed, car2.handle)

print(Car, car1, car2)
print(id(Car), id(car1), id(car2))
print(car1.__dict__)   # 이건 car1이라는 오브젝(객체)의 멤버를 확인 할 수있음 / 결과:{'name': 'tom', 'speed': 10, 'color': '파랑'}
print(car2.__dict__)   # 결과: {'name': 'john', 'speed': 20}

print('-------메소드---------')
print('car1 speed:', car1.showData())  # 결과: car1 speed: 속도: 10킬로미터  /  car1 객체에는 메소드가 현재 없음. 그래서 Car 클래스로 올라가서 showData 써야함. car1의 주소를 showData(self)의 self에게 넘겨줌. 그래서 위의 showData의 str(self.speed) 부분 보면 Car의 speed멤버를 가져오는 게 아닌 car1의 speed를 가져올 수 있음..
print('car2 speed:', car2.showData())
car1.speed = 80
car2.speed = 110
print('car1 speed:', car1.showData())
print('car2 speed:', car2.showData())

print('car1 handle:', car1.printHandle())   #printHandle(self)의 self에 car1의 주소를 가져다 주고, printHandle메소드에서 return self.handle로 인해서 car1의 멤버중에 handle이 있나 찾아보는데, 없으니까 클래스의 handle 멤버를 찾아보고 있으니까 쓰는 것.
print('car2 handle:', car2.printHandle())

#car라는 클래스 안에 handle, speed, showData가 있음. 이걸 원형클래스라고 함. 원형클래스 안에 있는 멤버들을 prototype이라고 함.
#클래스로 인해서 만들어진 것들을 오브젝트라고 함. 오브젝은 클래스를 참조함 그래서 멤버필드가 오브젝에게 공유자원임 공유 자원이기 때문에 print(Car.handle)이라고 하면 Car 클래스의 handle이라는 멤버를 가져올 수 있는 거임 (공유중이니까)

#handle, speep는 멤버필드, showData는 메소드 필드에 있음.
#멤버들 앞에 +나 -를 줄 수 있음. +는 퍼블릭(누구나 갖다 쓸 수 있음), -는 프라이빗(나만 쓸 수 있음)
#UML 다이어그램, 시퀀스 다이어그램, Use Case 다이어그램 꼭 참조하기