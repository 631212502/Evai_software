#coding=utf-8
import os
from aip import AipFace
import base64

APP_ID = '15326441'
API_KEY = 'MSyfmyPQIMkxyq5aBI9Rhcxk'
SECRET_KEY = 'iwEukefbzNzw0Ym71fF5819G4WlGq9PU'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
filePath = r'/home/evai/下载/M-system/evai_speech/image/image.jpg'

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
	result = aipFace.detect(get_file_content(filePath), imageType, options)
 	a=str(result)
 	if a.find("None") !=-1:
		print("there is no face detected.")
		
		
		human_default=['neutral']+['male']
		return human_default
	emotion = result['result']['face_list'][0]['emotion']['type']
	true_emo = result['result']['face_list'][0]['emotion']['probability']
        gender= result['result']['face_list'][0]['gender']['type']
	age=result['result']['face_list'][0]['age']
	#get_emotion=str(emotion)+str(probability)
	#emo=str(emotion)
	#pro=str(probability)
	human=[]
	print(emotion)
	print(true_emo)
	print(gender)
	print(age)
	human=[emotion]+[gender]
	return human
#get_emotion()
#print(result)
if __name__=="__main__":
	gg=get_emotion()



