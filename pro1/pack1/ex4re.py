import re  #정규표현식 지원 모듈 로딩

ss="1234 abc가나다abcABC_123555집에가나요_6'Python is fun'"
print(ss)
print(re.findall(r'123', ss))  #결과: ['123', '123']  / 그리고 '123' 전에 r 넣는 이유는 \n, \t, \b 등 라인 띄워쓰기 들을 없애기 위함임. 데이터가 많을 경우에는 숨어있을 수 있기 때문
print(re.findall(r'가나', ss))  #결과: ['가나', '가나']
print(re.findall(r'[0-9]',ss))  #결과:['1', '2', '3', '4', '1', '2', '3', '5', '5', '5', '6']
print(re.findall(r'[0-9]+',ss)) #결과: ['1234', '123555', '6']
print(re.findall(r'[0-9]{2}',ss))  #결과:['12', '34', '12', '35', '55']
print(re.findall(r'[0-9]{2,3}',ss))  #결과: ['123', '123', '555']
print(re.findall(r'[가-힣]+',ss))  #결과: ['가나다', '집에가나요']
print(re.findall(r'\d+',ss)) #숫자만 넣음. 결과: ['1234', '123555', '6']
print(re.findall(r'\D+',ss)) #숫자만 뺌.. 결과: [' abc가나다abcABC_', '집에가나요_', "'Python is fun'"]
