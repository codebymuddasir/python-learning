# SET method
# union and update
#  union method can print all item present in both sets

s1 = {1,2,3,4,5}
s2 = {2,3,4,6}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)
# for example
cities = {"lahore", "karachi","multan"}
cities2 = {"islamabad", "multan" "jatoi"}
cities3 = cities.union(cities2)
print(cities3)
# intersection mean wo value jo dono sets main hai
cities = {"lahore", "karachi","multan"}
cities2 = {"islamabad", "multan","karachi", "jatoi"}
cities3 = cities.intersection(cities2)
print(cities3)
# symetric defrence mean jo value common nhin hogi wo value print ho jai gi
cities = {"lahore", "karachi","multan","jatoi"}
cities2 = {"islamabad", "multan", "jatoi"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# difference and defrence update
cities = {"lahore", "karachi","multan","jatoi"}
cities2 = {"islamabad", "multan", "jatoi"}
cities3 = cities.difference(cities2)
print(cities3)
# idisjoint means they have no interacrion between them yaaano un ka ik dory sy koi matlab nhin hota. THERE HAVE NO ELEMENT IN COMMON.
cities = {"lahore", "karachi","multan","jatoi"}
cities2 = {"islamabad", "multan", "jatoi"}
print(cities.isdisjoint(cities2))
cities = {"lahore", "karachi","multan3","jatoi"}
cities2 = {"islamabad", "multan", "jatoi1"}
print(cities.isdisjoint(cities2))
# is superset
cities = {"Tokyo", "indiai", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "delhi","lahore"}
print(cities.issuperset(cities3))
# is subset means opposit of superset
cities = {"Tokyo", "indiai", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "delhi","lahore"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))
# ADD
cities = {"Tokyo", "indiai", "Berlin", "Delhi"}
cities.add("england")
print(cities)
# remove
cities = {"Tokyo", "indiai", "Berlin", "Delhi", "england"}
cities.remove("england")
print(cities)
# pop
citiesities = {"Tokyo", "indiai", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
# del
cities = {"Tokyo", "indiai", "Berlin", "Delhi"}
del cities
print(cities)
# clear
cities = {"Tokyo", "indiai", "Berlin", "Delhi"}
cities.clear
print(cities) 