# 상속: 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
# 코드 재사용
# 확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공통개념은 부모 클래스, 구체적 내용은 자식 클래스에서 구현
# 다형성 구사 - 메소드 오버라이딩
# 강결합 - 상속 / 약결합 - 포함

class Animal:   # 동물들이 가져야할 공통속성과 행위 선언
    age = 1
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물')

class Dog(Animal):   #상속 하고 싶으면 class 00뒤에 ()하고 ()안에 상속받고자 하는 것 넣기  / Animal: 부모, 조상, super, parent. / Dog: 자식, 자손, 파생, sub, child
    def __init__(self):
        print('Dog 생성자')

    def my(self):
        print('댕댕이라고 해요')

dog1 = Dog()  #dog1은 인스턴스 베리어블이라고 함
dog1.my()
dog1.move()  #dog1에서 move를 뒤져보고 없으면 상속 관계인 Animal로 가서 move를 찾아보는 거임
print('age: ', dog1.age)
print()
dog2 = Dog()
dog2.my()
dog2.move()
