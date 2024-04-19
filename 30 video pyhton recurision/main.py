# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1



# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(3))
print(factorial(2))
print(factorial(6))

print(factorial(5))
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1

