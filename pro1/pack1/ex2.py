#연산자
v1 = 3  #치환 연산자
v1 = v2= v3= 5
print(v1, v2, v3)
print('출력1', end =',') #다음 내용 줄바꿈 안 시키고 싶을 때 end =',' 사용해서 옆에 나란히 출력되도록 함
print('출력2')
print('출력3')

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5  #v1 = (1,2,3,4,5) 라는 뜻임.
v1=[1,2,3,4,5]
*v1, v2 =[1,2,3,4,5]  # v1, v2 =[1,2,3,4,5]는 변수가 두개로 많아서 오류 뜸, *를 앞에 넣으면 '제일 끝 값만 끝 변수부터 하나씩 가져, 나머지는 앞 변수가 가진다'는 뜻
print(v1, '',v2)


print()
print(format(1.5678, '10.3f'))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))  #{0}, {1}은 대응 순서임. 한국인이 0번째, 33이 1번째
print('이름은 {}, 나이는 {}'.format('신선해', 33))  #대응 순서 없으니까 그냥 차례대로
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
abc=123
print(f"abc의 값은 {abc}임")  #" "는 그냥 문자열인데 안에 {}있으니까 거기에 abc 데이터가 적용됨
print('\n\n본격적 연산 --------')   #\n, \b, \t .. 는 라인 스킵. \n은 다음줄로 넘어감 \b는 위 줄로 back함 \t은 tab하는 것처럼 떨어짐
print(5 + 3 , 5-3, 5*3, 5/3, 5//3, 5%3, 3**3)
print(divmod(5,3), ' ', 5%3)
result = 3+4*5+(2+3)/2
print(result) 

print(5>3,5==3, 5!=3)
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))
print(True or False and False)
print(True and False or False)   #and가 or보다 우선순위 높음

print(4+5)  #산술연산
print('4'+'5')  #문자열 더하기
print('한'+'국'+'만세')
print('한국'*5)
print('누적')
a=10
a=a+1
a +=1  #-=, *=, /=
print(f"a는 {a}")
#print(a++)  #++, --: 증감 연산자 X, 파이썬엔 증감연산자 기능 없음
print(--a)
print(-a)
print(a*-1)

#print(('1'+'1')+1)  #TypeError임
print(int('1'+'1')+1)  #12
print(float('1'+'1')+1)  #12.0
#print((1+1)+'1')  #TypeError
print(str(1+1)+'1')  #21 str(숫자) -. 문자화
print('boolean 처리: ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'),bool([12]))  #다 True 나옴
print(bool(0), bool(0.0), bool(' '),bool([])), bool(None)  #다 False 나옴 -> 데이터 있으면 True 나오고, 데이터 없으면 False나옴

print('aa\tbb')
print('aa\nbb')
print(r'aa\tbb')  #r 쓰면 이스케이프 문자가 순수 데이터로 나타남
print(r'aa\nbb')

