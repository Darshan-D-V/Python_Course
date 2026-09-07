'''
def outer(): #HOF
    print("outer function body")
    def inner(): #Callback
        print("inner function body")

    return inner #outer function returning the adress of inner function

inner=outer() #or print(outer())
print(inner)
inner()
inner()
'''
#Closure:-
def outer(): #1 #HOF
    a=100 #3 #Enclosing Variable
    def inner(): #4  #Callback
        print("inner function body",a) #8

    return inner #5 #outer function returning the adress of inner function

inner=outer()#2 #inner 6 #or print(outer())
inner() #7

def get_colour():
    colour='red'
    def show_colour():
        print("colour is:",colour)
    return show_colour

show_colour=get_colour()
show_colour()

def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)
    return increment
increment=counter()
increment()
increment()
increment()

print("==============================================================")

def get_colour():
    colour='red'
    def show_colour():
        print("colour is:",colour)
    return show_colour


get_colour()()#first get_colour() gets the function and then () calls that returned function.
              #The last '()' is inner function reference.


        
