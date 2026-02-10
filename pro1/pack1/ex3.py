#기본 자료형: int, float, bool, complex
#묶음 자료형:  str,list,tuple, set, dict

#1) str: 문자열 묶음 자료형. 순서는 있음. 하지만 수정 불가
s= 'sequence'
print(s,id(s))
print('길이:',len(s))  #s의 단어 알파벳 길이
print(s[0],s[2])  #sequence 단어에서의 0번째 알파벳이랑 2번째 알파벳이 뭔지 (s(0번째)e(1번째) 등등 0번째부터 시작)
print('길이:', s.find('e'),s.find('e',3),s.rfind('e'))  #문자열 관련함

#인덱싱 / 슬라이싱
print(s[5])   #인덱싱 - 변수명[순서],순서를 인덱스라고 함. index는 0번째부터 카운팅하는것.
print(s[2:5])  #슬라이싱 - 2번째부터 (5-1)번째까지 말하세요. [n이상:m미만]
print(s[:], ' ', s[0:len(s)])  #0부터 전체 길이까지 말하세요.
print(s[0:7:2])  #0번째부터 7번째까지 2씩 증가해라
print(s[-1])  #-1번째는 맨뒤에서부터 카운트하는 것. -2는 맨뒤에서 두번째
print(s[-1], ' ', s[-4:-1:1])
print(s, id(s))
s='sequenc'  #s값 수정된 게 아님. 변경이라고 생각해야함
print(s, id(s))
s='bequence'
print(s,id(s))

print('---'*10)
#2) List: 다양한 종류의 자료 묶음형. 순서O, 수정O, 중복O
a=[1,2,3]
print(a, a[0],a[0:3])
b = [10,a,10,20.5,True, '문자열']  #다양한 type 다 들어갈 수 있음
print(b, ' ', b[1], ' ',b[1][0])
print()
family =['엄마','아빠','나','여동생']
print(id(family))
family.append('남동생')  #family에 남동생 추가하기 위해서 append 사용. 결과는 ['엄마', '아빠', '나', '여동생', '남동생']
print(id(family))
family.remove('나')  #family에 나 빼기 위해서 remove 사용
family.insert(0,'할머니')  #family에 할머니를 "삽입"하는 것임. 0번째 지점에 삽입
family.extend(['삼촌', '고모', '조카'])  #family에 이 그룹 추가
family += ['이모']  #+= 사용해서도 이모 추가 가능
print(family)
print(family.index('아빠'))  #아빠가 몇번째에 있는지 순서를 알려줌
print('엄마' in family, '나' in family) #family에 엄마가 있는지, family에 내가 있는지 True와 False로 출력

family.remove('아빠')  #값에 의한 삭제, '아빠'를 삭제하기 위해 값을 기재
del family[2]  #순서에 의한 삭제,  '여동생'을 삭제하기 위해 몇번째 순서인지를 기재
print(family)

print()
kbs = ['123','34','234']
kbs.sort()  #문자열 정렬
print(kbs)
mbc = [123,34,234]
#mbc.sort()  #숫자 정렬 (ascending sort, 오름)
mbc.sort(reverse=True)  #숫자 정렬 (ascending sort, 내림)
print(mbc)
sbs=[123,34,234]
ytn=sorted(sbs)  # sorted는 원본은 그대로, sort는 원본을 바꿈
print(sbs)
print(ytn)
print()
name = ['tom','james','oscar']
name2 = name
print(name, id(name))
print(name2, id(name))

import copy
name3 = copy.deepcopy(name)  #새로운 객체에게 값을 치환하는 것, 즉 tom, james, oscar가 어딘가에 또 있다는것. 그래서 id해서 주소 찾으면 주소가 다름
print(name3, id(name3))

name[0]= '길동'
print(name)
print(name2)
print(name3)  #이렇게 되면 name과 name2 는 영향이 미쳐서 0번째가 길동으로 바뀌는데, copy했던 name3는 주소가 다르기 때문에 영향 없이 길동 들어오지 않음

print('---'*10)
#3) tuple: 리스트와 유사. 읽기 전용-수정 불가능 / 담을 데이터를 수정 못하게 고정하고 싶으면 tuple 사용. 수정하고 싶어질 것 같으면 list 사용
t=(1,2,3,4)   #얘는 tuple
t=1,2,3,4  #위와 동일
print(t, type(t))
k=(1)   #얘는 tuple 아님. type이 int 정수형으로 나옴
k=(1,)  #숫자가 1개 일 때, tuple 하고 싶으면 이렇게 (1,) 라고 써야함
print(k, type(k))
print(t[0], ' ', t[0:2])
#t[0]=77  #이렇게 하면 오류 뜸. 왜냐? tuple은 수정 불가니까. 위에서 정의 내렸으면 다시 다른 값으로 정의 내릴 수 없음. 

imsi = list(t)  #만약 tuple 수정하고 싶을 때, list로 바꿔
imsi[0]=77    #그리고 수정해
t= tuple(imsi)  #그리고 다시 tuple 시키면 끝!
print(t)


print('---'*10)
#4) set: 순서가 없음, 중복X, 수정은 가능
ss = {1,2,1,3}  #1,2,1,3에서 1이 중복됨. 이 중복되는 1을 제거함 결과. {1,2,3}
print(ss)
ss2={3,4}
print(ss.union(ss2))  #ss와 ss2의 합집합. 즉 둘의 합집합에서 중복되는 것 제외함
print(ss.intersection(ss2))  #ss와 ss2의 교집합. 즉 둘의 합집합에서 중복되는 것 제외함
print(ss - ss2, ss|ss2, ss&ss2) #차집합, 합집합, 교집합에서 중복되는 것 제외함
#print(ss[0])  #TypeError: 'set' object is not subscriptable 라는 오류 뜸. 왜? ss는 순서가 없으니까 0번째가 없음

ss.update({6,7})  #ss값 수정한 것임 6,7을 추가
print(ss)
ss. discard(7)  #값 삭제
ss. discard(7)  #값 삭제, discard는 있으면 지우고 없으면 스킵함
ss. remove(6)  #값 삭제, remove는 있으면 지우고 없으면 오류뜸
print(ss)

li=['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi =set(li)  #중복 빼기 위해서 imsi 사용해서 set으로 중복 제외
li=list(imsi)  #그 후에 list로 둬서 수정 가능하게 함
print(li)

print('---'*10)
#5) dict: 사전 자료형 {'키':값} 형태
# 방법1
mydic = dict(k1=1, k2='ok',k3=123.4)   #결과: {'k1': 1, 'k2': 'ok', 'k3': 123.4}
print(mydic,type(mydic))


#방법2
dic={'파이썬':'뱀','자바':'커피', '인사':'안녕'}  #몇번째 찾아줘로 못할 때, 키를 사용하는 것임. 마치 책 몇쪽에 있는 뭐뭐 찾아
print(dic)  #키를 가지고 값을 찾는것임
print(len(dic))
print(dic['자바'])  #결과: 커피
ff=dic.get('자바')  #결과: 커피
print(ff)
#print(dic['커피'])  # 얘는 그래서 오류뜸
#print(dic[0])  #인덱싱X

dic['금요일']='와우'  #결과: {'파이썬': '뱀', '자바': '커피', '인사': '안녕', '금요일': '와우'} / 데이터가 들어감.
print(dic)
del dic['인사'] #결과: {'파이썬': '뱀', '자바': '커피', '금요일': '와우'}
print(dic)
print(dic.keys())  #결과: dict_keys(['파이썬', '자바', '금요일'])
print(dic.values()) #결과: dict_values(['뱀', '커피', '와우'])