# Problem 3: Prioritizing Suspects
# You've identified a list of suspect, but time is limited and '
# 'you won't be able to question all of them today. 
# Write a function partition() to help prioritize the order in 
# which you question suspects. Given the head of a linked list of 
# integers suspect_ratings, where each integer represents the
# suspiciousness of the a given suspect and a value threshold, 
# partition the linked list such that all nodes with values greater 
# than threshold come before nodes with values less than or equal
# to threshold.

# Return the head of the partitioned list.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you 
# believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
	pass
# Example Usage:

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))
# Example Output:

# 4 -> 5 -> 1 -> 3 -> 2 -> 2
# Explanation: 
# Note that nodes 4 and 5 can be in any order in the result list so long as they come before
# 3, 2, and 1. 
# Similarly, 3, 2, and 1 can come in any order so long as they are after 4 and 5. 
# 5 -> 4 -> 3 -> 1 -> 2 -> 2 would also be a possible acceptable answer
