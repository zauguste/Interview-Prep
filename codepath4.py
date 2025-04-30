
# # # Problem 1: Prime Number
# # # Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. 
# # # A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

# def is_prime(n):
#     positiveDivisor = 1
#     while positiveDivisor < n:#1 < 5: true
#         if n%positiveDivisor == 0 and positiveDivisor > 1:#if 1 %  == 0 and 1 > 1 - false,9%2 == 0: F and 2 > 1,9%3 == 0: T and 3 > 1
#             # return False
#             return False
#         positiveDivisor += 1 #2,3
#     return True

# # # # Example Usage:

# print(is_prime(5)) 
# print(is_prime(12))# 12//12 == 1 and 12//1 == 5 12/2
# print(is_prime(9)) 
# # Example Output:

# # True
# # False
# # False
# # 💡 Hint: While Loops

# # Problem 2: Two-Pointer Reverse List
# # Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order.
# #  The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

# # Instead, use the two-pointer approach, which is a common technique in which we 
# # initialize two variables (also called a pointer in this context) to track different indices or
# #  places in a list or string, then moves the pointers to point at new indices based on certain conditions.
# #  In the most common variation of the two-pointer approach, we initialize one variable to point at the 
# # beginning of a list and a second variable/pointer to point at the end of list. We then shift the
# #  pointers to move inwards through the list towards each other, until our problem is solved or the 
# # pointers reach the opposite ends of the list.
# # 
# # Check it!
# # we are given a list and we want reverse the list using the two pointer technique
# # does the data type in the array matter? No
# # are we ever given an empty array? Yes 
# # if given empty return 0

# #1 We should handle the first case 
# # if we are given an empty array:
#     #return 0
# #2 lets use the two pointer technique
# #1. initialize the left pointer at the beginning of the array
# #2. initialize the right pointer at the end of the array
# #3. whie l  < r swap
# #4. increment the left pointer incrment the left pointer
# #5. return the list 
# # so lets say we have our list [1,2,3,3,4,5]
# #                                   |
#         #                           |
# # The time complexity is o(n)
# # def reverse_list(lst) -> list:
# #     if len(lst) == 0:
# #         return 0
# #     l = 0
# #     r = len(lst)-1
# #     while l<r:
# #         # swap
# #         lst[l],lst[r] = lst[r],lst[l]
        
# #         l+=1
# #         r-=1
# #     return lst
# # lst = [1, 2, 3, 4, 5,6]
# # print(reverse_list(lst)) 
# # Example Input: 
# # Example Output: [5, 4, 3, 2, 1]

# # 💡 Hint: Two Pointer Technique

# # Problem 3: Evaluating Solutions
# # The reverse_list() problem can also be solved without using the two pointer technique 
# # (as you may have seen it in previous units)! Evaluate the time and space complexity 
# # of your two-pointer solution.

# # Then, evaluate the time and space of the following solution:

# # def reverse_list(lst):
# #     # Create a new reversed list
# #     reversed_lst = lst[::-1]
# #     # Copy the elements back into the original list
# #     for i in range(len(lst)):
# #         lst[i] = reversed_lst[i]
# # Which has better time complexity?
# # Which has better space complexity?

# # 💡 Hint: Big O (Time & Space Complexity)

# # Problem 4: Move Even Integers
# # Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and
# #  moves all the even integers at the beginning of the list followed by all the odd integers.
# #  The function returns any list that satisfies this condition.

# # def sort_array_by_parity(nums):
# #     pass
# # Example Usage:

# # [4,2,3,1]
# #    |             
# #     |
# # l == r
# #  r+=1 
# # if l is odd and right is even swap
#     # l+=1
# # elif r is odd and right is even swap
#     # r-=1
# #      
# # if l is < r and l is not odd increment left
# nums = [3,1,2,4]

# def sort_array_by_parity(nums) -> []:
#     l = 0
#     r = len(nums)-1
# # [3,2,1,4]
# #  |     |
# # we need some conditional.
# # if the left is odd and  the right pointer is even: switch, hold = 3, replace right pointer with hold, shift pointers

# # else:
# #     shift pointer
# # since the array is indexed based we dont want to go out of bounds
# # 25 min
#     while l <= r: #0<=3
#         if  nums[l]%2!=0 and nums[r]%2==0:# true and  true,
#             # swap
#             hold = nums[l] 
#             nums[l] = nums[r]
#             nums[r] = hold
#             l+=1
#             r-=1
#         else:
#             l+=1
#             r-=1
            
#     return nums


# # nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))
# Example Output:

# [2,4,3,1]
# # Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
# [0]

# Problem 5: Palindrome
# Write a function first_palindrome() that takes in a list of strings words as a parameter 
# and returns the first palindromic string in the list. 
# A string is palindromic if it reads the same forward and backward. 
# If there is no such string, return an empty string ""

