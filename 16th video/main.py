a = int(input("Enter the value of a: "))

match a:
    
    case 0:
        print("a is zero")
    
    case 4:
        print("case is 4")

    case _ if a!=40:
        print(a, "is not 40")
    case _ if a!=30:
        print(a, "is not 30")
    case _:
        print(a)
