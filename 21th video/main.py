# default function
def average(a, b):
   print("The average is ", (a*b)/2)

average(4, 9)
# required function
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# keyworn

def name(**name):
    # print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="channar", lname="khan", fname="muddasir")