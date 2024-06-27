def f1(x):
    return x**2
f1_lamb = lambda x: x**2
print(f1(2)) #4
print(f1_lamb(2)) #4

def f2(list):
    new_l = list.copy()
    for i,x in enumerate(new_l):
        if x %2==0: new_l[i] *=2
    return sum(new_l)

f2_lamb = lambda list: sum(list)
lst = [1,2,3,4]
print(f2(lst))
print(f2_lamb(lst)) 
print(lst)