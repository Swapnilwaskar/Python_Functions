# Task 2 Recursive Function: Factorial Utility
# Create a recursive function to calculate the factorial of a number.
def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))