'''
DataTypes:- It defines the type/nature of the data assigned to a variable.
We don't need to explicitly define a type of the data.

'''
#int
'''age=22
print(age)
var=type(age)#<class 'int'>
print(var)
#print the default value of int
int_obj1= int()##default value of int is 0
print(int_obj1)
'''

#float
'''height=-5.7
print(type(height))#<class 'float'>
#print the default value of float
int_obj2= float()#default value of float is 0.0
print(int_obj2)
'''
#bool
'''is_married=False
print(is_married)
var1=type(is_married)#<class 'bool'>
print(var1)
int_obj3= bool()#default value of bool is False
print(int_obj3)
'''
#complex
c=-3.6+7.1j
print(c)
print(type(c))#<class 'complex'>
print(isinstance(c,int))#it will check the type of the object.
int_obj4= complex()#default value of complex is 0j
print(int_obj4)
print(c.real)#real part
print(c.imag)#imaginary part



