for i in range(2,5):
    for j in range(1,4):
        print("{} X {} =".format(i,j),i*j)
#or print(f"{i} X {j} = {i*j}")

l1=["Dosa","Idli","Puri"]
l2=["chutney","sambar","AlooCurry"]
for i in l1:
    for j in l2:
        print(f"{i}->{j}")#or print(i,j,sep="->")
