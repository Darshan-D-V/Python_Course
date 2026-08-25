b=True
i=10
f=2.5
c=5+7j

#single valued DT -> str()
a1=str(b)
print(a1)
print(type(a1))
a2=str(i)
print(a2)
print(type(a2))
a3=str(f)
print(a3)
print(type(a3))
a4=str(c)
print(a4)
print(type(a4))

print("-------------------------------------------")

#collections->Single valued DT
l=[10,20]
t=(23,33)
s={11,22}
st="python"
d={'a':100,'b':200}

print(bool(l))
print(bool(t))
print(bool(s))
print(bool(st))
print(bool(d))

print("=================================================")

#Apply boolean for any default values we get False.
#All default values are Falsy Values
print(bool(False))#Default Value of bool
print(bool(0))#Default Value of int
print(bool(0.0))#Default Value of float
print(bool(0j))#Default Value of complex
print(bool([]))#Default Value of list
print(bool(()))#Default Value of tuple
print(bool(set()))#Default Value of set
print(bool({}))#Default Value of dict
print(bool(''))#Default Value of str
print(bool(None))#Default Value for value in dict

print("===============================================")

#Parsing:-Converting string into its corresponding single valued datatype
#explicitly is known as Parsing.

st1="10"
print(int(st1),type(int(st1)))

st2='2.1'
print(float(st2),type(float(st2)))

st3='3.2j'
print(complex(st3),type(complex(st3)))






