# Problem Set Version 1
# Problem 1: Hello Hello
# A recursive function is a function that calls itself within the body of the function.

# Step 1: Copy the recursive function repeat_hello() into Replit and run it.

# Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

# Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

# def repeat_hello(n):
# 	if n > 0:
# 		print("Hello")
# 		repeat_hello(n - 1)
		
# repeat_hello(5)
# 💡 Hint: Recursion


# Problem 2: Factorial Cases
# Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.

# Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.

# Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

# def factorial(n):
# 	pass
# Example Usage:

# # Example Input: 5
# Example Output:

# # Expected Output: 120
# # Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
# 💡 Hint: Writing Recursive Functions

# Problem 3: Recursive Sum
# Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

# What is the time complexity of this function? What is the space complexity?

# def sum_list(lst):
# 	pass
# Example Usage:

# # Example Input: [1, 2, 3, 4, 5]
# Example Output:

# # Expected Output: 15
# # Explanation: 1 + 2 + 3 + 4 + 5 = 15

# Problem 4: Recursive Power of 2
# Given an integer n, return True if n is a power of two. Otherwise, return `False``.

# An integer n is a power of two if there exists an integer x such that n == 2ˣ.

# Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

# def is_power_of_two(n):
# 	pass

# Problem 5: Binary Search I
# Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!

# Evaluate the time and space complexity of your implementation.

# def binary_search(lst, target):
# 	# Initialize a left pointer to the 0th index in the list
# 	# Initialize a right pointer to the last index in the list
	
# 	# While left pointer is less than right pointer:
# 		# Find the middle index of the array
		
# 		# If the value at the middle index is the target value:
# 			# Return the middle index
# 		# Else if the value at the middle index is less than our target value:
# 			# Update pointer(s) to only search right half of the list in next loop iteration
# 		# Else
# 			# Update pointer(s) to only search left half of the list in next loop iteration
	
# 	# If we search whole list and haven't found target value, return -1

# def binary_search(lst, target):
# 	pass
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: 5
# # Explanation: 11 has index 5 in the list
# 💡 Hint: Binary Search

# Problem 6: Backwards Binary Search
# Generally binary search returns the index of the first occurrence of the target in the list. Write an updated version of binary search find_last() that, given a list that may contain duplicates, returns the index of the last occurrence of target.

# Evaluate the time and space complexity of your function.

# def find_last(lst, target):
# 	pass
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: 6
# # Explanation: The second (last) occurrence of 11 has index 6 in the list

# Problem 7: Find Floor
# Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

# Evaluate the time and space complexity of your function.

# def find_floor(lst, x):
# 	pass
# Example Usage:

# # Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5
# Example Output:

# # Expected Output: 1
# # 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.
# Problem Set Version 2
# Problem 1: Counting Down
# A recursive function is a function that calls itself within the body of the function.

# Step 1: Copy this code into Replit and run it.

# Step 2: Then create another function countdown_iterative() that produces the same output without using recursion.

# Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

# def countdown(n):
# 	if n > 0:
# 		print(n)
# 		countdown(n - 1)
		
# countdown(5)
# 💡 Hint: Recursion

# Problem 2: Fibonacci Cases
# Given the base case and recursive case, write a function fibonacci() that returns the nth number in the fibonacci sequence. The Fibonacci sequence is a mathematical sequence of numbers where each number is the sum of the two preceding numbers.

# Base Cases: Because Fibonacci numbers are defined by adding the two previous numbers in the sequence, the first two Fibonacci numbers are pre-defined. By definition, the 0th Fibonacci number is 0, and the 1st Fibonacci number is 1.

# Recursive Case: The nth Fibonacci number is the n-1th Fibonacci number + the n-2th Fibonacci number.

# def fibonacci(n):
# 	pass
# Example Usage:

# # Example Input: 6
# Example Output:

# # Expected Output: 8
# # Explanation: The 6th Fibonacci number is 8. The 5th Fibonacci number is 5 and the 4th Fibonacci
# # number is 3. 5 + 3 = 8.
# 💡 Hint: Writing Recursive Functions

# Problem 3: Recursive Product
# Write a function list_product() that calculates the product of all values in a list recursively.

# What is the time complexity of this function? What is the space complexity?

# def list_product(lst):
# 	pass
# Example Usage:

# # Example Input: [1, 2, 3, 4, 5]
# Example Output:

# # Expected Output: 120
# # Explanation: 1 * 2 * 3 * 4 * 5 = 120

# Problem 4: Recursive Power of 4
# Given an integer n, return True if n is a power of four. Otherwise, return False.

# An integer n is a power of four if there exists an integer x such that n == 4ˣ.

# Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

# def is_power_of_four(n):
# 	pass

# Problem 5: Binary Search II
# Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the recursive solution for binary search below, implement an iterative (non-recursive) implementation of binary search.

# Evaluate the time and space complexity of your implementation.

# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1  # Base case: target not found within bounds

# 		# find middle index of list
#     mid = (left + right) // 2
    
#     # If the middle element is the target, return its index
#     if arr[mid] == target:
#         return mid
#     # If the target is less than the middle element, search the left half
#     elif arr[mid] > target:
#         return binary_search_recursive(arr, target, left, mid - 1)
#     # If the target is greater than the middle element, search the right half
#     else:
#         return binary_search_recursive(arr, target, mid + 1, right)

