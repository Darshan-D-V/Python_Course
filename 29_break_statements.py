for i in range(2,8):
    print(i) 
    break
print("end")
print("-----------")
for i in range(2,8):
    break
    print(i) #no print(i)
print("end")
print("-----------")
# from range 51 to 70, when any number div by 11
#appears stop
for i in range(51,71):
    if i%11==0:
        break
    print(i)
print("end")
print("-----------")
# when going thru 45 to 67, when a num div by 11
#print only that num and stop
for i in range(45,67):
    if i%11==0:
        print(i)
        break
print("end")
print("-----------")
# when going through 45 to 67, when a num div by 11&3
#print only that nums and stop
for i in range(45,67):
    if i%11==0 and i%3==0:
        print(i)
        break
print("-----------")
l=[487,19390,32,18,7,38,24]
#when iterating thru each l search if there is 18,
#if yes print 'roll no 18 found' and stop the loop
for i in l:
    if i==18:
        print(f"roll no {i} found")
        break







