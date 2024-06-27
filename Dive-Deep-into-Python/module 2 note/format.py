# multi line and format string
val_1 = "A"
val_2 = "B"
val_3 = 'C'
print("""The firs val is {0}, 
and the second val is {2}
the final val is {1}""".format(val_1,val_3,val_2))
# ->
#The firs val is A,
#and the second val is B
#the final val is C

ex = "This is a sample sentence for testing split and join operations."
res = ""
for w in ex.split():
    res += w[0].upper() + w[1:] +" "

print(res.strip())