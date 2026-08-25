b=True
i=10
f=2.5
c=1+2j

#int->float
i_f=float(i)
print(i_f)

#int->complex
i_c=complex(i)
print(i_c)

#bool->int
b_i=int(b)
print(b_i)

#bool->float
b_f=float(b)
print(b_f)

#bool->complex
b_c=complex(b)
print(b_c)

#float->complex
f_c=complex(f)
print(f_c)

#int->bool
i_b=bool(i)
print(i_b)

#float->bool
f_b=bool(f)
print(f_b)

#complex->bool
c_b=bool(c)
print(c_b)

#float->int
f_i=int(f)
print(f_i)

#complex->int
#c_i=int(c)#TypeError: int() argument must be a string,
#a bytes-like object or a real number, not 'complex'
#print(c_i)

#complex->float
#c_f=float(c)#TypeError: float() argument must be a string,
#a bytes-like object or a real number, not 'complex'
#print(c_f)




