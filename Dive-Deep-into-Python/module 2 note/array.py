import array as ar
#comment the error line

# a = array.array('type',[ele1,ele2 ...])

# an integer array
a1 =  ar.array('i',[1,2,3]) # array('i', [1, 2, 3])
# error array if add different type element
a2 =  ar.array('i',[1,2,3, 4.0]) # error
# an float array
a3 = ar.array('f',[1,2,3, 4.0]) # array('f', [1.0, 2.0, 3.0, 4.0])
print(a3) # type: ignore

# unicode array
a4 = ar.array('u',['h','e','l','l','o'])
print(a4) # array('u', 'hello')

a5 = ar.array('u',['hello','world']) #error because must be unicode
# character, need to use numpy array 

#slicing
print(a4[1:4]) # array('u', 'ell')
a6 = ar.array('i',[0,1,2,3,4]) #array('i', [0, 2, 4])
print(a6[0:5:2])