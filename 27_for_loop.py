l=[10,20,30,40]#4
for _ in l:
    print("wednesday")

for i in range(1,51):
    print("wednesday",i)


for i in range(4,29,4):
    print(i)

l=[10,20,30,40,50,60,70]
for i in range(0,len(l),3):#for i in range(0,7,3):
    print(l[i])

l=[10,20,30,40,50,60,70]
for i in range(5,0,-2):
    print(l[i])

s={11,22,33,44}
for i in s:#unordered manner
    print(i)
d={1:10,2:20,3:30}
for i in d:#By default when dict is used with for loop we get keys. 
    print(i)
for i in d.values():
    print(i)
for i in d:
    print(d[i])#it will also print values
for i in d.items():
    print(i)
st="Aizen"
for i in st:
    print(i)
print("=======================================")
d={"goku":"DragonBallz","yagami":"DeathNote","ichigo":"Bleach","migi":"parasyte"}
for i in d:
    if i=="yagami":
        print(d[i])
#or
for i in d:
    if i=="yagami":
        print(d.get(i))
print("========================================")
for i in d:
    if "i" in i:
        print(d[i].upper())
    
