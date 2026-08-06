#Methods of Set:-
s1=set()#empty set

#1]ref.add(object)
#it adds the object randomly into the set.
s1.add(24)
print(s1)
s1.add(36)
s1.add(48)
print(s1)

#2]ref.update(collection)
#it copies and adds the collection elements into the reference set.
s2={10,20,30}
s1.update(s2)
print(s1)

print("-----------------------------------------------")

#3]ref.pop()
#it removes and returns an arbitrary(random) element from the set.
var = s1.pop()
print(var)
print(s1)

#4]ref.remove(object)
#it removes the specified object from the set.
s1.remove(24)
#s1.remove(240)#KeyError: 240,if the object is not found.
print(s1)

#5]ref.discard(object)
#it removes the specified object from the set,
#if the object is not present, it Does Not raise the error.
s1.discard(240)
print(s1)

#6]ref.clear()
#it removes all the set elements.
s1.clear()
print(s1)

#7]set1.issubset(set2)
#it checks if the set2 contains all the elements of set1 and returns boolean value.
s3={10,20,30}
s4={20,30,40,10}
print(s3.issubset(s4))#True
print(s4.issubset(s3))#False

#8]set1.issuperset(set2)
#it checks if set1 contains all the elements of set2 and returns boolean value.
print(s4.issuperset(s3))

#9]set1.isdisjoint(set2)
#it returns False if there is Atleat 1 common elements b/w both sets and returns boolean value.
print(s3.isdisjoint(s4))#False

#10]set1.union(set2)
#it returns a new set which contains the unique elements of both sets.
s5={11,22,33}
s6={33,44,55}
print(s5.union(s6))

#11]set1.intersection(set2)
#it returns the new set which contains the common elements of both sets.
print(s5.intersection(s6))

#12]set1.symmetric_difference(set2)
#it returns the new set which contains the uncommon elements of both sets.
print(s5.symmetric_difference(s6))

#13]set1.difference(set2)
#it returns the new set which contains elements of set1 but not present in set2.
print(s5.difference(s6))

#14]set_name.copy()
#Parameters: None.
#Return Value: A new set object with the same elements.
print(s5.copy())
#or we can store it in var
var=s6.copy()
print(var)



