#String Formatting
#1st way using f string method
num1=50
num2=28
result=num1+num2
print(f"Addition of {num1} and {num2} is {result}")
#or
#print(f"Addition of {num1} and {num2} is {num1+num2}")

player_name=input("enter your favourite cricketer:")
age=int(input("enter age of the player:"))
average=float(input("enter batting average:"))
team=input("enter the country name:")
is_genius=eval(input("is your cricketer a cricketing genius?"))

statement=f"{player_name} whose age is {age} and batting average is {average} plays for {team} is a {is_genius} genius"
print(statement)

#2nd way using format() method
#syntax:-"string with empty placeholders {}{}".format(value1,value2)
statement1="{} whose age is {} and batting average is {} plays for {} is a {} genius".format(player_name,age,average,team,is_genius)
print(statement1)
