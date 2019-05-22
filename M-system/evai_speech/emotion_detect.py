#coding=utf-8
import os
from aip import AipFace
import base64
#from catch import catch_picture

APP_ID = '15326441'
API_KEY = 'MSyfmyPQIMkxyq5aBI9Rhcxk'
SECRET_KEY = 'iwEukefbzNzw0Ym71fF5819G4WlGq9PU'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
filePath = r'/home/song/下载/M-system/evai_speech/image/image.jpg'

global gender
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')


imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,emotion,beauty,expression"
def get_emotion():
        global gender
	os.system("fswebcam --no-banner -r 640x480 image/image.jpg")
	#catch_picture()  #OPCV获取图像，报错
	result = aipFace.detect(get_file_content(filePath), imageType, options)
 	a=str(result)
 	if a.find("None") !=-1:
		print("there is no face detected.")				
		human_default=['neutral']+['male']
		return human_default
	face = result['result']['face_list'][0]['emotion']['type']
	'''
	表情特征编码
	'''
    	if face == "angry" :
        	face = 10
    	elif face == "disgust":
        	face = 20
    	elif face == "fear":
        	face = 30
    	elif face == "happy":
        	face = 40
    	elif face == "sad":
        	face = 50
    	elif face == "surprise":
        	face = 60
    	elif face == "neutral":
        	face = 70
	true_emo = result['result']['face_list'][0]['emotion']['probability']
        gender= result['result']['face_list'][0]['gender']['type']
	age=result['result']['face_list'][0]['age']
	#get_emotion=str(emotion)+str(probability)
	#emo=str(emotion)
	#pro=str(probability)
	human=[]
	print(face)
	print(true_emo)
	print(gender)
	print(age)
	human=[face]+[gender]
	return human
#get_emotion()
#print(result)
if __name__=="__main__":
	gg=get_emotion()



