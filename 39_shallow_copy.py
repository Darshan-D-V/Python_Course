import copy
list1=[10,20,30,[40,50]]
list2=copy.copy(list1)#shallow copy
list1[2]=200
print(list2)#change made in list1 is not reflected on list2
list1[3][0]=500
print(list2)#change made in list1 is reflected on list2(only changes made in inner list will be reflected)
print(list1)
