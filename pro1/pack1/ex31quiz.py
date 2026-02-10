class ElecProduct:   #공통 규칙 선언
    volume = 0
    def volumeControl(self,volume):
        #print(f'볼륨을 조절한다: {volume}')
        pass

# Payment의 자식은 결제를 pay()라는 동일 메소드를 이용하기를 기대
# 동일 인터페이스 구사

class ElecTv(ElecProduct):
    
    def TV1(self):
        print('ElecTv 고유 메소드')

    def volumeControl(self, volume):
    print('금요일 와우')
    self.volume = volume
    print(f'ElecTv 볼륨을 조절한다:{volume}')  #메소드오버라이딩

class ElecRadio(ElecProduct):
    def volumeControl(self,volume):
        sori = volume
        print('ElecRadio 소리를 조절한다: {sori}')

product = ElecProduct()
tv = ElecTv()
product = tv
product.volumeControl(5)
print()
radio=ElecRadio()
product = radio
product.volumeControl(3)
product('-----')


q1 = [ElecTv(), ElecRadio()]
for a in q1:
    a.volumeControl(2)
    print()