# def first_palindrome(words) -> str:
#     for string in words: #abc
#         l = 0
#         r = len(string)-1 #2
#         while l <= r:#0<=2,
#             if string[l] != string[r]: #a != c
#                 break #break
#             elif string[l] == string[r] and (l == r or l == r-1): #
#                 return string
#                 break
#             else:
#                 l+=1
#                 r-=1
#     return ""    

# # we want to ensure we have a palindronic string
# # llll
# #  ||

# Example Usage:#

# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)
# Example Output:


# ada
# racecar

# 💡 Hint: Helper Functions

# Problem 6: Remove Duplicates with O(1)
# Write a function remove_duplicates() that takes in a sorted list of 
# integers nums as a parameter and removes the duplicates in-place such that each element appears only once. 
# Do not allocate extra space for another array; you must do this by modifying the
# input list with O(1) extra memory. The function returns the new length of the list.

# Notes: We want to modify a list without using any extra space to remove the duplicates within the given array.

# lets try starting at the first index
# traverse the array and compare the left the the right and make a comparision
# we can use the 2 pointer technique

# We can accomplish this by pointing at index: 0 our left pointer

# # Helper function 

# def count(nums) -> int:
#     n = 1
#     for i in nums:
#         if i != '':
#             n+=1
#     return n

# # primary function
# def remove_duplicates(nums) -> int:
#     l = 0
#     r = 0

#     for l in range(len(nums)-1):
#         r = l+1
#         while r < len(nums)-1:
#             if nums[l] == nums[r] and r <= len(nums)-1:
#                 nums[r] = ""
#             r +=1

#             if nums[l] != nums[r]:
#                 continue
#     return count(nums)


# # Example Usage:
#         # 0 1,2,3,4,5,6,7
# nums = [1,1,1,3,4,4,5]
# #     #   L 
# #     #     R      
# #         #  if l equal r delete right and r +=1 loop again, 
# #         #                         else:
# #                                     # l+=1 
# #                                     # l = r 

# # # do until the end of the array is reached
# # # then count all the numbers

# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list
# # Example Output:

# [1,1,2,3,4,4,4,5]
# 5
# [1,2,3,4,5]

# Problem set version 1 is done






# Problem Set Version 2
# Problem 1: Perfect Number

# Write a function is_perfect_number() that takes in a positive integer n and returns 
# True if it is a perfect number and False otherwise. 
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

# For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.


# Notes:
# we want to return true if we can add numbers that divide into the given number equals and those numbers
# euqal the given number excempt the number itself

# 10 divisors: 1,2,5 == 8 return False,
# take the divisors
# add the divisors
# compare to original



# done
# def is_perfect_number(n) -> bool:
#     i = 0
#     total=0
#     while i < n:
#         if i > 0  and n%i == 0:
#             total += i

#         i+=1
#     if total == n:
#         return True
#     else:
#         return False

# Example Usage:

# print(is_perfect_number(6))
# print(is_perfect_number(28))
# print(is_perfect_number(9))
# Example Output:

# True
# True
# False
# 💡 Hint: While Loops

# Problem 2: 2-Pointer Palindrome
# Write a function is_palindrome() that takes in a string s as a parameter and
#  returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

# The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.



# notes:
# 1. We need to use the two pointer technique to go through the string s by starting at opposite side of the array 
# 2. check if the elements at the left and right equal each other and l and r are less than or equal
# l = 0 start at 0
# r = len(s)-1 start at len(s)-1
# while l<=r: 
#     while l < r and not alph(s[l]):
    #       increment the left pointer
          # l+=1
#      while r > l and not alph(s[r]):
    #       decrement the right pointer
          # r-=1
        # if s[l]!=s[r]:   
            # return False


# helper
# 
# True
# False
# 💡 Hint: Two Pointer Technique

# Problem 3: Evaluate Palindrome
# The is_palindrome() problem can also be solved without using the two-pointer technique (as you may have seen it in previous units)! 
# Evaluate the time and space complexity of your two-pointer solution.

# Then, evaluate the time and space complexity of the following solution:

# def is_palindrome(s):
#     reverse = s[::-1]
#     return reverse == s
# Which has better time complexity?
# Which has better space complexity?

# 💡 Hint: Big O (Time & Space Complexity)







# Problem 4: Make Palindromes
# You are given a string s consisting of lowercase English letters,
#  and are allowed to perform operations on it. 
# In one operation, you can replace a character in s with another lowercase English letter.

# Write a function make_palindrome() that takes in a string s and turns it into a 
# palindrome with the minimum number of operations as possible. 
# If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

# The function returns the resulting palindrome string.

# notes:understand: we want to go through the string and retrieve the letter that is going to make the string a palidrome
# match: we can utilize the two pointer technique to do this.
# plan: 
# 1. starting at both ends of the string
# 2. compare if same:  work inwards
            # else: change left to right
            #   
#   efcfe: 
#    | |
# 


