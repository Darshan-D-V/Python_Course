#accept marks from the user,check if it is greater
#than 35,print "positive number"
marks=int(input("enter your marks:"))
print("Start")
if marks>35:
    print("congratulations")
print("End")

#accept any number from the user,check if it is greater
#than 0,print "positive number"
num=int(input("Enter any Number:"))
print("Start")
if num>0:
    print("positive number")
print("End")

#dict
student={21:"krishna",49:"balarama",99:"kamsa"}
#check if kamsa in the student dict,if True,print "danger".
if "kamsa" in student.values():
    print("danger")
