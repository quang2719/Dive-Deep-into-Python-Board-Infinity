import numpy as np
import array
ar = np.array(['hello','i\'m','quang']) #['hello' "i'm" 'quang'
print(ar)
print(" ".join(ar)) #hello i'm quang

a6 = array.array('i',[0,1,2,0,2]) #array('i', [0, 2, 4])
for x in a6:
    print(x,end = " - ")
    print(a6.index(x))