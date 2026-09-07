#Lambda function:-
'''
var=lambda a,b:a+b
print(var(10,9))

var1=lambda p,q:p*q
print(var1(10,20))

var2=lambda n:n**2
print(var2(6))

var3=lambda a,b,c,d:a+b-c+d
print(var3(10,5,20,15))

check_even=lambda n:n%2==0
print(check_even(10))

#2nd approach-Direct Call:-
#syntax:-(lambda para1,para2,para3:expression) (arg1,arg2,arg3)

print((lambda a,b:a+b )(10,20))

print((lambda n:n**2 )(10))

print((lambda n:n%2==0 )(10))

def square(n): #simple helper function->REPLACES WITH LAMBDA FUNCTION
    return n**2

nl=[]
def transform(fun,col):#HOF
    for i in col:
        result=fun(i)
        nl.append(result)
    return nl


l=[10,20,30,40,50]
print(transform(square,l))
'''
nl=[]
def transform(fun,col):
    for i in col:
        result=fun(i)
        nl.append(result)
    return nl


l=[10,20,30,40,50]
print(transform(lambda n:n**2,l))
#print(transform(lambda n:n**3,l))
