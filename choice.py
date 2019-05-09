

def all():
 while True:
    print("  ")
    print("1: type  2:report  3:analysis  4:suggest typing  5:exit")
    a=input("which one you want?  ")
    if(a=="1"):
      clear_output()
      interface() 
  
    elif(a=="2"):
        clear_output()
        report()
        
    elif(a=="3"):
        clear_output()
        probanalysis()
    elif(a=="4"):
        clear_output()
        suggest()
    else:
        break
all()
  
