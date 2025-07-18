# # Breakout Problems Session 1
# # 💡 Unit 6 Cheatsheet

# # To help your learning journey with linked lists, we've put together a guide to common concepts and syntax you will use throughout Unit 6 breakout problems. 
# # Use this cheatsheet as a quick reference guide as you work through the problems below.

# # Problem Set Version 1
# # Problem 1: Nested Constructors
# # Step 1: Copy the following code into Replit.

# # Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 
# # in a single assignment statement.

# # class Node:
# # 	def __init__(self, value, next=None):
# # 		self.value = value
# # 		self.next = next
# # 💡 Hint: Nested Constructors

# # Problem 2: Find Frequency
# # Given the head of a linked list and a value val, return the frequency of val in the list. 
# # Evaluate the time and space complexity of your solution. 
# # Define your variables and provide a rationale for why you believe your 
# # solution has the stated time and space complexity.

# notes:
# we are given head and val
# return the number of times val occurs in the list
# we can do this by traversing the linked list 
# starting with the head and ending at None
# we may also track the frequency of val by using a starting variable n and incrementing it by one and return the value it produce, hence n
# 1.start with the head
    # and n = 0
    #while head not none:
        # if val is_equal_to head.val:
            # increment n + 1
        # move to next node       


# # class Node:
# # 	def __init__(self, value, next=None):
# # 		self.value = value
# # 		self.next = next
# #     def count_element(head, val):
# #         n = 0
# #         while head:
# #             if head.val == val:
# #                 n+=1

# #             head= head.next
# #         return n
# #       	#start at the head
#     # traverse until we val == head.val:
#         # n+=1
# #   return n

# # Example Usage:

# # # Input List: 3 -> 1 -> 2 -> 1
# # # Input: head = 3, val = 1
# # Example Output:

# # # 2

# # Problem 3: Remove Tail
# # The following code attempts to remove the tail of a singly linked list. However, it has a bug!

# # Step 1: Copy this code into Replit.

# # Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to
#  identify and fix the bug so that the function correctly removes the tail of the list.

# # class Node:
# #     def __init__(self, value=None, next=None):
# #         self.value = value
# #         self.next = next
        
        
# # # Helper function to print the linked list
# # def print_list(node):
# #     current = node
# #     while current:
# #         print(current.value, end=" -> " if current.next else "")
# #         current = current.next
# #     print()


# # # I have a bug! 
# # def remove_tail(head):
# #     if head is None: # If the list is empty, return None
# #         return None
# #     if head.next is None: # If there's only one node, removing it leaves the list empty
# #         return None 
		
# # 	# Start from the head and find the second-to-last node
# #     current = head
# #     while current.next: 
# #         current = current.next

# #     current.next = None # Remove the last node by setting second-to-last node to None
# #     return head
# # Example Usage:

# # # Input List: 1 -> 2 -> 3 -> 4
# # # Input: head = 1
# # Example Output:

# # # Expected Return Value: 1
# # # Expected Result List: 1 -> 2 -> 3

# # Problem 4: Find the Middle
# # A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. 
# If there are two middle nodes, return the second middle node.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# #    def __init__(self, value, next=None):
# #        self.value = value
# #        self.next = next

# # def find_middle_element(head):
# # 	pass
# # Example Usage:

# # # Input List:
# # # 1 -> 2 -> 3
# # # Input: head = 1
# # Example Output:

# # # Expected Return Value: 2
# # 💡 Hint: Slow and Fast Pointers

# # Problem 5: Is Palindrome?
# # Given the head of a singly linked list, 
# # return True if the values of the linked list are palindromic and False otherwise. 
# # Use the two-pointer technique in your solution.

# # Evaluate the time and space complexity of your solution. 
# # Define your variables and provide a rationale for why you believe your s
# # olution has the stated time and space complexity.

