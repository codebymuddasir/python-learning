#string methods Python provides a set of built-in methods that we can use to alter and modify the strings.
#upper uper method converts a stig to uper case
met1 = "i am a good boy"
print(met1.upper())

#lower
met2 = "I WANT A CAR"
print(met2.lower())

#rstrip the rstrip() removes any trailing characters
met3 = "muddasir!!!!"
print(met3.rstrip("!"))

#replace
print(met3.replace("muddasir", "rashid"))

#captalize
met4 = "i am a boy a."
print(met4.capitalize())

# center
met5 = 'i am a student'
print(met5.center(25))
print(len(met5))
print(len(met5.center(25)))

# count method
print(met4.count("a"))

# endswith
met6 = "i work daily of python./"
print(met6.endswith("./"))

# find
met7 = "python's is really interesting"
print(met7.find("is"))
 
#isalnum
met8 = "Amanismad"
print(met8.isalnum())  

# islower
met9 = "my name is muddasir"
print(met9.islower())

# isprintable
met10 = "Imran khan is a great leader"
print(met10.isprintable())


# isspce
met11 = "       "
print(met11.isspace())

#istitle The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
met12 = "pakistan"
print(met12.istitle())
met12 = "Pakistan"
print(met12.istitle())

#isupper
met13 = "HELLO PAKISTAN"
print(met13.isupper())

# startwith
met14 = "@codewithmuh"
print(met14.startswith("@"))

# title
met15 = "pakistan is my country"
print(met15.title())

#swapcase The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
met16 = "MY name is MUDDASir"
print(met16.swapcase())