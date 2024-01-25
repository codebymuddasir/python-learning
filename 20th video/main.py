b = 10
c = 12
gmean = (b-c)/(b*c)
print(gmean)

def calculateGmean(b, c):
  mean = (b*c)/(b+c)
  print(mean)

def isGreater(b, c):
  if(b>c):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

  
  

a = 12
b = 14
isGreater(b, c)
calculateGmean(a, b)


b = 10
c = 43
isGreater(b, c)
calculateGmean(b, c)