# def binary_search_iterative(arr, target):
# 	pass
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: 5
# # Explanation: 11 has index 5 in the list
# 💡 Hint: Binary Search

# Problem 6: Find Ceiling
# Given a sorted list of integers and a value x, return the index of the ceiling of x. The ceiling of x is the smallest element in the array larger than or equal to x. If there is no ceiling of x, return -1.

# Evaluate the time and space complexity of your function.

# def find_ceiling(lst, x):
# 	pass
# Example Usage:

# # Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5
# Example Output:

# # Expected Output: 2
# # 8 is the largest element in the list that is greater than or equal to 5. 
# # 8 has index 2 in the list.

# Problem 7: Ternary Search
# Ternary search is a search algorithm that, similar to binary search, works on a sorted array. However, instead of dividing the search interval into two halves (as in binary search), ternary search divides it into three parts, using two midpoints. This reduces the problem size to approximately one-third in each step, rather than one-half.

# Given the pseudocode for ternary_search() below, implement the function. Evaluate the time and space complexity of your solution

# def ternary_search(lst, target):
# 	pass
#   # Divide the array into three parts using two mid points (mid1 and mid2).
  
#   # While the lower bound is less than or equal to the upper bound:
# 	  # Compare the target value with the values at mid1 and mid2:
# 	      # If the target value matches mid1 or mid2
# 		      # the search is successful.
# 	      # If the target is less than the value at mid1
# 		      # search between the lower bound and mid1 - 1.
# 	      # If the target is between mid1 and mid2
# 		      # search between mid1 + 1 and mid2 - 1.
# 	      # If the target is greater than the value at mid2
# 		      # search between mid2 + 1 and the upper bound.
#   # Return -1, indicating the target is not in the array.
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: 5
# # Explanation: 11 has index 5 in the list
# Problem Set Version 3
# Problem 1: In The Stars
# A recursive function is a function that calls itself within the body of the function.

# Step 1: Copy the recursive function insert_stars() into Replit and run it.

# Step 2: Then create another function insert_stars_iterative() that produces the same output without using recursion or the built-in join() method.

# Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

# def insert_stars(s):
#     # If the string is empty or has only one character, return it as is
#     if len(s) <= 1:
#         return s
#     # Otherwise, insert '*' between the first character and the rest, then recurse
#     else:
#         return s[0] + '*' + insert_stars(s[1:])
        
# insert_stars('abc')
# 💡 Hint: Recursion

# Problem 2: String Length Cases
# Given the base case and recursive case, write a recursive function string_length() that returns the length of a string s without using the built-in len() function.

# Base Case: An empty string should have size 0.

# Recursive Case: We can restate the problem to say that the string length is 1 + the length of s[1:].

# def string_length(s):
# 	pass
# Example Usage:

# # Example Input: 'abc'
# Example Output:

# # Expected Output: 3
# 💡 Hint: Writing Recursive Functions

# Problem 3: Recursive Digits Sum
# Given a non-negative integer n, write a function sum_digits() that calculates and returns the sum of its digits recursively.

# Evaluate the time and space complexity of your solution.

# def sum_digits(n):
# 	pass
# Example Usage:

# # Example Input: 523
# Example Output:

# # Expected Output: 10
# 💡 Hint: Finding Digits

# Problem 4: Recursive Count 7s
# Given a non-negative integer n, write a recursive function count_sevens() that returns the count of the occurrences of 7 as a digit.

# Evaluate the time and space complexity of your solution.

# def count_sevens(n):
# 	pass
# Example Usage:

# # Example Input: 727
# Example Output:

# # Expected Output: 2
# # Explanation: 2 digits with value 7 in the number 727

# Problem 5: Binary Search III
# Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search that returns True if the given target is in the list and False otherwise. There is also a recursive alternative that we’ll cover in the session 2 problem set!

# Evaluate the time and space complexity of your implementation.

# def binary_search(lst, target):
# 	# Initialize a left pointer to the 0th index in the list
# 	# Initialize a right pointer to the last index in the list
	
# 	# While left pointer is less than right pointer:
# 		# Find the middle index of the array
		
# 		# If the middle value is the target value, return True
# 		# If the middle value is smaller than the target value, search the right half of the list
# 		# If the middle value is greater than the target value, search the left half of the list
	
# 	# Return False if the target element has not been found

# def binary_search(lst, target):
#     pass
# Example Usage:

# # Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output:

# # Expected Output: True
# 💡 Hint: Binary Search

# Problem 6: Find Missing
# Given a sorted list of integers nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the list.

# Your solution must have O(log n) time complexity.

# def find_missing(nums):
# 	pass
# Example Usage:

# # Example Input: nums = [0,1,3]
# Example Output:

# # Expected Output: 2

# Problem 7: Square Root
# Given a positive number, return the square root of it. If the number is not a perfect square, return the floor of its square root.

# def sqrt(x):
# 	pass
# Example Usage:

# # Example Input: 8
# Example Output:

# # Expected Output: 2