var1 = "안녕 파이썬"
print(var1)    # 이건 주석
"""
여러
줄 주석
"""
var1 = 5;
var1 = 10
var1 = 5.6
print(var1)
var2 = var1
print(var1, var2)
var3 = 7
print(var1, var2, var3)
print(id(var1), id(var2), id(var3))
Var3 = 8
print(var3, Var3)

a = 5
b = a
c = 5
print(a, b, c)
print(a is b, a == b) # iS: 주소 비교 연산, ==: 값 비교 연산
print(b is c, b == c)
aa = [5] #대괄호 []는 그룹임.
bb = [5]
print(aa, bb)
print(aa is bb, aa == bb) #결과는 false, true임. 왜냐? 주소는 aa랑 bb랑 다르지만 값은 같기 때문에 is는 틀렸고, ==는 맞음

print('------') #print("------")
import keyword  #keyword: 키워드 목록 확인용 모듈 읽기/자주쓰는 건 import 안 해도 되지만, 잘 사용하지 않는 keyword같은 건 import로 끌어올려줘야함
print('예약어 목록:', keyword.kwlist) #이미 있는 모듈 목록임. 이걸 임의 이름으로 쓰면 안됨. ex) if.. 등등

print('type(자료형) 확인')
kbs = 9
print(isinstance(kbs, int))
print(isinstance(kbs, float))
print(5, type(5))  #5 <class 'int'>
print(5.3, type(5.3))  
print(3 + 4j, type(3+4j))  
print(True, type(True))  
print('good', type('good'))  #스트링
print((1,), type((1,)))  #그룹형
print([1], type([1]))  #그룹형
print({1}, type({1}))  #Set, 그룹형
print({'k':1}, type({'k':1}))  #딕셔너리, 그룹형