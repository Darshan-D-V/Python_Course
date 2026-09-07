#Nested Function

def outer():#1]OFD
    print("outer function body") #3.OFB
    def inner():#4.IFD
        print("inner function body")#6.IFB
        
    inner()#5.IFC
    
outer() #2.OFC

print("==============================================================")
a=100
def outer():
    print("outer function body",a) 
    def inner():
        print("inner function body",a)
        
    inner()
    inner()
outer() 

print("==============================================================")


#Enclosing Variables:-
a=100 #GV 
def outer():
    b=200 #Enclosing Variable
    print("outer function body",a,b) 
    def inner():
        c=300 #LV
        print("inner function body",a,b,c)
        
    inner()
outer()

print("==============================================================")

#modification of enclosing variable inside inner function using 'nonlocal' keyword
a=100 #GV 
def outer():
    b=200 #Enclosing Variable 
    def inner():
        nonlocal b #modify of enclosing variable inside inner function
        b=b+20
        print("inner function body",b)
        
    inner()
outer()

print("==============================================================")

#modification of enclosing variable & global variable inside inner function using 'nonlocal'&'global' keyword
a=100 #GV 
def outer():
    b=200 #Enclosing Variable 
    def inner():
        nonlocal b #modify of enclosing variable inside inner function
        global a #modify of global variable inside inner function
        b=b+20
        a=a*2
        print("inner function body",a,b)
        
    inner()
outer()

print("==============================================================")

def counter():
    count=0 #EV
    a=2
    def increment():
        nonlocal count
        count+=1
    def decrement():
        nonlocal a
        a-=1
    increment()
    increment()
    print("count value:",count)
    decrement()
    print("count a:",a)
    
    
counter()



