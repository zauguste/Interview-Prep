# Problem 1: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# return True if the input string is valid and False otherwise.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# notes
# we are given '(', ')', '{', '}', '[' or ']' and we must determine if the 
# open brackets are closed by the same type, 
# closed in the correct order and every closed bracket has a corresponding open bracket of same type.

#ei.  if given : ()  
            #    ||
# (([))
#  || return false

# two pointer : o(1)time o(1)memory
# dictionary: ')':'(',  '}':'{', ']':'['
# plan: begin at left and right of string

# left,right = 0, len(s)-1
# while left < right:
# check if s[left] != .get(s[right]): to retrieve key
        # return False
        # else:
            #left+=1
            #right-=1
# return True

s = "()[]{}" #stack: 

def is_valid(s) -> bool:
    stack = []#(
    closed = {')':'(', ']':'[', '}':'{'}
    for i in s:#(
        if i == '(' or '{' or '[':#True
            stack.append(i)
        elif i in closed : #True    
            if stack.pop() != closed[i]:#( !=
                return False
    return True
s = "(]"
print(is_valid(s))
# Example Usage:

# Example #1:
s = "()"
print(is_valid(s))
# Expected Output: True

# Example #2:
#       |
# stack = []#(
# closed = {')':'(', ']':'[', '}':'{'}
# for open in s:#(
#     if open == '(' or '{' or '[':#True
#         stack.append(open)
#     elif open in closed : #True    
#         if stack.pop() != closed[open]:
#             return False

# loop through 
# if open append to the stack
# if closed pop from the stack
# if the stack is not empty return false else true
#         



# Expected Output: True

# Example #3: 
# s = "(())"
# Expected Output: True

# Exampel #4:

# Expected Output: False


# Problem 2: Best Time to Buy & Sell Stock
# You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# def max_profit(prices):
# 	pass

# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Problem 3: Shuffle Merge
# Given the heads of two singly linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists. If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. Return the head of the merged list.

# def shuffle_merge(head_a, head_b):
# 	pass


# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 3


# Problem 4: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# def group_anagrams(strs):
# 	pass

# Example Usage:

# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example #2:
# Input: strs = [""]
# Expected Output: [[""]]

# Example #3:
# Input: strs = ["a"]
# Expected Output: [["a"]]


# Problem 5: Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.

# A leaf node is a node with no children.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sum_numbers(root):
# 	pass 

# Example Usage:

#  Example Input Tree #1:

#       1
#      / \
#     2   3

# Example Input: root = 1
# Expected Output: 25
# Explanation: 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example Input Tree #2:

#       4
#      / \
#     9   0
#    / \
#   5   1

# Input: root = 4
# Expected Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.