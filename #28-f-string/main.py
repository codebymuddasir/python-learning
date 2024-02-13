hello = "Hey my name is {1} and I am from {0}"
country = "pakistan"
name = "muddasir"

print(hello.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 232.9087
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))