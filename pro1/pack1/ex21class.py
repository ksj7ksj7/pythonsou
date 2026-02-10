kor = 100  #모듈의 전역변수

def abc():
    kor = 0  # 함수 내의 지역 변수
    print('모듈의 멤버 함수')

class My:
    kor = 80  # My 멤버 변수(필드)

    def abc(self):
        print('My 멤버 메소드')

    def show(self):
        #kor = 77  #메소드 내의 지역 변수    /   이 멤버 변수 없는데, my.show()하면 클래스 내의 kor =80 반영하는 게 아니라 모듈의 전역변수인 kor= 100을 반영함
        print(kor)
        print(self.kor)   #self 붙이면 클래스의 멤버 변수 씀
        self.abc()   #앞에 self를 찍어줬으니까 클래스의 abc 메소드를 사용
        abc()   #앞에 self 없으니까 클래스가 아닌 모듈의 함수를 사용

my= My()
my.show()
print('-----')
print(My.kor)
tom=My()
print(tom.kor)
tom.kor=88
print(tom.kor)

oscar = My() #oscar라는 새 객체 생성
print(oscar.kor)