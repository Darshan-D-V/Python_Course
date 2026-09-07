#Generator:-user defined function containing atleast one yield kw.

def fun():  #generator function
    yield 10
    yield 20
    yield 30

gen_obj=fun() #when u call generator fun it returns generator obj 
              #and this generator obj is called iterator.
print(gen_obj)    
print(next(gen_obj))#10
print(next(gen_obj))#20
print(next(gen_obj))#30
#print(next(gen_obj))#StopIteration



def fun():
    value=0
    yield value
    value+=1
    yield value
    value+=2
    yield value**2
    value+=3
    yield value**3
    value-=2
    yield value**2
gen_obj=fun()
'''
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
#print(next(gen_obj))#StopIteration
'''
for i in gen_obj:
    print(i)
'''   
print(list(gen_obj))
#print(next(gen_obj))
'''
