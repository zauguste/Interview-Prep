# Problem 4: Calculating Groot's Growth
# Groot grows according to a pattern similar to the Fibonacci sequence. 
# Given n, find the height of Groot after n months using a recursive method.

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Evaluate the time complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time complexity.


# u:calculate the fibonacci sequence
# plan
# n = 5
# base case n <= 1 (is n <=1 no: continue), (7<=1 no: continue)
# recursive case
# return fibonacci_growth(n-1) + fibonacci_growth(n-2) f(4) + f(3) = 7, 
                                                    #   f(3) + f(1) = 4
                                                    #   f(2) + f(0) = 3
                                                    #   f(1) + f(0) = 2

def fibonacci_growth(n):
    if n <= 1: #5
        return n
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)#4 + 3 = 7, 6 + 5= 10

    

print(fibonacci_growth(5))
print(fibonacci_growth(8))
# Example Output:

# 5
# 21
