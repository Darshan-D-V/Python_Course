#2]Keyword Argument

def order(dish,hotel,cost,location):
    print(f"i ordered {dish} from {hotel} which costs {cost} at {location}.")

order(hotel="Mandya hotel",cost=250,dish="Biriyani",location="BTM")

print("====================================================")


def order(dish,hotel,cost,location):
    print(f"i ordered {dish} from {hotel} which costs {cost} at {location}.")

order("gobi","empire",location="BTM",cost=250,)#1stpriority for positional arguments nxt for keyword arguments
