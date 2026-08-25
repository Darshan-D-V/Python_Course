player_name=input("enter your favourite cricketer:")
age=int(input("enter age of the player:"))
average=float(input("enter batting average:"))
team=input("enter the country name:")
is_genius=eval(input("is your cricketer a cricketing genius?"))

statement=player_name + "whose age is" + str(age) + "and batting average is" + str(average) + "plays for" + team + "is a" + str(is_genius) + "genius"


print(statement)
#it is time consuming and error prone and explicit Type casting and too many '+' operators.


