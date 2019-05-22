# -*- coding: utf-8 -*-
import cv2;

cap = cv2.VideoCapture(0)

def catch_imagine():
	while(1):  #摄像头捕获
		ret,frame = cap.read()
		cv2.imshow("capture",frame)
		if(cv2.waitKey(1)==27):
			break
	cap.release()
	cv2.destroyAllWindows()
def stillcatch_picture(): #连拍
	while(1): 
		ret,frame=cap.read() 
		cv2.imshow('capture',frame) 
		cv2.imwrite('/home/evai/下载/M-system/evai_speech/image/' + str(i) + ".jpg", frame)#将拍摄到的图片保存在data1文件夹中
		print("picture-get")
		i=i+1
		if cv2.waitKey(1)&0xFF==ord('q'):#按键盘q就停止拍照
        		break
	cap.release()
	cv2.destroyAllWindows()

def catch_picture():
	ret,frame=cap.read() 
	cv2.imshow('capture',frame) 
	cv2.imwrite('/home/evai/下载/M-system/evai_speech/image/image.jpg', frame)#将拍摄到的图片保存在data1文件夹中
	print("picture-get")

if __name__=="__main__":
	#catch_picture()
	catch_imagine()