# # class Node:
# #     ''' Node class '''
# #     def __init__(self, value, next=None) -> None:
# #         self.value = value
# #         self.next = next
# #     def print_nodes(self, head) -> int:
# #         '''print nodes'''
# #         while head:
# #             print(head.value)
# #             head = head.next
# #     def help_reverse(self, head):
# #         '''helper function'''
# #     #   1. draw your prev pointer, current pointer, and next pointer
# #     #   2. start at the head/C
# #     #   3. hold the next location before updating it. 
# #     #   4. make the next location the previous location <- pivot point
# #     #   5. update previlous to current
# #     #   6. update current location to next using the held position
# #     #   7. repeat steps 2 through 6 
# # # hold: c.n : None
# #     #   None - 1 - NONE 2 - 1 3 - 2 None
# #     #                         P      c
# # # prev = p
# # # cur = c
# # # cur.next = c.n   
# #         prev = None
# #     #   start at the head
# #         while head:
# #     # we want to hold the next location because we are going to update it
# #     # hold the current location before updating it
# #             hold = head.next
# #     # update the next location with the previous location
# #     # pivot point
# #             head.next = prev
# #     # store the current location in prev before moving to the next location
# #             prev = head
# #     #   traverse until none
# #             head = hold
# #     # update head with the next location
# #     # return prev
# #         return prev
# #     def is_palindrome(self,head) -> bool:
# #         if not head:
# #             return False
# #         # get the middle
# #         slow,fast = head,head
# #         reversed_middle_head = Node(-1)
# #         while slow and fast:
# #             fast,slow = fast.next.next,slow.next
# #             if fast == None:
# #                 middle = slow
# #                 # the middle
# #                 reversed_middle_head = self.help_reverse(middle)
# #         # set pointers
# #         left,right = head,reversed_middle_head
# #         # go until none
# #         while right:
# #             print(left.value, end=""+"==")
# #             print(right.value)
# #             if left.value != right.value: #check for uneqal values
# #                 return False
# #             left,right = left.next,right.next
# #         return True
# # # Example Usage:
# # node4 = Node('a')
# # node3 = Node('b',node4)
# # node2 = Node('b',node3)
# # head = Node('a',node2)
# # # node4 = Node('i')
# # # node3 = Node('b',node4)
# # # node2 = Node('b',node3)
# # # head = Node('a',node2)
# # # while cur not none:
# #     # hold equals cur.next # None
# #     # change cur.next to prev
# #     # change prev to cur
# #     # change cur to hold
# # # return prev

# # # None ->     1->   None  2->  1   3-> 2 None
# # #                                prev     cur 

# # CHECK = head.is_palindrome(head)
# # print(CHECK)
# # # Input List:
# # # 1 -> 2 -> 1
# # # Input: head = 1
# # Example Output:

# # # True
# # 💡 Hint: Multiple Pass Technique




# # Problem 6: Put it in Reverse
# # Given the head of a singly linked list, reverse the list, and return the reversed list. 
# # You must reverse the list in place. Return the head of the reversed list.

# # Evaluate the time and space complexity of your solution. 
# # Define your variables and provide a rationale for why you believe your solution has the 
# # stated time and space complexity.

# # class Node:
# #     '''reverse linked list'''
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next
# #     def print_rev(self,head):
# #         '''print the reversed nodes'''
# #         while head:
# #             print(head.value,end="->")
# #             head = head.next

# #     def reverse(self, head):
# #         '''reverse head method'''
# #         prev = None
# #         #   check if we hit None
# #         while head:
# #             # hold the next
# #             hold_next = head.next
# #             # hold the nextchange the next to reference the previous location
# #             head.next = prev
# #             # change the next
# #             prev = head
# #             # go to the next
# #             head = hold_next
# #         return prev
# # # Example Us
# # # age:
# # node3 = Node(3)
# # node2 = Node(2,node3)
# # head = Node(1,node2)
# # node = Node(-1)
# # node.print_rev(head)
# # print('',None)
# # reversed_head = node.reverse(head)
# # node.print_rev(reversed_head)
# # print('',None)
# # # # Input List: 1 -> 2 -> 3 -> 4
# # # # Input: head = 1
# # # Example Output:

# # # # Expected Return Value: 4
# # # # Expected Result List: 4 -> 3 -> 2 -> 1
# # # 💡 Hint: Which technique?
# Problem Set Version 1
# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

# Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(head):
# 	pass
# Example Usage:

# # num1 -> num2 -> num3 -> num1
# print(is_circular(num1))

# # var1 -> var2 -> var3
# print(is_circular(var1))
# Example Output:

# True
# False

# Problem 2: Find Last Node in a Linked List Cycle
# Given the head of a singly linked list, write a function that returns the last node in the cycle. If there is no cycle in the linked list, return None.

# def find_last_node_in_cycle(head):
# 	pass
# Example Input: num1 -> num2 -> num3 -> num4 -> num2