def make_palindrome(s) -> str:
    
    sArr = []
    for i in s:
        sArr.append(i)

    l = 0
    r = len(sArr)-1
    while l <= r:
        if sArr[l] != sArr[r]:
            # check if lexilogically smaller else s[r] = s[l]
            if ord(sArr[r]) > ord(sArr[l]):
                sArr[r] = sArr[l]
            else:
                sArr[l] = sArr[r]
        else:
            l+=1
            r-=1
    s = "".join(sArr)
    # space - o(n^2) time- o(n)
    return s
# Example 1:

# s = "egcfe"
# s_pal = make_palindrome(s)
# print(s_pal)
# print(s_pal == "efcfe")
# # The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# # another palindrome possible is "egcge", but it is not lexicographically smaller
# Example 2:

# s = "abcd"
# s_pal = make_palindrome(s)
# print(s_pal)
# print(s_pal == "abba")
# # The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# # a palindrome cannot be created in 1 operation
# Example 3:

s = "seven"
s_pal = make_palindrome(s)
print(s_pal == "neven")
print(s_pal)
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations

# Done



# Problem 5: Reverse Vowels
# Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.

# def reverse_vowels(s):
#     pass
# Example Usage:

# s1 = "hello"
# rev_s1 = reverse_vowels(s1)
# print(rev_s1)

# s2 = "leetcode"
# rev_s2 = reverse_vowels(s2)
# print(rev_s2)
# Example Output:

# holle
# leotcede
# 💡 Hint: Helper Functions

# Problem 6: Two-Pointer Remove Element
# The two-pointer approach can also be used with two pointers that iterate forward through a list
#  or string at different rates. Use two pointers to solve the following problem:

# Write a function removeElement() that takes in a list nums and a value val as parameters and removes 
# all instances of that value in-place. The function returns the new length of nums.



# notes
# we want to remove all instances of a given number
# using two pointers we can


# def removeElement(nums, val):
#     pass
# Example Usage:

# nums = [5, 4, 4, 3, 4, 1]
# nums_len = removeElement(nums, 4)
# print(nums) # same list
# print(nums_len)
# Example Output:

# [5, 3, 1]
# 3

# Problem Set Version 3
# Problem 1: Highest Exponent
# Write a function find_highest_exponent() that takes in an integer base and an integer limit as parameters. The function returns the highest exponent for which a given base raised to that exponent is less than or equal to limit.

# def find_highest_exponent(base, limit):
#     pass
# Example Usage:

# exp = find_highest_exponent(2, 100)
# print(exp)

# exp2 = find_highest_exponent(3, 5)
# print(exp2)
# Example Output:

# # 2^6 = 64 and 2^7 = 128
# 6
# # 3^1 = 3 and 3^2 = 9
# 1
# 💡 Hint: While Loops

# Problem 2: Two-Pointer Target Sum
# Write a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

# The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

# def two_sum(nums, target):
#     pass
# Example Usage:

# nums = [2,7,11,15,7]
# sol1 = two_sum(nums, 9)
# print(sol1)
# sol2 = two_sum(nums, 18)
# print(sol2)
# Example Output

# [0,1]
# [1,2]
# 💡 Hint: Two Pointer Technique

# Problem 3: Evaluate Two Sum
# The two_sum() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

# Then, evaluate the time and space complexity of the following solution:

# def two_sum(nums, target):
#     prev_map = {}  # Value to index mapping
    
#     for i in range(len(nums)):
#         diff = target - nums[i]
#         if diff in prev_map:
#             return [prev_map[diff], i]
#         prev_map[nums[i]] = i
# Which has better time complexity?
# Which has better space complexity?

# 💡 Hint: Big O (Time & Space Complexity)

# Problem 4: Two-Pointer Reverse Letters
# Using the two-pointer approach, write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.

# def reverse_only_letters(s):
#     pass
# Example Usage:

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# Example Output: j-Ih-gfE-dCba


# Problem 5: Reverse Prefix
# Write a function reverse_prefix() that takes in a 0-indexed string word and a character ch as parameters. The function reverses the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive) and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the resulting string.

# def reverse_prefix(word, ch):
#     pass
# Example Usage:

# word = "abcdefd"
# rev_word = reverse_prefix(word, "d")
# print(rev_word)

# word2 = "helloworld"
# rev_word2 = reverse_prefix(word2, "w")
# print(rev_word2)

# word3 = "xyzxyz"
# rev_word3 = reverse_prefix(word3, "a")
# print(rev_word3)
# Example Output:

# dcbaefd
# wollehorld
# xyzxyz

# Problem 6: Squash Spaces
# The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

# Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed.
# Do not use any of the built-in trim methods.

# def squash_spaces(s):
#     pass
# Example Usage:

# print(squash_spaces("  hello    world  "))
# print(squash_spaces("  what  about  this    ?"))
# print(squash_spaces("this is my sentence"))
# Example Output:

# hello world
# what about this ?
# this is my sentence
