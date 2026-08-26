list1=[10,20,30,[40,50]]
list2=list1#generalcopy
list1[2]=200
print(list2)#change made in list1 is reflected on list2
list2[1]=300
print(list1)#change made in list2 is reflected on list1
