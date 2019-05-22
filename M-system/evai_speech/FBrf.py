# -*- coding: utf-8 -*-

from __future__ import division
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#from sklearn.externals import joblib

global face0,tendency0,bot0,face1,tendency1,bot1
face0=[10,10,10,10,10,10,10,20,20,20,20,20,20,20,30,30,30,30,30,30,30,40,40,40,40,40,40,40,50,50,50,50,50,50,50,60,60,60,60,60,60,60,70,70,70,70,70,70,70]
tendency0=[5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95]
bot0=[1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1]
face1=[10,10,10,10,10,10,10,20,20,20,20,20,20,20,30,30,30,30,30,30,30,40,40,40,40,40,40,40,50,50,50,50,50,50,50,60,60,60,60,60,60,60,70,70,70,70,70,70,70]
tendency1=[5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95,5,15,30,50,70,85,95]
bot1=[1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1]

'''
df=pd.DataFrame({'name':['Lily','Lucy','Jim','Tom','Anna','Jack','Sam'],
                 'face':[42,38,78,67,52,80,92],
                 'tendency':[162,158,169,170,166,175,178],
                 'bot':[0,0,1,0,1,0,1]})
'''
def Training(face,tendency,feedback):
    global face0,tendency0,bot0,face1,tendency1,bot1
    if feedback == 0:
        face1=face0
        tendency1=tendency0
        bot1=bot0
    if feedback == 1:
        face0=face1
        tendency0=tendency1
        bot0=bot1
    df=pd.DataFrame({'face':face0,
                         'tendency':tendency0,
                         'bot':bot0})

    #print(df)
    x=df.loc[:,["face","tendency"]]
    y=df['bot']

    #print(x)
    #print(y)
    
    #print(m)
    #print(n)

    #训练部分



    clf=RandomForestClassifier()

    clf.fit(x,y)

    #joblib.dump(clf,"train_model.m")#保存模型

    #print(clf)

    x_importance=clf.feature_importances_

    #print(x_importance)



    #直接调用部分

    df=pd.DataFrame({'face':[face],
                     'tendency':[tendency]})
    print(df)
    real=df.loc[:,["face","tendency"]]
    
    y_pred=clf.predict(real)#type 'numpy.ndarray'
    #save data
    face1=face0+[face]
    tendency1=tendency0+[tendency]
    bot1=bot0+[y_pred[0]]
    
    #print("result:"+str(y_pred[0]))
    return y_pred[0]
    #print(y_pred)

    #预测准确率
    '''
    l=len(y)
    #print(l)
    i=0
    count=0
    while i<l:
        if y[i] == y_pred[i]:
            count+=1
        i+=1         
    zhunquedu=count/i*100
    print('准确率'+str('%.2f' %zhunquedu)+'%')
    #print(y[4])
    #print(y_pred[4])
    '''
    #模型调用部分
    '''

    clf=joblib.load("train_model.m")

    y_pred=clf.predict(x)

    print(y_pred)

    '''
def Training2(face,tendency,feedback):  
    global face0,tendency0,bot0,face1,tendency1,bot1  
    if int(feedback) == 0:
        face0=face1
        tendency0=tendency1
        if bot1[len(bot1)-1] == 0:
            bot0=bot0+[1.0]
        else:
            bot0=bot0+[0.0]
    if int(feedback) == 1:
        face0=face1
        tendency0=tendency1
        bot0=bot1
        
    df=pd.DataFrame({'face':face0,
                     'tendency':tendency0,
                     'bot':bot0})
    
    #print(df)#数据集
    x=df.loc[:,["face","tendency"]]
    y=df['bot']
    
    #print(x)
    #print(y)

    #训练部分



    clf=RandomForestClassifier()

    clf.fit(x,y)

    #joblib.dump(clf,"model300-1.m")#保存模型

    #print(clf)

    x_importance=clf.feature_importances_

    #print(x_importance)  #输出权重

#社群识别率
    '''
    y_pred=clf.predict(x)
    
    
    l=len(y)
    #print(l)
    i=0
    count=0
    while i<l:
        if y[i] == y_pred[i]:
            count+=1
        i+=1         
    zhunquedu=count/i*100
    #print(zhunquedu)
    pianchadu=100-zhunquedu
    #print(pianchadu)
    print('此时偏差率'+str('%.2f' % pianchadu)+'%')
    #print(y[4])
    #print(y_pred[4])
    '''

#直接调用部分
    df=pd.DataFrame({'face':[face],
                     'tendency':[tendency]})
    print(df)
    real=df.loc[:,["face","tendency"]]
    y_pred=clf.predict(real)
#储存交互数据
    face1=face0+[face]
    tendency1=tendency0+[tendency]
    bot1=bot0+[y_pred[0]]
    #print(y_pred[0])
    if y_pred[0] == 0.0:
        print("那我说话自然点")
    if y_pred[0] == 1.0:
        print("那我说话暖心点")
    return y_pred[0]
#test
if __name__=="__main__":    
    while True:
        face=input("您当前的表情是？:")
        tendency=input("您当前情绪倾向？:")
        feedback=input("上一轮我的表现你可还满意？:")
        gg=Training2(face,tendency,feedback)
	print("我的选择是"+str(gg))

