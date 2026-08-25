
r=range(1,8,1)
print(r,type(r))

#explicit typecasting on range object.
print(list(r))
print(tuple(r))

r1=range(1,12)
print(tuple(r1))
print(list(range(12)))

#[-1,-3,-5,-7,-9]
print(list(range(-1,-10,-2)))

#[-9,-7,-5,-3,-1,1]
print(list(range(-9,2,2)))
#print(list(range(3.1,7,1.1)))#TypeError: 'float' object cannot be interpreted as an integer
