b = int(input("Enter the value between 2 and 6:"))

if(b<2 or b>6):
    raise ValueError("value should be between 2 and 6")