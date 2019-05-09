    
def report():
 from IPython.display import clear_output
 import pandas as pd
 #clear_output()   
 name1=input("name  ")
 df = pd.read_csv (r'E:\project\python\python00000\final\tstest2.csv')
 df
 
 df=df.loc[df['name']==name1.upper()]
 import numpy as np
 import pandas as pd
 ts=(df.ts[0:len(df)])
 acc=(df.acc[0:len(df)])
 #N = 8


 ts = ts
 acc = acc

 ind = np.arange(len(ts))
 width = 0.5     
 plt.bar(ind, ts, width, label='typing speed')
 plt.bar(ind + width, acc, width,
    label='accuracy')

 plt.ylabel('ts/acc')
 plt.title('Typing Speed - Accuracy')

 plt.xticks(ind)
 plt.legend(loc='best')
 plt.show()
 
    
    
    
    
    
    
    
