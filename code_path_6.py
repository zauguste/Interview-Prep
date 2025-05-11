# Breakout Problems Session 1
# 💡 Unit 6 Cheatsheet

# To help your learning journey with linked lists, we've put together a guide to common concepts and syntax you will use throughout Unit 6 breakout problems. 
# Use this cheatsheet as a quick reference guide as you work through the problems below.

# Problem Set Version 1
# Problem 1: Nested Constructors
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 
# in a single assignment statement.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# 💡 Hint: Nested Constructors

# Problem 2: Find Frequency
# Given the head of a linked list and a value val, return the frequency of val in the list. 
# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your 
# solution has the stated time and space complexity.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
#     def count_element(head, val):
#         n = 0
#         while head:
#             if head.val == val:
#                 n+=1

#             head= head.next
#         return n
#       	#start at the head
    # traverse until we val == head.val:
        # n+=1
#   return n

# Example Usage:

# # Input List: 3 -> 1 -> 2 -> 1
# # Input: head = 3, val = 1
# Example Output:

# # 2

# Problem 3: Remove Tail
# The following code attempts to remove the tail of a singly linked list. However, it has a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
        
# # Helper function to print the linked list
# def print_list(node):
#     current = node
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()


# # I have a bug! 
# def remove_tail(head):
#     if head is None: # If the list is empty, return None
#         return None
#     if head.next is None: # If there's only one node, removing it leaves the list empty
#         return None 
		
# 	# Start from the head and find the second-to-last node
#     current = head
#     while current.next: 
#         current = current.next

#     current.next = None # Remove the last node by setting second-to-last node to None
#     return head
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4
# # Input: head = 1
# Example Output:

# # Expected Return Value: 1
# # Expected Result List: 1 -> 2 -> 3

# Problem 4: Find the Middle
# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def find_middle_element(head):
# 	pass
# Example Usage:

# # Input List:
# # 1 -> 2 -> 3
# # Input: head = 1
# Example Output:

# # Expected Return Value: 2
# 💡 Hint: Slow and Fast Pointers

# Problem 5: Is Palindrome?
# Given the head of a singly linked list, 
# return True if the values of the linked list are palindromic and False otherwise. 
# Use the two-pointer technique in your solution.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your s
# olution has the stated time and space complexity.

class Node:
    ''' Node class '''
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
    def print_nodes(self, head) -> int:
        '''print nodes'''
        while head:
            print(head.value)
            head = head.next
    def help_reverse(self, head):
        '''helper function'''
    #   1. draw your prev pointer, current pointer, and next pointer
    #   2. start at the head/C
    #   3. hold the next location before updating it. 
    #   4. make the next location the previous location <- pivot point
    #   5. update previlous to current
    #   6. update current location to next using the held position
    #   7. repeat steps 2 through 6 
# hold: c.n : None
    #   None - 1 - NONE 2 - 1 3 - 2 None
    #                         P      c
# prev = p
# cur = c
# cur.next = c.n   
        prev = None
    #   start at the head
        while head:
    # we want to hold the next location because we are going to update it
    # hold the current location before updating it
            hold = head.next
    # update the next location with the previous location
    # pivot point
            head.next = prev
    # store the current location in prev before moving to the next location
            prev = head
    #   traverse until none
            head = hold
    # update head with the next location
    # return prev
        return prev
    def is_palindrome(self,head) -> bool:
        if not head:
            return False
        # get the middle
        slow,fast = head,head
        reversed_middle_head = Node(-1)
        while slow and fast:
            fast,slow = fast.next.next,slow.next
            if fast == None:
                middle = slow
                # the middle
                reversed_middle_head = self.help_reverse(middle)
        # set pointers
        left,right = head,reversed_middle_head
        # go until none
        while right:
            print(left.value, end=""+"==")
            print(right.value)
            if left.value != right.value: #check for uneqal values
                return False
            left,right = left.next,right.next
        return True
# Example Usage:
node4 = Node('a')
node3 = Node('b',node4)
node2 = Node('b',node3)
head = Node('a',node2)
# node4 = Node('i')
# node3 = Node('b',node4)
# node2 = Node('b',node3)
# head = Node('a',node2)
# while cur not none:
    # hold equals cur.next # None
    # change cur.next to prev
    # change prev to cur
    # change cur to hold
# return prev

# None ->     1->   None  2->  1   3-> 2 None
#                                prev     cur 

CHECK = head.is_palindrome(head)
print(CHECK)
# # Input List:
# # 1 -> 2 -> 1
# # Input: head = 1
# Example Output:

# # True
# 💡 Hint: Multiple Pass Technique




# Problem 6: Put it in Reverse
# Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def reverse(head):
# 	pass
# Example Usage:

# # Input List: 1 -> 2 -> 3 -> 4
# # Input: head = 1
# Example Output:

# # Expected Return Value: 4
# # Expected Result List: 4 -> 3 -> 2 -> 1
# 💡 Hint: Which technique?
