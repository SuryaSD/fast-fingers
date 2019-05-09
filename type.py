******importing packages**********
import nltk
import threading
import time
import csv
from IPython.display import clear_output
import matplotlib.pyplot as plt
import random



paragraph=[para1,para2]


ind= random.randint(0,1)


def interface():
  word_data = paragraph[ind]
  name=input("enter your name")
  atime=int(input("time : (in sec)"))
  start = time.time()
#print(type(start))
  
  PERIOD_OF_TIME = atime# 5min
  totaltime=PERIOD_OF_TIME
  j=1


#print(len(word_data))
#print([len(x) for x in word_data.split()])
  nltk_tokens = nltk.word_tokenize(word_data)
#print (nltk_tokens[2])

  my_word=[]
  correct_length=0
  incorrect_length=0
  c_word=0
  w_word=0
  c_w=[]
  w_w=[]
  original=[]
  for i in range (len(nltk_tokens)):
  
   if time.time() < start + PERIOD_OF_TIME:
    
     print(nltk_tokens[i])
    #my_timer.start()
    
    #print(word_data[i])
     a=input("")
     clear_output()
    
     my_word.append(a)
    
     if(a==nltk_tokens[i]):
      correct_length+=len(my_word[i])
      c_w.append(nltk_tokens[i])
        
	 
      c_word+=1
     
     else:
     
      incorrect_length+=len(my_word[i])
      w_w.append(a)
      original.append(nltk_tokens[i])
	 
      w_word+=1
   else:  
     break

#print("typing speed is")
  typingspeed=((correct_length/4)/atime)*60
#print(typingspeed)
#print("accuracy")
  accuracy=((correct_length/(incorrect_length+correct_length))*100)
#print(accuracy)

  print("Accuracy : ",accuracy,'\t\t',"Typing Speed : ",typingspeed)
  print(" Correct word : ",c_word,'\t',"Incorrect word : ",w_word)
  #print(c_word)
  #print("incorrect word")
  #print(w_word)
  #print(c_w)
  #print(w_w)
  #print(original)
  name=name.upper()
  
  #def save(w_w,original):
  b=input("do you wanna save it?")
  if b=="y":
   my_lst = w_w
   l1=len(my_lst)
   print(my_lst)

   original=original
   print(original)
#print(original[1])
   ichar=[]
   for i in range(len(my_lst)):
    if (len(my_lst[i])<len(original[i])):
     for j in range (len(my_lst[i])):
        if (my_lst[i][j]!=original[i][j]):
            ichar.append(original[i][j])
        else:
            pass
    else:
     for j in range (len(original[i])):
        if (my_lst[i][j]!=original[i][j]):
            ichar.append(original[i][j])
        else:
            pass
  # print("your incorrect letters")    
   z3print(ichar)
   iset=set(ichar)
#print(iset)
   ilist=list(iset)
   print(ilist)
   s = ""
  
# joins elements of list1 by '-' 
# and stores in sting s 
   s = s.join(original) 
   s=list(s) 
   print(s)
# join use to join a list of 
# strings to a separator s 
#print(s[0]) 
#want is for to count prob of incorrect letters
   want=[]
   for i in range (len(ilist)):
    for j in range (len(s)):
        if ilist[i]==s[j]:
            want.append(s[j])
        else:
            pass
  # print(want)
   want_str="".join(str(x) for x in want)
   i_str="".join(str(x) for x in ichar)




#extra

   l1=w_w
   l2=original
#print(len(l1[0]))
   extra=[]
   for i in range (len(l1)):
    if len(l1[i])>len(l2[i]):
     for j in range (len(l2[i]),len(l1[i]),1):
        extra.append(l1[i][j])
   print("extra keywords you type")
   print(extra)
   extra_str="".join(str(x) for x in extra)
   print(extra_str)



#third:


   row = [name,typingspeed,accuracy,c_word,w_word,i_str,want_str,extra_str]
   with open(r'E:\project\python\python00000\final\tstest2.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

   csvFile.close()
  else:
        pass

