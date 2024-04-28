a = input("Enter a number:" )
print("The multiplication table of {a} is:")
try:
   for b in range(1, 1133):
    print(f"{int(a)} * {b}) = {int(a)*b}")
except:
  print("invalid INput")
    
print("these are imp code")
print("End of progrm")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")
  
  