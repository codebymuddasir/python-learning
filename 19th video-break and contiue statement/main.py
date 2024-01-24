#  break statement: agr hum loop ko khtm kr ky ky exist kr dain to us ko break statment khty hain

for m in range(10):
     print("11 *", m+1, "=", 11 * (m+1))
     if(m == 10):
         break 
# #countinious statement
for m in range(11):
   
     print("11 *", m+1, "=", 11 * (m+1))
     if(m == 11):
         print(m)
     continue
m = 1
while True:
    print(m)
    m = m +  1
    if(m%200 == 1):
        break