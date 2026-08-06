#Tuple:-it is predefined class in python.

t1=()#1st way to create a empty tuple
print(type(t1))

t2=tuple()#2nd way to create a empty tuple
print(type(t2))

t3=(10,33,45,45,65)#tuple with elements.
print(type(t3))
#print(t3[10])#IndexError: tuple index out of range
print(t3[2])

t4=(98)
print(type(t4))#<class 'int'>
t5=(98,)#if you want to have a single tuple element use','after that element.
print(type(t5))

#Tuple Methods
#1]ref.count(object)
#it returns the number of occurences of the object.
print(t3.count(45))

#2]ref.index(object)
#it returns the indexnumber of first occurences of the object.
print(t3.index(45))


