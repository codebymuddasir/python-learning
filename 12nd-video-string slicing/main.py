fruite = "Apple"
#we can find the length of string using len() fuction 
#You can return a range of characters by using the slice syntax.
Applelen = len(fruite)
print(Applelen)
print(fruite[0:5]) # including 0 but not 5
print(fruite[3:2]) # including 3 but not 2
print(fruite[:4])
print(fruite[0:-3])
print(fruite[:len(fruite)-3])
print(fruite[-5:len(fruite) - 3])
print(fruite[-3:-1])

