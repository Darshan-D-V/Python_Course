#Membership Operator
#list
l=[11,12,13]
print(12 in l)
print(12 not in l)

print("===========================")

#string
st="Darshan"
print("D" in st)
print("d" in st)

print("===========================")

#Dict
#in dict by default it will only check keys.
d={1:"Darshan",2:"Chetan","age":22}
print(1 in d)
print("a" in d)#False
print("age" in d)#True,Bcz we need to enter full name
#in order to check values we need to use entire value + d.values()
print("D" in d.values())
print("Darshan" in d.values())
