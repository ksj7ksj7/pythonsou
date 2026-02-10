#매개변수 유형
#위치 매개변수: 인수와 순서대로 대응
#기본값 매개변수: 매개변수에 입력값이 없으면 기본값 사용
#키워드 매개변수: 실인수와 가인수 간 동일 이름으로 대응
#가변 매개변수: 인수의 갯수가 동적인 경우

def showGugu(start,end=5):  #여기 end에 end=5라고 작성하면 그게 end의 기본값임
    for dan in range(start, end+1,1):
        print(str(dan)+ '단 출력')
        for i in range(1,10):
            print(str(dan)+'*'+ str(i)+ '='+str(dan*i), end= ' ')
            print()
showGugu(2,3)
print()
showGugu(2)  #함수 정의에 end=5라고 기본값주면 매개변수에 입력값이 없으니까 showGugu(2,5)결과로 나옴
print()
showGugu(start=7,end=9)
print()
showGugu(start=9,end=7)
print()
showGugu(7,end=9)   #얘는 잘나옴
print()
#showGugu(start=7,9) #얘는 오류남
#showGugu(end=9,7) #얘는 오류남

print('가변 매개변수-------')
def func1(*ar):  #ar 앞에 * 없을 땐 func1('김밥','비빔밥', '볶음밥') 실행하면 오류나게 됨. 왜냐면 ar은 한개인데 김밥, 비빔밥, 볶음밥 세개가 들어가서 오류. 그러나 * 붙이면 가능해짐
    print(ar)    # *: 여러 개의 인자를 tuple로 묶어서 받겠다는 의미
    for i in ar:
        print('밥:'+i)

func1('김밥','비빔밥', '볶음밥')
func1('김밥','비빔밥', '볶음밥', '공기밥')
func1('김밥')  #위에 *붙여서 *ar로 줬기 때문에 하나만 주면 안 됨. 이건 func1('김밥',)이 모양으로 전달되는 것임.

print()
def func2(a, *ar):
    print(a)
    print(ar)

func2('김밥', '비빔밥')
func2('김밥','비빔밥','볶음밥','공기밥')

print()
def func3(w, h, **other):   # **: dict를 받겠다는 의미임. func3(80,180,irum='신기루',nai=23)처럼 두개 가능. 그런데, func3(80,180,{irum='신기루',nai=23})는 안됨.type 에러임
    print(f'몸무게:{w}, 키: {h}')
    print(f'기타: {other}')

func3(80,180,irum='신기루',nai=23)

print()
def func4(a,b,*c, **d):
    print(a,b)
    print(c)
    print(d)

func4(1,2)  #결과:1 2  ()  {}
func4(1,2,3,4,5)   #결과:1 2  (3, 4, 5)  {}
func4(1,2,3,4,5,kbs=9, mbc=11)   #결과: 1 2   (3, 4, 5)   {'kbs': 9, 'mbc': 11}

print()
#type hint: 함수의 인자와 반환값에 type을 적어 가독성 향상
def typeFunc(num:int, data:list[str]) -> dict[str, int]:   #num:int, data:list[str]가 type hint임. num은 int형 넣을거고, data는 str의 list형 넣을거다라는 뜻, -> dict[str, int]도 순전히 가독성을 위한 것. 기능적인 역할 X
    print(num)
    print(data)
    result={}
    for idx, item in enumerate(data, start=1):   #enumerate: 묶음형 자료에서 인덱스랑 하나씩 빼줌
        print(f'idx:{idx}, item:{item}')
        result[item]=idx
    return result

rdata = typeFunc(1, ['일','이','삼'])
print(rdata)

print()
rdata = typeFunc("한개",[10,20,30])
print(rdata)

