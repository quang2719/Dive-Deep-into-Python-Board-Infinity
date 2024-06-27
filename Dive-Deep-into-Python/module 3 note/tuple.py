t1 = ('hi','helo',2) # ('hi', 'helo', 2)
print(t1)
t2 = (2)
print(type(t2)) #<class 'int'>
t3 = (2,)
print(type(t3)) #<class 'tuple'>

print(t3.insert(1,2)) #AttributeError: 'tuple' object has no attribute 'insert'