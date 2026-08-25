'''
temp=float(input("enter the present temperature:"))
if temp>35:
    print("Hot Weather")
elif 15<=temp<=35:
    print("Warm Weather")
elif 8<=temp<=14:
    print("Cool Weather")
else:
    print("Cold Weather")
'''
print("===========================================")
marks=int(input("enter your marks:"))
if 100>=marks>=90:
    print("A Grade")
elif 70<=marks<90:
    print("B Grade")
elif 50<=marks<70:
    print("C Grade")
elif 35<=marks<50:
    print("D Grade")
elif 0<=marks<35:
    print("Fail")
else:
    print("invalid marks entered")

