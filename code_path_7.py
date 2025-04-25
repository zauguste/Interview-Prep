# Problem 2: How Many 1s
# Given a sorted list of integers containing only 0s and 1s, c
# count the total number of 1’s in the array in O(log n) time.

# def count_ones(lst):
# 	pass
# Example Usage:

# # Example Input: [0, 0, 0, 0, 1, 1, 1]
# Example Output:

# # Expected Output: 3
# [0,1,0,0,0,1,0,1]
# Expected output: 3

# 
# utilized binary search to rec search and count the number of 1's
# in the array in o(logn) time  > o(n)
# Example Input: [1, 0, 0,0, 0, 0, 0, 0, 1, 1]n = 2
#                                         |
# 0 ->  1
# start in the middle to bgin search
# if there is no 1 there:
        # search the right
        
# if there is a 1:
  #      turn to 0
  #      increment n += 1
        #recursive keep searching left

# base case if n == len(arr):
def count_ones(lst):
    left, right = 0, len(lst) - 1
    first_one_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == 1:
            first_one_index = mid
            right = mid - 1        
        else:
            left = mid + 1

    if first_one_index == -1:
        return 0      
    return len(lst) - first_one_index


lst =  [0,0, 0, 0, 1, 1]

print(count_ones(lst))
