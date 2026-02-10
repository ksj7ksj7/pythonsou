a=1
while a <=5:
    print(a, end = ' ')
    a = a + 1
else:
    print('수행성공')


print()
i=1
while i <= 3:
    j=1
    while j <=4:        
        print('i='+str(i)+'/j='+str(j))
        j= j+1
    i=i+1

print('1~100 사이의 정수 중 3의 배수의 합 ---')
su = 1; hap = 0
while su <= 100:
#    print(su)
#    su += 1
    if su% 3 ==0:
        #print(su)
        hap += su   #hap =hap +su
    su += 1
print('합은', hap)


print()
colors = ["빨강", "파랑", "노랑"]
#num =0
#print(colors[num])  # index valuable
#print(colors[1])
#print(colors[2])
num = 0
#while num<3: #얘는 색깔이 몇개인지 알아야 함
while num < len(colors):   #행의 전체 길이까지를 고려하는 것이기 때문에 색깔 행에 색깔을 계속 추가해도 이 코드는 그대로 둬도 됨
    print(colors[num])
    num += 1


print('\n별 찍기-----')
i = 1
while i <= 10:
    j=1
    msg=''
    while j <= i:
        msg +="*"
        j += 1
    print(msg)
    i += 1

"""

print('if 블럭 내 while 블럭 사용 ---')
#폭탄은 스위치를 누르고 5초 뒤에 폭발함. 이 관련 기술 구현
import time
sw = input('폭탄 스위치를 누를까요? [y/n]')
if sw == 'Y' or sw == 'y':
    count = 5
    while 1 <= count:
        print('%d초 남았습니다' %count)
        time.sleep(1)  #1초 후 다음 문장 실행하는 것임. 딜레이 하는 것.
        count -= 1
    print('폭발')

elif sw =='N' or sw =='n':
    print('작업 취소')
else:
    print('y 또는 n을 누르세요')

"""

print('\ncontinue/break ---')
a = 0
while a <10:
    a += 1
    if a ==3: continue   #아래 문(print 문)을 무시하고 바로 while로 올라가 이동
    if a ==5: continue
    #if a ==7: break   #while 문 무조건 탈출
    print(a)
else:
    print('정상 종료')  #정상 시에 else를 수행함. break를 써서 조건문 빠져나오는 등의 비정상 조건 빠져나올 시에는 else 수행 안 함.
print('while 수행 후 %d'%a)


print('\n키보드로 숫자를 입력받아 홀수 짝수 확인하기(무한반복) -----')
while True:   # True, 1, 100, -12, 4.5, 'ok' ... 등 데이터가 있기만 해도 참 이라는 의미임.
    mysu = int(input('확인할 숫자 입력(예: 5): '))   #input은 숫자도 문자로 인식하기 때문에 숫자 받으려면 앞에 int 정수형 처리 해줘야함
    if mysu == 0:
        print('프로그램 종료')
        break
    elif mysu %2 ==0:
        print("%d는 짝수"%mysu)
        continue
    elif mysu%2 ==1:
        print("%d는 홀수"%mysu)



print('end')