for i in range(1,5):
    print(i)
    break    
else:
    print("else block")

for i in range(1,5):
    print(i)
    continue    
else:
    print("else block")

roll_no=[101,102,103,104,105,106,107]
rollnumber=int(input("Enter your roll number:"))
for roll in roll_no:
    if roll==rollnumber:
        print("rollnumber found")
        break
else:
    print("rollnumber not found")

