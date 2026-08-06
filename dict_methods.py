d1={}
d1[29]=200#syntax to modify a value or add keu-value to dict.
d1[70]=56
print(d1)

#1]ref.setdefault(key,optionalvalue)
#it adds the key with the given value into dict,
#but if the value is not given,default value None will be used.
d2={}
d2.setdefault(10,100)
d2.setdefault(20)
print(d2)

#2]ref.update(dict)
#it copies and adds the items of the dict into the ref
d1.update(d2)
print(d1)

#3]ref.get(key)
#it returns the value for the key,
#if the key is not present it returns None.
print(d1.get(70))
#print(d1.get(708))#prints None

#4]ref.pop(key)
#it removes the item and returns the value
var=d1.pop(29)
print(var)
print(d1)
#d1.pop(30)#KeyError: 30
#print(d1)

#5]ref.popitem()
#it does not take any parameter.
#It is going to returns and remove the last item from the dictionary
d1.popitem()
print(d1)
#d3={}
#d3.popitem()#KeyError: 'popitem(): dictionary is empty'
#print(d3)

#6]ref.clear()
#it clears the entire dictionary and makes it empty.
d1.clear()
print(d1)

#7]ref.keys()
#it returns the list of keys from the dictionary.
d3={1:100,2:200,3:300,4:400}
print(d3.keys())

#8]ref.values()
#it returns the list of values from the dictionary.
print(d3.values())

#9]ref.items()
#it returns the list of items from the dictionary but in tuple form.
print(d3.items())


