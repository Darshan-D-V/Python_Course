#MAP Function- It is a predefined higher order function
#syntax:- map(function,iterable)
          #function->shud takes one parameter and return one value
          #iterable:-sequence (list,tuple etc)

'''
m=map(lambda n:n**2,[10,20,30,40,50])
print(m)#<map object at 0x000002DA6C279B80>
print(list(m))#explicit typecasting
'''
print(list(map(lambda n:n**2,[10,20,30,40,50])))
