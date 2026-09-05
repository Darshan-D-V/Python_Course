'''
l={1:10,2:20,3:30}
a,b,c,=l#unpacking
print(a)#10
print(b)#20
print(c)#30

a,b,c,=l.values()#unpacking
print(a)
print(b)
print(c)

a,b,c,=l.items()#unpacking
print(a)
print(b)
print(c)
'''
l='india'
#a,b,c,d,e,f=l#not enough values to unpack (expected 6, got 5)
#a,b,c,d=l#too many values to unpack (expected 4)
a,b,c,d,e=l
print(a)
print(b)
print(c)
print(d)
print(e)

#extended iterable unpacking
l=[10,20,30,40,50,60,70]
a,b,*c=l
print(a)
print(b)
print(c)

