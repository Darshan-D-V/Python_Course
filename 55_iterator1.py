#Iterator
#Note:-Single use object.
#itr_obj:-An iterator object is an object that allows Python to take values one by one from an iterable.
#Think of it like a pointer/bookmark that remembers where you currently are in the list.

#using next():-

l=[10,20,30,40]#iterable
itr_obj=iter(l)#1 calling iter() that returns iterator object
print(itr_obj)
print(next(itr_obj))#10
print(next(itr_obj))#20
print(next(itr_obj))#30

for i in range(1,3):#even after using unrelated operation,the cursor still at the same point.
    print("Money Multiplication")
    
print(next(itr_obj))#40
#print(next(itr_obj))#StopIteration

print("=====================================")

#using for loop:-

l=[10,20,30,40]#iterable
itr_obj=iter(l)
print(itr_obj)
for i in itr_obj:
    print(i)
#print(next(itr_obj))#StopIteration

print("=====================================")

#using explicit typecasting:-

l=[10,20,30,40]#iterable
itr_obj=iter(l)
print(itr_obj)
print(tuple(itr_obj))#explicit typecasting
#print(next(itr_obj))#StopIteration

print("=====================================")

l=[10,20,30,40]#iterable
itr_obj=iter(l)
print(itr_obj)
i=0
while i<len(l): 
    print(next(itr_obj))
    i=i+1
#print(next(itr_obj))#StopIteration
