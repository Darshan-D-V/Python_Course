#1]Global Variable:-

##Accessing the GV inside and outside the function
a=100 #GV

def fun():#fd
    print("function body")
    print("accessing the GV inside the function",a)#accessing the GV inside the function only by calling function.

print("accessing the GV Outside the function",a) #accessing the GV Outside the function
fun()#function call

print("==================================================================")

#modify global variable outside the function
a=100 #GV

def fun():#fd
    print("function body")
    print("accessing the GV inside the function",a)#accessing the GV inside the function only by calling function.

print("accessing the GV Outside the function",a) #accessing the GV Outside the function
fun()#function call

a=a+50#modification of GV outside the function.
print(a)

print("==================================================================")

#modify global variable inside the function
EX:1
a=100 #GV1
def fun():#fd
    global a#use global keyword when we are trying to modify GV inside the function.
    a=a+300
    print("accessing the GV inside the function",a)

print("accessing the GV Outside the function",a) 
fun()#function call

a=a+50#modification of GV outside the function.
print(a)

print("==================================================================")

#EX:2
a=100 #GV1
b=200 #GV2
def fun():#fd
    global a,b
    a=a+300
    print("accessing the GV1 inside the function",a)
    b=b*5
    print("accessing the GV2 inside the function",b )

print("accessing the GV Outside the function",a) 
fun()#function call

