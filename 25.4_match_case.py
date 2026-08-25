##import keyword
##print(keyword.softkwlist)#['_', 'case', 'match', 'type']

weekday=int(input("Enter weekday number:"))
match weekday:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7|0:
        print("Sunday")
    case _:
        print("Invalid Weekday Number")
        
