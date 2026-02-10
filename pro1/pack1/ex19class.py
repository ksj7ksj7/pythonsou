# oop(객체 중심 프로그래밍 가능): 새로운 타입 생성, 포함, 상속, 다형성 등을 구사
# class(설계도)로 인스턴스 해서 객체를 생성(별도의 이름 공간을 가짐)
# 객체는 멤버필드(변수)와 메소드로 구성됨
# 자바와 달리 접근 지정자가 없다. 메소드 오버로딩 없다.
# 모듈의 멤버: 변수, 명령문, 함수, 모듈, 클래스
# 설계도인 클래스로 만들어낸 객체는 속성과 행동을 가지고 있음. 여기서 속성은 멤버필드, 행동은 메소드임.

print('뭔가를 하다가 객체 만들기')

class TestClass:   #클래스는 설계도. 객체를 만들 수 있음. 새로운 Type을 만들 수 있음
    aa = 1  # 멤버필드(변수). 현재 클래스 내에서 전역

    def __init__(self):  # 특별한 메소드. 메소드는반드시 argument 갖고 있어야 함. 그 argument는 여기서 self임. 메소드란 클래스 안에서의 함수를 뜻하는것임. 모든 클래스의 생성자는 __init__임
        print('생성자: 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')   #맨날 꼭 써야하는 건 아니고, 초기화 해야할 때는 꼭 써줘야 함.

    def __del__(self): #self가 객체의 주소를 넘겨받음
        print('소멸자: 프로그램 종료시 자동실행. 마무리 작업')

    def printMsg(self):  # 일반 메소드. 클래스 내의 함수는 메소드라고 부름.
        name = '한국인'   # 지역 변수:printMsg에서만 유효
        print(name)

print(TestClass)   #결과: <class '__main__.TestClass'>   -> 타입이 TestClass라는 뜻임.
test = TestClass()    # 객체변수 test를 만듦. TestClass() 같이 () 붙여주면 객체를 생성했다는 뜻임. 그 생성된 객체의 주소를 test가 받게 됨. 그래서 TestClass가 실행 됨.
#test.   #객체변수명. 이렇게 하면 객체변수에 주소가 담겨있기 때문에 멤버 'aa'랑 'printMsg'가 뜨게 됨.
print("test객체의 멤버 aa: ", test.aa)

# method call
test.printMsg()   # 1. Bound Method call  #객체의 이름으로 멤버 부르는 법
TestClass.printMsg(test)   # 2. Unbound Method call   -> argument를 줘야함. 즉 test를 써줘야함. 객체변수를 넣어줘야함  #클래스 이름으로 멤버 부르는 법
print(type(1))
print(type(1.0))
print(type(test))
print(id(test)) # 결과: 1742394913328
print(id(TestClass))  # 결과: 1742398168784
test2 = TestClass() # 만들어도 결과는 print(id(TestClass)) 과 다른 주소가 나옴. 왜냐하면 객체가 계속 새로 만들어지기 때문에 설계도인 print(id(TestClass))와는 다른 주소가 계속 새로 찍힘
