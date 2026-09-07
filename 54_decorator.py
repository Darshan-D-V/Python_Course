#Decorator:-

def decorator(fun):#decorator function #HOF
    def wrapper(): #wrapper function containing the decoration logic 
        print("select gift paper")
        fun() #gift()
        print("add label to the gift")
    return wrapper
def gift():#callback              #function to be decorated
    print("coffee mug gift ")

gift=decorator(gift)
gift()

print("===========================================")

def decorator(fun):
    def wrapper():
        print("take the box")
        fun()
        print("add a label above cake")
        print("place candle above box")
    return wrapper
def cake():
    print("chocolate cake")
decorator(cake)()

print("===========================================")

def decorator(fun):#decorator function #HOF
    def wrapper(name): #wrapper function containing the decoration logic 
        print("select gift paper")
        fun(name) #gift(name)
        print("add label to the gift")
    return wrapper
def gift(name):#callback              #function to be decorated
    print(f"{name} gift ")

gift=decorator(gift)
gift("Smiling Buddha")

print("===========================================")

def decorator(fun):
    def wrapper(name,price):
        print("take the box")
        fun(name,price)
        print("add a label above cake")
        print("place candle above box")
    return wrapper
def cake(name,price):
    print(f"{name} cake selected which costs {price}")
decorator(cake)("Chocolate",500)

print("===========================================")

def decorator(fun):
    def wrapper(*args): 
        print("select gift paper")
        fun(*args) 
        print("add label to the gift")
    return wrapper
def gift(*args):
    print("Gift selected",args)

gift=decorator(gift)
gift("Smiling Buddha",800,"Prakash gift store","ceramic","gold","Mumbai")

print("===========================================")

def decorator(fun):
    def wrapper(*args):
        print("take the box")
        fun(*args)
        print("add a label above cake")
        print("place candle above box")
    return wrapper
def cake(*args):
    print("cake selected",args)
decorator(cake)("Bread","cream","Milk","egg","water")

print("===========================================")

def decorator(fun):
    def wrapper(*args,**kwargs): 
        print("select gift paper")
        fun(*args,**kwargs) 
        print("add label to the gift")
    return wrapper
def gift(*args,**kwargs):
    print("Gift selected",args,kwargs)

gift=decorator(gift)
gift("Smiling Buddha",800,"Prakash gift store",material="ceramic",color="gold",place="Mumbai")

print("===========================================")

def decorator(fun):
    def wrapper(*args,**kwargs):
        print("take the box")
        fun(*args,**kwargs)
        print("add a label above cake")
        print("place candle above box")
    return wrapper
@decorator #automated way of calling decorator
def cake(*args,**kwargs):
    print("cake selected",args,kwargs)
#cake=decorator(cake)
cake("Honey Cake",40,"egg",Bread="Brown",cream="whipped cream",Milk="Saturated Milk")

print("===========================================")
def decorator(fun):
    def wrapper():
        print("function started")
        fun()
        print("function ended")    
    return wrapper

@decorator
def login():
    print("login operation")
@decorator
def payment():
    print("payment operation")
@decorator
def logout():
    print("logout operation")

login()
payment()
logout()
  


