#function: 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위
#함수 고유의 실행 공간을 가짐
#자원의 재활용

#내장함수 일부 체험
print(sum([1,2,3]))
print(bin(8))
print(eval('4+5')) #4+5는 수식인데 '4+5'로 해서 문자열 됨. 이걸 수식화 다시 하는 게 eval 내장 함수임.
print(round(1.2), round(1.6))   #반올림 한 정수

import math
print(math.ceil(1.2), ' ', math.ceil(1.2))  #근사치 정수 중 큰 값 결과: 2
print(math.floor(1.2), ' ', math.floor(1.2))  #근사치 정수 중 작은 값 결과: 1
b_list=[True, 1, False]
print(all(b_list))   #하나라도 false면 false임
print(any(b_list))  #하나라도 true면 true임

data1 = [10,20,30]
data2 = ['a','b']
for i in zip(data1,data2):
    print(i)
    