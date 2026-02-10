#Closure: Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
#내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a,b):
    c=a*b
    return c
print(funcTimes(2,3))

kbs = funcTimes(2,3)   #2,3의 funcTimes 실행 결과를 kbs에 치환 됨.
print(kbs)
kbs = funcTimes   #주소가 kbs에 치환 됨. ( )가 있냐 없냐에 따라서 실행결과가 치환될수도, 주소가 치환될수도 있음
print(kbs)
print(kbs(2,3))
print(funcTimes(2,3))
print(id(kbs), id(funcTimes))
mbc=sbs=kbs
del funcTimes   #funcTimes의 변수 삭제
#print(funcTimes(2,3))   #del funcTimes으로 삭제했으니까 에러남
print(mbc(2,3))  #mbc, sbs, kbs는 여전히 funcTimes의 주소를 가지고 있으니까 참조할 수 있음. 에러 안나고 잘 됨.

print('\n----클로저를 사용하지 않은 경우----')
def out():
    count = 0
    def inn():
        nonlocal count  #out()에서 사용된 count를 가져온거임.(선언)
        count +=1
        return count
    print(inn())

#print(count)
out()
out()


print('\n----클로저를 사용한 경우----')
def outer():
    count = 0
    def inner():
        nonlocal count  #out()에서 사용된 count를 가져온거임.(선언)
        count +=1
        return count
    return inner   #이게 클로저. 내부함수의 주소를 반환. return inner()가 아니고 return inner임 값을 가져오는 게 아니라 주소를 가져오는 것

var1 = outer()   #내부함수의 주소를 변수에 저장
print('var1 주소:', var1)
print(var1())
print(var1())
myvar = var1()
print(myvar)
print()
var2=outer()   #새로운 객체(inner)생성
print(var2())
print(var2())

print(var1,var2)

print('수량 * 단가 * 세금 한 결과를 출력하는 함수 작성')
def outer2(tax):   #tax는 지역 변수
    def inner2(su, dan):
        amount = su * dan *tax
        return amount
    return inner2    #이게 클로저임

#1분기에는 su * dan에 대한 tax는 0.1 부과
q1 = outer2(0.1)  #inner2의 주소 기억
result1 =q1(5,50000)
print('result1:',result1)

result2 =q1(2,50000)
print('result2:',result2)

print()
#2분기에는 su * dan에 대한 tax는 0.05 부과
q2 = outer2(0.05)  #inner2의 주소 기억
result3 =q2(5,50000)
print('result3:',result3)
result4 =q2(2,10000)
print('result4:',result4)

print('\n일급함수: 함수 안의 함수, 인자로 함수 전달, 반환값이 함수')
def func1(a, b):
    return a+b

func2 = func1
print(func1(3,4))
print(func2(3,4))
print()
def func3(fu):    #인자로 함수 전달
    def func4():  #함수안에 함수
        print('나는 내부함수야~~')
    func4()
    return fu   #반환값이 함수

mbc = func3(func1)
print(mbc(3,4))

print('\n축약함수(Lambda function):이름이 없는 한줄짜리 함수')
#형식: lambda 매개변수들,,:반환식 <=return 없이 결과 반환
def hapFunc(x, y):
    return x+y
print(hapFunc(1,2))
#람다로 표현
print((lambda x, y:x + y)(1,2))

gg=lambda x, y:x+y
print(gg(1,2))

kbs = lambda a, su=10: a+su
print(kbs(5))
print(kbs(5,6))

sbs =lambda a, *tu,  **di:print(a,tu,di)
sbs(1,2,3,var1=4, var2=5)   #결과: 1 (2, 3) {'var1': 4, 'var2': 5}

li = [lambda a, b:a+b, lambda a,b:a*b]
print(li[0](3,4))   #결과: 7
print(li[1](3,4))   #결과: 12

print('\n 다른 함수에서 람다 사용하기')
#filter함수의 기본 형태는 filter(function, iteration) 형태임. 근데 function 부분에 def~ 하면서 쓸 수 없기 때문에 이 때 lambda 함수 쓰는 것.
#filter(함수, 반복가능한객체)
print(list(filter(lambda a:a<5, range(10)))) #0부터 10미만중에 5 미만인 숫자를 filter 걸러줘서 list해줘
print(list(filter(lambda a:a%2, range(10))))  #파이썬에서 0이면 False고 1이면 True임 그렇기 때문에 %2했을 때 나머지 1 인 애들만 걸러짐 왜냐? 나머지 1 =True니까 True만 나옴

# 문) filter 이용해 1~100사이의 정수 중 5의 배수이거나 7의 배수만 출력
print(list(filter(lambda a:a%5 ==0 or a%7 ==0 , range(100))))