# Example Output: num4

# 💡 Hint: Multiple Pass Technique

# Problem 3: Partition List Around Value
# Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def partition(head, val):
# 	pass
# Example Input:

# # 1 -> 4 -> 3 -> 2 -> 5 -> 2
# # head = 1, val = 3
# Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

# 💡 Hint: Temporary Head Technique

# Problem 4: Convert Binary Number in a Linked List to Integer
# You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def binary_to_int(head):
# 	pass
# Example Usage:

# # 1 -> 0 -> 1
# num1 = 1
# num2 = 0
# num3 = 1
# int_num = binary_to_int(num1)
# # 101 in binary 

# print(int_num)
# Example Output: 5

# 💡 Hint: Binary to Decimal

# Problem 5: Add Two Numbers Represented by Linked Lists
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def add_two_numbers(head_a, head_b):
#     pass

# Example Usage:

# # list 1: 2 -> 4 -> 3 (342)
# # list 2: 5 -> 6 -> 4 (465)
# # head_a = 2, head_b = 5

# sum = add_two_numbers(head_a, head_b)
# print(sum)
# Example Output: 7 -> 0 -> 8

# Explanation: 342 + 465 = 807, so the list is 7 -> 0 -> 8.


# Problem 6: Reverse Sublist of a Linked List
# Given the head of a linked list and indices m and n, reverse the linked list between positions m and n. Assume the linked list uses 1-based indexing and the 0 <= m <= n <= length of list. Return the head of the list.

# def reverse_between(head, m, n):
# 	pass
# Example Usage:

# # input list: 1 -> 2 -> 3 -> 4 -> 5
# reverse_between(head, 2, 5)
# Result Linked List: 1 -> 5 -> 4 -> 3 -> 2


# Problem Set Version 2
# Problem 1: Convert a Singly Linked List to a Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. Write a function that transforms a singly linked list into a circular linked list. Return the head of the linked list. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def make_circular(head):
# 	pass
# Example Usage:

# # Input List: num1 -> num2 -> num3
# make_circular(num1)
# Result Linked List: num1 -> num2 -> num3 -> num1


# Problem 2: Collect Nodes of a Cycle in a Linked List
# Given the head of a linked list, return the elements of any cycle in the linked list as a list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_cycle_nodes(head):
# 	pass
# Example Usage

# # num1 -> num2 -> num3 -> num4 -> num2
# lst = collect_cycle_nodes(num1)
# print(lst)

# # var1 -> var2 -> var3 -> var4
# lst2 = collect_cycle_nodes(var1)
# print(lst2)
# Example Output:

# [num2, num3, num4]
# []
# 💡 Hint: Multiple Pass Technique

# Problem 3: Delete Duplicates in a Linked List
# Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def delete_dupes(head):
# 	pass
# Example Input: 1 -> 2 -> 3 -> 3 -> 4 -> 5

# Example Output: 1 -> 2 -> 4 -> 5

# 💡 Hint: Temporary Head Technique

# Problem 4: Identical Linked Lists
# Two linked lists are identical when they have the same values and the same order of values. Given the heads of two linked lists, write a function that returns True if the the linked lists are identical and False otherwise.

# def is_identical(head_a, head_b):
# 	pass
# Example 1:

# # list1: 1->2->3->4
# # list2: 1->2->3->4
# # head_a = 1, head_b = 1,
# print(is_identical(head_a, head_b))
# Expected Output: True

# Example 2:

# # list1: 1->2->3->4
# # list2: 1->3->4->2
# # head_a = 1, head_b = 1,
# print(is_identical(head_a, head_b))
# Expected Output: False


# Problem 5: Circular Linked List Rotate
# Given the head of a linked list and a non-negative integer k, rotate the list to the right by k places. Return the head of the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value

#         self.next = next


# def rotate_right(head, k):
# 	pass
# Example 1:

# # num1 -> num2 -> num3 -> num4 -> num5
# new_head = rotate_right(num1, 2)
# Expected Output: num4 -> num5 -> num1 -> num2 -> num3

# Example 2:

# # num1 -> num2 -> num3
# new_head = rotate_right(num1, 4)
# Expected Output: num3 -> num1 -> num2


# Problem 6: Circular Linked List Delete
# Given the head of a circularly linked list and a value val, write a function that deletes the first node in the list with value val. Return the head of the modified list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def delete_node(head, val):
# 	pass
# Example 1:

