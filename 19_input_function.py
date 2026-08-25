name=input("Enter your Name:")
print(name)
print(type(name))

print("===============================")

#marks=input("Enter 10th Marks:")
num_marks=int(input("Enter 10th Marks:"))
##num_marks=int(marks)#explicit TC/Parsing
print(num_marks+5)#int+int
print(type(num_marks))

height=float(input("Enter your Height:"))
print(height+2.1)

is_citizen=bool(input("Are You Indian Citizen?"))
print(is_citizen)
print(type(is_citizen))

#it prints True whether you give True or False,Eventhough he is not a citizen.
