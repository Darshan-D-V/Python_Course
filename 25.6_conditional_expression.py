'''
num=40
if num>0:
    print("positive")
else:
    print("Negative")

result="Positive" if num>40 else "Negative"
print(result)
'''
#check if kiran present in the list,if present print length of the list,
#if not present print "not found"
l=['mohan','rohini','kiran']
result2=len(l) if "kiran" in l else "not found" 
print(result2)
result3=len(l) if "Ravana" in l else "not found" 
print(result3)
