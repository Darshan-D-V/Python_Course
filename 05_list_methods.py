l1=[]

#1]append()
#ref.append(object)
#it appends the object to the end of the list.
#it takes only one object.
l1.append(10)
print(l1)
l1.append(20)
l1.append(30)
print(l1)

print("--------------------")

#2]ref.insert(index,object)
#it inserts the object to the specified index number,
#the existing element should shift to the right by 1 position.
#l1.insert(1)#TypeError: insert expected 2 arguments, got 1
l1.insert(1,400)
print(l1)

l2=[11,22,33]
#l1.append(l2)#if we use this it will give the output like this ,[10, 400, 20, 30, [11, 22, 33]]
#it will treat entire list as one element.
#print(l1)

#3]ref.extend(collection)
#it copies and adds the elements of the collection
#into the list.
l1.extend(l2)
print(l1)
print(l2)

print("--------------")

l4=[10,20,30]
l5=[11,22,33]
l6=l4+l5
print(l6)#new list is created , no previous lists are affected.

#4]ref.pop()
#it removes and returns the last element from the list.
l6.pop()
print(l6)
##ref.pop(indexnumber)
#it removes and returns the specific element from the list.
x=l6.pop(2)
print(x)
print(l6)

print("----------------------------------")

#5]ref.remove(object)
#it removes the specified object from the list and
#if the element is repeated the first occurence will be removed 
l7=[10,20,30,10,10,40]
l7.remove(10)
print(l7)
#l7.remove(50)# 50 is not in list,ValueError: list.remove(x): x not in list
#print(l7)

print("-------------------------------")

#6]ref.clear()
#it removes entire list elements
l7.clear()
print(l7)

print("-------------------------------")

#7]ref.count(object)
#it returns the number of occurences of that object.
l8=[22,33,11,34,45,11]
print(l8.count(11))

print("-------------------------------")

#8]ref.index(object)
#it returns the indexnumber of the first occuring object
print(l8.index(11))
#print(l8.index(20))#ValueError: list.index(x): x not in list

print("--------------------------------")

#9]ref.sort()
#it sorts the list in Ascending order by default
l8.sort()
print(l8)
#ref.sort(reverse=True)
#it sorts the list in Descending order by default
l9=[2,4,3,6,7,5,1]
l9.sort(reverse=True)
print(l9)
print("-----------------------------")

#10]ref.reverse()
l=[3,4,2,5,3,4,6]
l.reverse()
print(l)

#11]var=ref.copy()
#it copies a element from ref to var ,the var with same elements as ref.
a=[10,20,30]
b=a.copy()
print(b)

#another example
c=[10,20,30]
d=c#whenever we use this,
#if we try to modify any of the list it will change in both. 
d.append(50)
print(c)#output:[10, 20, 30, 50]
print(d)#output:[10, 20, 30, 50]
#in the above example we only append 50 to d, but it
#was added in both lists.
