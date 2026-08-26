import copy
list1=[10,20,30,[40,50]]
list2=copy.deepcopy(list1)#deep copy
list1[2]=200#modify using list1
print(list1)#[10, 20, 200, [40, 50]]
print(list2)#[10, 20, 30, [40, 50]]#change made in list1 is not reflected on list2
list1[3][0]=500#modify nested object using list1
print(list1)#[10, 20, 200, [500, 50]]
print(list2)#[10, 20, 30, [40, 50]]#change made in list1 is not reflected on list2
