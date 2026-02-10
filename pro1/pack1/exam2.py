for i in {1, 2, 3, 4, 5, 5, 5, 5}:
    print(i, end = ' ')

print(5/3)
print(5//3)
print(5%3)

*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)

i = 10
while i >= 1:
    j=i
    msg=''
    while 0 <j <= i:
        msg +="*"
        j -= 1
    print(msg)
    i -= 1

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}', end =' ')


a=1
while a <=9:
    print(f'{3}*{a}={3*a}', end = ' ')
    a = a + 1
else:
    print('')

a=1
while a <=9:
    print(f'{5}*{a}={5*a}', end = ' ')
    a = a + 1
else:
    print('')

a=1
while a <=9:
    print(f'{7}*{a}={7*a}', end = ' ')
    a = a + 1
else:
    print('')

a=1
while a <=9:
    print(f'{9}*{a}={9*a}', end = ' ')
    a = a + 1
else:
    print('')


# class Bicycle:
#     name = 1
#     wheel = 1
#     price = 1

# def __init__(self, name, wheel, price):
#     self.name = name
#     self.wheel = wheel
#     self.price = price

# gildong=Bicycle()
# gildong=Bicycle('길동', 2, 50000)
# print(f'{name}님 자전거 바퀴 총액은 {wheel*price} 입니다')

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 100:
        break

    print(i, end = ' ')
    i +=1

print('')

def Hap(m, n):
  return m + n * 5


Hap = lambda m,n: m+n*5
print(Hap)