# Problem 1: Build a Binary Tree I
# Given the following TreeNode class, create the binary tree depicted in the image below.

# Binary Tree Example

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self,val):
#         new_Node = TreeNode(val)
#         while True:
#             if val > cur.val:
#                 if 

# root = TreeNode(4)
# root.left = TreeNode(5)
# root.right = TreeNode(6)
# cur = root

# 💡 Hint: Binary Trees

# Problem 2: 3-Node Sum I
# Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child,
# return True if the value of the root is equal to the sum of the values of its two children. 
# Return False otherwise.

# Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
        '''CHECK ROOT'''
        if (root.val) == (root.left.val + root.right.val): 
             return True
        else:
             return False
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(5)


c = check_tree(root)
print(c)
# Example Usage:

# Example Input Tree #1: 
#   10
#  /  \C
# 4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False

# Problem 3: 3-Node Sum II
# Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, 
# return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
# 	pass

# Example Usage:

# Example Input Tree #1: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True

# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False

# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False


# Problem 4: Find Leftmost Node I
# Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
# 	pass

# Example Usage:


# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1

# Example Input Tree #3: 

# Input: root = None
# Output: None


# Problem 5: Find Leftmost Node II
# If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

# Evaluate the time complexity of the function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
# 	pass

# Example Usage:

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1

# Example Input Tree #3:

# Input: root = None
# Output: None


# Problem 6: In-order Traversal
# Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def inorder_traversal(root):
# 	pass

# Example Usage:

# Example Input Tree #1: 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: [1,3,2]

# Example Input Tree #2 : 

# Input: root = None
# Output: []

# Example Input Tree #3:
#     1  

# Input: root = 1
# Output: [1]
# 💡 Hint: Traversing Trees

# Problem 7: Binary Tree Size
# Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def size(root):
# 	pass

# Example Usage:

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 5

# Example Input Tree #2: 

# Empty tree (None)
# Input: root = None
# Expected Output: 0


# Problem 8: Binary Tree Find
# Given a value and the root of a tree, write a function find() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def find(root, value):
# 	pass

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 5
# Expected Output: True

# Example Input Tree #2: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 10
# Expected Output: False

# 💡 Hint: Balanced Trees

# Problem 9: Binary Search Tree Find
# Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def find_bst(root, value):
# 	pass


# # Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4, value = 5
# Expected Output: True

# Example Input Tree #2: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4, value = 10
# Expected Output: False

# 💡 Hint: Binary Search Trees

# Problem 10: BST Descending Leaves
# Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order. Assume the tree is balanced.

# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right
   
# def descending_leaves(root):
# 	pass

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: [5, 3, 1]

# Example Input Tree #2: 
#  10 

# Input: root = 4
# Expected Output: [10]

