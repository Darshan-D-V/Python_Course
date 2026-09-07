#2]Local Variables:-
#access the LV inside that function
def fun():
    a=100 #LV
    print("access the LV inside that function",a)
fun()

#1]modifying the LV inside that function
def fun():
    a=100 #LV
    print("access the LV inside that function",a)
    a=a+50
    print("accessing modified value",a)
fun()
#print("access the LV outside that function",a)#not possible

print("==================================================================")

#2]modifying the LV inside that function
def fun(a):
    
    print("access the LV inside that function",a)
    a=a+50
    print("accessing modified value",a)
fun(100)

print("==================================================================")

a=100
def fun():
    global a
    print(a)
    a=200
    print(a)
print(a)
fun()
print(a)
