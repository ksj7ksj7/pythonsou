# 예외처리: 파일, 네트워크, DB작업, 실행에러 등의 에러 대처

def divide(a, b):
    return a / b

print('이런 저런 작업 진행...')
#c= divide(5,2)
#c = divide(5,0)  # => 결과가 0이라서 false나오니까 에러가 뜨게됨. 이럴 경우 "예외"처리를 해줘야함 / 긴 코드 중에 이런 경우가 있으면 코드 실행 중에 끝까지 못 가고 강제 종료 되게 됨. 이를 방지하기 위함임.
#print(c)

try:
    # 실행문(예외 발생 가능 구문)
    c = divide(5,2)
    #c = divide(5,0)
    print(c)

    aa = [1, 2]
    print(aa[0])  # 에러 없음
    #print(aa[3])   #aa의 3번째 값이 없음. 인덱스 에러가 남

    open("c:/work/abc.txt")

except ZeroDivisionError:   # 예외 종류 관련 클래스
    print('두번째 값은 0을 주면 안돼요')    #예외 발생 처리 구문

except IndexError as err:   #인덱스 에러에 err라는 별명을 붙여줌
    print('참조 범위 오류:', err)   #결과: 참조 범위 오류: list index out of range

except Exception as e:   # 모든 에러에 대한 except 실행
    print('에러:', e)    # 결과: 에러: [Errno 2] No such file or directory: 'c:/work/abc.txt'
finally:
    print('에러 유무에 상관없이 반드시 수행됨')
print('end')