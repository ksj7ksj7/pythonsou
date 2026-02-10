#opencv(Computer Vision)
#색상처리, 영상처리 주파수 변환 등을 함
# pip install opencv-python

import cv2
print(cv2.__version__)

img1 = cv2.imread('ani.jpg')
print(type(img1))
cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()
#print('end')

#다른 이름으로 저장
cv2.imwrite('ani2.jpg',img1)  #img1 사진을 ani2이름으로 다시 저장
cv2.imwrite('ani3.jpg',img1,[cv2.IMWRITE_JPEG_QUALITY, 10])   #img1사진을 ani3이름으로 다시 저장, 대신 얘는 퀄리티를 떨어뜨린 버전임. 메모리 조금만 쓰도록하기 위해서 > 컨볼루션

#이미지 크기 조절
img2 = cv2.resize(img1, (300,100), interpolation=cv2.INTER_AREA)
cv2.imwrite('ani4.jpg',img2)


#이미지 밝기 조절


#이미지 상하좌우 회전


#특정 영역 자르기

