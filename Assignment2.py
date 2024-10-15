"""1. Write a program that finds greatest of three numbers using functions. Pass the numbers as arguments."""

def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
if __name__ == "__main__":
    # Input: Three numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    greatest = find_greatest(a, b, c)
    print(f"The greatest of the three numbers is: {greatest}")


"""2.Write a program to implement these formulae of permutations and combinations.
 Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
 Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!"""


import math

def permutations(n, r):
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    if r > n:
        return 0
    return permutations(n, r) // math.factorial(r)
if __name__ == "__main__":
    # Input: n and r values
    n = int(input("Enter the value of n (total objects): "))
    r = int(input("Enter the value of r (objects taken at a time): "))
    perm = permutations(n, r)
    comb = combinations(n, r)
    print(f"Number of permutations of {n} objects taken {r} at a time: {perm}")
    print(f"Number of combinations of {n} objects taken {r} at a time: {comb}")


"""3.Write a function cubesum() that accepts an integer and returns the sum of the cubes of 
individual digits of that number. Use this function to make functions PrintArmstrong() 
and isArmstrong() to print Armstrong numbers and to find whether is an Armstrong 
number."""

def cubesum(n):
    return sum(int(digit) ** 3 for digit in str(n))

def isArmstrong(n):
    return n == cubesum(n)

def PrintArmstrong(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if isArmstrong(num):
            print(num, end=' ')
    print()  
if __name__ == "__main__":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    PrintArmstrong(start, end)


"""4.Write a Python function to create and print a list where the values are the squares of 
numbers between 1 and 30 (both included)."""


def squares_list():
    squares = [i ** 2 for i in range(1, 31)]
    print(squares)
if __name__ == "__main__":
    squares_list()


"""5.Given a string s = “1234” and an integer n = 5678, concatenate them as a single string 
and then convert the result back to an integer. What is the final integer value?"""


s = "1234"
n = 5678
concatenated = s + str(n)
final_integer = int(concatenated)
print(final_integer)


"""6.Write a Python program that repeatedly asks the user to enter a positive integer. If the 
user enters a negative number or zero, the program should ask again until a positive 
integer is entered"""

def get_positive_integer():
    while True:
        try:
            user_input = int(input("Please enter a positive integer: "))
            if user_input > 0:
                print(f"You entered: {user_input}")
                break
            else:
                print("That's not a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    get_positive_integer()
