#클래스는 새로운 타입(정수형 등등..int처럼)을 만들어 자원을공유 가능

# class Singer:
#     title_song = "빛나라 대한민국"

#     def sing(self):
#         msg = "노래는 "
#         print(msg, self.title_song)

from ex22singer import Singer  #원래는 import ex22singer 하고 Singer를 모두 ex22singer로 바꿔야 했음

bts = Singer()   #생성자 호출해 객체 생성 후 주소를 bts라는 변수에 치환
bts.sing()
print(type(bts))
bts.title_song = "permission to dance"  # 기본 클래스, 메소드에 대해서 항목을 바꿀 수 있음
bts.sing()
bts.co = '빅히트 엔터테인먼트'   # 기본 클래스, 메소드에 대해서 항목을 추가할 수 있음
print('소속사: ', bts.co)

print()
ive=Singer()
ive.sing()
print(type(ive))
#print('소속사: ',ive.co)
Singer.title_song="아 대한민국"
bts.sing()
ive.sing()

niceGroup = ive
niceGroup.sing()

