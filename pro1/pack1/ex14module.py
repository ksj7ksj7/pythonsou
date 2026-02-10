#module: 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리
#하나의 파일은 하나의 모듈이 된다.
#표준 모듈, 사용자 작성 모듈, 제3자 모둘(third party)
print(print.__module__)    #print의 모듈은 표준모듈. builtins


print('뭔가를 하다가...외부 모듈사용하기')
import sys
print(sys.path)   #모듈명.멤버  sys파일 안에 보면 path가 있다는 뜻
a = 5
if a>7:
    sys.exit()   #응용 프로그램의 강제 종료. sys를 강제 종료하고 싶을 때임. sys.exit()에서 ()가 있는 건 exit가 함수거나 메소드라는 뜻  ()가 없으면 그냥 멤버라는 뜻

import math
print(math.pi)

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2026,2)
del calendar

import random
print(random.random())   #이렇게 random.random()하기 귀찮으면 from 쓰기.
print(random.randrange(1,10))

from random import random, choice, randrange  # from '모듈' import '멤버'
print(random())   #위에 from으로 불렀기 때문에 멤버만 써줘도 됨!


print('end')
