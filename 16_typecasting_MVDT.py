#Type_Casting among MultiValued Datatype:-
#Achieved only By Explicit Type_Casting.

l=[10,20,30]
t=(21,31,41)
s={11,22,33}
st="abc"
d={1:20,2:40,3:60}

print(tuple(l))
print(set(l))
print(str(l))
#print(dict(l))#TypeError: object is not iterable
#Cannot convert dictionary update sequence element #0 to a sequence

print("=============================")
print(list(t))
print(set(t))
print(str(t))
#print(dict(t))#TypeError: object is not iterable
#Cannot convert dictionary update sequence element #0 to a sequence

print("=============================")
print(list(s))
print(tuple(s))
print(str(s))
#print(dict(s))#TypeError: object is not iterable
#Cannot convert dictionary update sequence element #0 to a sequence

print("=============================")
print(list(st))
print(tuple(st))
print(set(st))
#print(dict(st))#ValueError: dictionary update sequence
#element #0 has length 1; 2 is required

print("=============================")
print(list(d))
print(tuple(d))
print(set(d))
print(str(d))

print("=======================================================================")





