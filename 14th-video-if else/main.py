# conditional operators
# <,>,<=,>=,==,!=
# Ifelse
py = int(input("Enter your age: "))
print("your age is:", py )
if(py>18):
    print("you can drive: ")
else:
    print("you cant drive: ")
print ("Thanks for allow")     
# less then
print(py<18)
# less then equal
print(py<=18)
# equal to
print(py==18)
#greater then
print(py>=18)
# not equal to
print(py!=18)

laptopprice = 65000
budget = 30000
if(laptopprice <= budget):
    print("dont buy")
else:
    print("buy")

no= int(input("Enter the value of no: "))
if (no < 0):
  print("Number is negative.")
elif (no == 0):
  print("Number is Zero.")
elif (no == 435):
  print("Number is lucky.")
else:
  print("Number is positive.")
  