# # num1 -> num2 -> num3 -> num1
# num1 = 1
# num2 = 2
# num3 = 3
# delete_node(num1, 2)
# Result Linked List: num1 -> num3 -> num1

# Example 2:

# # num1 -> num2 -> num3 -> num1
# num1 = 1
# num2 = 2
# num3 = 3
# delete_node(num1, 1)
# Result Linked List: num2 -> num3 -> num2


# Problem Set Version 3
# Problem 1: Circular List Length
# A circular linked list is a linked list where the tail node points at the head node. Write a function that returns the length of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def circular_list_length(head):
# 	pass
# Example Usage:

# """
# Input List:
# 1 -> 2 -> 3
# ^         |
# |_________|
# Input: head = 1
# """
# # Expected Return Valuet: 3
# Problem 2: Detect and Remove Cycle in a Linked List
# Given the head of a linked list, write a function that removes any cycles in the linked list. Return the head of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def detect_and_remove_cycle(head):
# 	pass
# Example Usage:

# """
# Input List
# 1 -> 2 -> 3
# ^         |
# |_________|
# Input: head = 1
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3

# """
# 💡 Hint: Multiple Pass Technique
# Problem 3: Merge Two Sorted Linked Lists
# Given the heads of two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the input lists. Return the head of the result list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def merge_two_lists(head_a, head_b):
# 	pass
# Example Usage:

# """
# Input: List 1: 1 -> 2 -> 4, List 2: 2 -> 3 -> 4
# Input: head_a = 1, head_b = 2
# Output: 1 -> 2 -> 2 -> 3 -> 4 -> 4
# """
# 💡 Hint: Temporary Head Technique
# Problem 4: Skip and Remove Nodes in a Linked List
# Given the head of a linked list and two integers m and n, traverse the list such that you keep the first m nodes then delete the next n nodes. Continue with this pattern until the end of the list is reached. Return the head of the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


# """
# Example usage:

# Input: List 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
# Input: head = 1, m = 2, n = 3

# Output: 1 -> 2 -> 6 -> 7 
# Explanation: Keep first two nodes 1 & 2, delete next three nodes 3, 4, & 5
# Keep next two nodes 6 & 7, delete remaining three nodes 8, 9, & 10


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# """

# def skip_and_remove(head, m, n):
# 	pass

# Problem 5: Rotate a Doubly Linked List to the Left
# Given the head of a doubly linked list and a non-negative integer k, rotate the list to the left by k places. Return the head of the linked list.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution 
# has the stated time and space complexity.


# """
# Input List
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# Input: head = 1, k = 2

# Expected Return value: 4
# Expected Output List: 3 <-> 4 <-> 5 <-> 1 <-> 2

# Explanation: 
# Rotation 1: 2 <-> 3 <-> 4 <-> 5 <-> 1
# Rotation 2: 3 <-> 4 <-> 5 <-> 1 <-> 2

# Input List
# 0 <-> 1 <-> 2
# Input: head = 0, k = 4

# Expected Return value: 4
# Expected Output List: 1 <-> 2 <-> 0
# Explanation: 

# Rotation 1: 1 <-> 2 <-> 0
# Rotation 2: 2 <-> 0 <-> 1 
# Rotation 3: 0 <-> 1 -> 2
# Rotation 4: 1 <-> 2 <-> 0

# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
# """

# def rotate_doubly_linked_list(head, k):
# 	pass

# Problem 6: Merge Nodes Between Zeros in a Linked List
# Given the head of a linked list which contains a series of integers separated by 0s, merge the nodes lying between two zero nodes into a single node whose value is the sum of all the merged nodes. The modified list should not contain any zeroes. The head and tail of the list will be nodes with value zero. Return the head of the merged list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# """
# Input List:
# 0 -> 3- > 1 -> 0 -> 4 -> 5 -> 2 -> 0
# Input: head = 0

# Expected Return value: 4
# Expected Result list: 4 -> 11

# Explanation: 3 + 1 = 4, 4 + 5 + 2 = 11

# Input List: 
# O -> 1 -> 0 -> 3 -> 0 -> 2 -> 2-> 0
# Input: head = 0

# Expected Return Value: 1
# Expected Result List: 1 -> 3 -> 4

# Explanation: 1, 3, 2+ 2 = 4

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# """

# def merge_nodes(head):
# 	pass
