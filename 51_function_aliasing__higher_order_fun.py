#function aliasing
def eat():
    print("eating is a survival mechanism")
consume=eat #Function Aliasing
eat()
consume()
print(eat)#address
print(consume)#address

#Higher order function
def checkout(paymentmode):#Higher order function
    paymentmode()

def cash():#callback
    print("cash payment")

def card_swipe():#callback
    print("swipe card")

checkout(cash)
checkout(card_swipe)


def conduct_exam(sub):#higher order function
    sub(3)
def java_exam(time):#callback
    print(f"java exam last for {time} hrs")
def python_exam(time):#callback
    print(f"python exam last for {time} hrs")

conduct_exam(java_exam)
conduct_exam(python_exam)
