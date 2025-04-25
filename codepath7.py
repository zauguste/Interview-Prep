# # # codepath7.py
# # Problem 2: Factorial Cases
# # Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.

# # Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.

# # Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

# # def factorial(n):
# # 	pass
# # Example Usage:

# # # Example Input: 5
# # Example Output:

# # # Expected Output: 120
# # # Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

# # we have a base case of 0 or 1
# # n = n * factorial(n-1)
# #  n  = 5 *  factorial(4) stack = 20, n = 5* factorial(3) stack = 20 * 3,  n = 10* factorial(2) n = 20, n = n* factorial(1) n = 0,  n = 0* factorial(0) n = 0   
# # n
# def factorial(n):
#     if n == 0:
#         return 1
    
#     return n * factorial(n-1)
    
# print(factorial(5))
# Problem 4: Recursive Power of 2
# Given an integer n, return True if n is a power of two. Otherwise, return `False``.

# An integer n is a power of two if there exists an integer x such that n == 2ˣ.

# Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

def is_power_of_two(n):
	#x = 5
    # n == 2^5

# if n is a power of 2:
#     return True
# else:
#     return False

