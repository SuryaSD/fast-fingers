
def suggest():
 import pandas as pd
 %matplotlib inline 
 import matplotlib.pyplot as plt 
 df = pd.read_csv (r'E:\project\python\python00000\final\tstest2.csv')
 df
 a=input("name : ")
 df=df.loc[df['name']==a.upper()]
 i=len(df)
#print(i)
 name=(df.name[0:len(df)])
 c_word=0
 w_word=0
 ws=(df.ws[0:len(df)])
 os=(df.os[0:len(df)])
# print(ws)
 newws=''.join(ws)
 #print(newws)
    
    
    
    
 a=int(input("time : (in sec)"))
 start = time.time()
#print(type(start))
  
 PERIOD_OF_TIME = a# 5min
 totaltime=PERIOD_OF_TIME
 j=1

 for i in range (len(newws)):
  
   if time.time() < start + PERIOD_OF_TIME:
    
     print(newws[i])

     characters=input("")
     clear_output()
    
    
    
     if(characters==newws[i]):
  

      c_word+=1
    
     elif(characters=="stop"):
            break
     
     else:

      w_word+=1
 print("correct :" ,c_word)
 print("wrong :",w_word)
 
     



