#반복문 for
#for i in [1,2,3,4,5]:   #[  ]는 묶음형 자료
#    print(i, end ='')   #묶음형 자료에 자료가 있을 동안 for문 반복함

#for i in (1,2,3,4,5):
#    print(i, end = '')

#for i in {1,2,3,4,5}:
#    print(i, end = '')

print('분산/표준편차 ----')


#numbers = [1,3,5,7,9]  #합은 25, 평균은 5
numbers = [3,4,5,6,7]  #합은 25, 평균은 5
#numbers = [-3,4,5,7,12]  #합은 25, 평균은 5
tot=0
for a in numbers:
    tot += a
print(f"합은 {tot}, 평균은 {tot / len(numbers)}")  #len(numbers)는 전체 개수
avg = tot / len(numbers)
#편차의 합
hap=0
for i in numbers:
    hap += (i-avg)**2
print(f'편차 제곱의 합{hap}')
vari=hap/len(numbers)
print(f'분산은 {vari}')
print(f'표준편차는 {vari**0.5}')

print()
colors=['r','g','b']   #r, g, b 데이터가 차례차례 v에 들어가서 순서대로 찍음 대신 {  }는 set이라서 순서가 없음
for v in colors:
    print(v, end ='')

print('iter(): 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator =iter(colors)
for v in iterator:
    print(v, end = ',')

print()
for idx, d in enumerate(colors):   #enumerate: 인덱스와 값을 반환해줌  (0번쨰 r, 1번째 g, 2번째 b 등.. 인덱스랑 같이 값을 매겨줌)
    print(idx, '', d)

print('\n사전형----')
datas = {'python':'만능언어','java':'웹용언어', 'mariadb':'RDBMS'}
for i in datas.items():   #item은  tuple 형태로 t와 value 연관지어줌
#    print(i)
    print(i[0],'~~', i[0])

for k, v in datas.items():
    print(k, '--', v)

for k in datas.keys():
    print(k, end='')

for val in datas.values():
    print(val, end ='')

print('다중 for ------')  #for 안에 for, for 안에 while 등..
for n in [2,3]:
    print('--{}단 --'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n,i, n*i))

print ('continue, break----')
nums=[1,2,3,4,5]
for i in nums:
    if i ==2: continue
    if i ==4: break
    print(i, end=' ')
else:
    print('정상종료')


print('\n정규표현식 + for')
str = """
이 보고서는 미국 AI 연구개발 기업 앤트로픽(Anthropic)이 발표한 앤트로픽 경제지표를 활용해 글로벌 AI 사용 실태와 한국의 현황을 분석한 내용을 담았다.
앤트로픽 경제지표는 앤트로픽이 자사 AI 서비스 클로드(Claude) 사용 데이터를 기반으로 ▲업무 복잡성 ▲인간 및 AI 기술 수준 ▲사용 목적 ▲AI 업무위임도 ▲업무 성공률 등 다섯 가지 차원에서 분석한 지표다.
보고서에 따르면, 우리나라의 AI 사용 비중은 3.06%(3만618건)로 동아시아 4개국(한국·일본·대만·싱가포르) 중 2위를 기록했다.
"""
import re #re는 정규표현식 모듈
str2= re.sub(r'[^가-힣\s]','',str)  #한글과 공백 이외의 문자는 공백처리 ,\s는 공백을 의미, []속의 ^는 부정(^뒤가 아닌 사람들)
print(str2)
str3 = str2.split(' ')  #공백을 기준으로 문자열 분리
print(str3)

cou ={}  #{}는 set 아니면 dic임
for i in str3:
    if i in cou:
        cou[i]+= 1   #같은 단어가 있으면 누적
    else:
        cou[i] = 1  #최초 단어인 경우는 '단어' : 1
print(cou)

print('정규표현식 좀 더 연습')
for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234']:
    if re.match(r'^\d{3}-\d{4}$', test_ss):  ## \d 숫자를 의미, ()안의 r은 처음을 의미 () 안의 $는 끝을 의미 -> ^\d{3}-\d{4}$는 \d로 시작하고 \d로 끝나야한다. 즉 숫자로 시작하고 숫자로 끝
        print(test_ss, '전화번호 맞아요')
    else:
        print(test_ss, '전화번호 아니야')

print('comprehension: 반복문 + 조건문 + 값 생성을 한 줄로 표현')
a =[1,2,3,4,5,6,7,8,9,10]
li=[]
for i in a:
    if i%2 ==0:
        li.append(i)
print(li)

print(list(i for i in a if i %2 ==0))   #위의 한바가지 코드랑 같은 결과 나옴

datas = [1,2,'a', True, 3.0]
li2 = [i*i for i in datas if type(i)== int]
print (li2)

datas = {1,2,2, 1,1,2,'a', True, 3.0}  # 위의 113줄이랑 결과 똑같음. 왜냐? 중복 값은 배제하기 때문에 똑같이 나옴
li2 = [i*i for i in datas if type(i)== int]
print (li2)

id_name={1:'tom', 2:'oscar'}
name_id={val:key for key, val in id_name.items()}  #결과:{'tom': 1, 'oscar': 2}
print(name_id)
print()
print([1,2,3])   # 결과: [1, 2, 3]
print(*[1,2,3]) # *: unpack, 결과:1, 2, 3
aa = [(1,2), (3,4),(5,6)]
for a, b in aa:
    print(a+b)


print(*[a+b for a, b in aa],sep='\n')

print('\n수열생성: range')
print(list(range(1,6))) #결과: [1, 2, 3, 4, 5] 1부터 6미만까지 list로 출력.
print(tuple(range(1,6,2)))  #결과: (1, 3, 5)   [start, end, step증가치]
print(list(range(-10, -100, -20)))
print(set(range(1,6)))  #결과: {1, 2, 3, 4, 5}
print()
for i in range(6):  ##값 안주면 임의로 항상 0부터임. 즉 0부터 6미만까지. 결과: 0 1 2 3 4 5
    print(i, end = ' ')

for _ in range(6):  #i 안 쓰고 싶고, 반복만 하고 싶다면 그냥 언더바 _ 만 쓰기
    print('반복')

tot = 0
for i in range(1,11):
    tot += i
print('tot:', tot)
print('tot:',sum(range(1,11)))  #sum(): 내장함수

for i in range(1,10):
    print(f'2*{i}={2*i}')

#문제1: 2~9 구구단 출력 (단은 행 단위 출력)
for i in range(2,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}', end =' ')

    print
#문2: 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(6):
    n1 = i+1
    for j in range(6):
        n2 =j+1
        n = n1+n2
        if n%4 ==0:
            print(n1, n2)
print()

for i in range(1, 7,1):
    for j in range(1,7,1):
        su = i+j
        if su%4==0: print(i,j)

print('\nend')
