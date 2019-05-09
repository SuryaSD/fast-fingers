
def probanalysis():
    
 import pandas as pd
 df = pd.read_csv (r'E:\project\python\python00000\final\tstest2.csv')
 df
 a=input("name : ")
 df=df.loc[df['name']==a.upper()]
 i=len(df)
#print(i)
 name=(df.name[0:len(df)])
# print(name)
#name	ts	acc	nocw	noww	ws	os	date
#nocw=no of correct word
#noww=no of wrong word
#ws=wrong string
#os=original string
 ws=(df.ws[0:len(df)])
 os=(df.os[0:len(df)])
 #print(ws)
# print(os)
#extra=(df.extra[0:len(df)])
#print(type(ws[0]))








#THIRD:




 newws=''.join(ws)
 #print(newws)
 newos=''.join(os)
 #print("newws",newws)
 print(newos)



#FOUR:

 def takefirst(elem):
    return elem[0]


 liws = list(newws)
#print (List)
 Uniq = set(liws)
#print (Uniq)
 countws=[]
 for key1 in Uniq:
    a=liws.count(key1)
    b=(key1, a)
    countws.append(b)
 countws.sort(key=takefirst)  
 #print(countws)


#count original one:

 lios = list(newos)
#print (List)
 Uniq2 = set(lios)
 countos=[]

 for key2 in Uniq2:
    a=lios.count(key2)
    b=(key2, a)
    countos.append(b)
 countos.sort(key=takefirst)  
 #print("countos",countos)
 print("")



 #print(len(countws))
#countos=list(countos)
#countws=list(countws)
#print(countws[0][0])
 for i in range (len(countws)):
   countws[i]=list(countws[i])
   countos[i]=list(countos[i])
   for j in range (len(countws)): 
    if countws[i][0]==countos[j][0]:
      prob=countws[i][1]/countos[j][1]
      print(countws[i][0]," prob is ",prob*100,"%")
      
      countos[i][1]=prob
      #print("new os",countos[i])
       
    else:
        pass
 #print("check new os",countos)

 totalprob=0
 for i in range(len(countos)):
    
    totalprob+=countos[i][1]
 #print(totalprob*100,"totalprob")
 print("")
 print("")
 check=[]
 for i in range (len(countos)):
    x=countos[i][1]/totalprob
    countos[i][1]=x
    check.append(x)
 #print("countos is",countos)
 #print(sum(check))








#FIVE:


 mystr=countos
 total2=0

        
		
		
		
#spep 9(each fingers)


 lf1=['r','f','v','t','g','b']

 lf2=['e','d','c']

 lf3=['w','s','x']

 lf4=['q','a','z']


 rf1=['y','h','n','u','j','m']

 rf2=['i','k']

 rf3=['o','l']

 rf4=['p',';']


 lrf=[lf1,lf2,lf3,lf4,rf1,rf2,rf3,rf4]

#print(countos)


 

 def fingers(finger):

  num=0
  l=0
  for i in range (len(countos)):

      if countos[i][0] in finger:
      #if mystr[i][0] in f1:
       l+= countos[i][1]
       num+=1
  if l >0:
   return l

  else:
   return 0
    

 lef=[]
 for i in range (8):
    a=fingers(lrf[i])
    lef.append(a)
    
    #print("left",i,lef[i])




 #print("index : 2 ","middle : 3","ring : 4","pinky : 5")

#print(lef)
 k=0
 bal=0
 bal2=0
 fing=["index","middle","ring","pinky"]
 for i in range(8):
  #print("left hand: ")
  if i  in range(4):
    
    print("left hand ",fing[i],"  : ",lef[i]*100,"%")
   
    
    bal+=lef[i]

    
  else:
    print("right hand ",fing[k]," : ",lef[i]*100,"%")
   
    
    k+=1
    bal2+=lef[i]

 
 #fingers(finger)
 print(" ")
 print(" ")
 print("error in left hand",bal*100,"%")  
 print("error in right hand",bal2*100,'%')
 labels = ['left','right']
 sizes = [bal*100,bal2*100]
 colors = ['yellowgreen', 'gold']
 explode = (0.1, 0)
 plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
 plt.axis('equal')
 plt.show()

