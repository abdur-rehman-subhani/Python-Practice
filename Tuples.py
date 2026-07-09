tup=(2,43,53,2,3,9,0)
print(type(tup), tup,'\nThe Length of this tuple is: ',len(tup))
print(tup[2],tup[6],tup[-3])
if 53 in tup:
    print('53 is present in tuple')
else:
    print('53 is absent in tuple')

tup2=tup[1:5]
print(tup2)