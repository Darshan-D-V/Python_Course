#2]function without parameter and with return

def wish_birthday():
    print("happy birthday")
    return "chocolate"

plate=wish_birthday() #or print(wish_birthday)
print(plate)

print("============================================================")

def wish_birthday():
    return "chocolate"
    print("happy birthday")

print(wish_birthday())

print("============================================================")

def send_otp():
    print("otp sent successfully")
    return 647
print(send_otp())

print("=================================================")

#3]function with parameter and without return
def order_food(name,dish,price):
    print(f"{name} has ordered {dish} which costs {price}")
    
order_food("Darshan","Dosa",70)
order_food("Chetan","Biriyani",170)

def book_ticket(name="Darshan",ticketprice=450):
    print(f"{name} has booked the movie ticket for {ticketprice}")

book_ticket()

print("============================================================")

#4]function with parameter and with return

def add(a,b):
    c=a+b
    return c
print(add(2,3))
def subtract(c,d):
    return c-d
print(subtract(6,3))
def multiply(e,f):
    return e*f
print(multiply(3,4))
def division(g,h):
    return g//h
print(division(22,7))


