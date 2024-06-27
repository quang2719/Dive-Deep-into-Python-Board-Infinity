set1 = {1,3,5,6,7}
set2 = set([0,2,4,6,7,8])
print(type(set1),type(set2),sep = "\n") #<class 'set'> \n <class 'set'>
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # {6, 7}
print(set1.difference(set2)) # {1, 3, 5}
