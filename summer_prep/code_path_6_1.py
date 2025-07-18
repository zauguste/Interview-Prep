# # Problem 6: Volume Control
# # You are working as an engineer normalizing volume
# #  levels on songs. Given the head of a singly linked 
# # list with integer values song_audio representing volume
# #  levels at different points in a song, return the number
# #  of critical points. A critical point is a local 
# # minima or maxima.

# # Given the head of a singly linked list 
# # return the number of critical points 
# # 
# # The head and tail nodes are not considered critical points.
# # A node is a local minima if both the next and previous elements are greater than the current element
# # A node is a local maxima if both the next and previous elements are less than the current element
# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
# # for why you believe your solution has the stated time and space complexity.
# # prev = Node()
# # if .next.val > current.val and .prev.val > current.val:
#     # local minima
# # elif .next.val < current.val and .prev.val < current.val:
#     # local maxima

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
	
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def count_critical_points(song_audio):
#     current = song_audio.next
#     prev = song_audio
#     count = 0
#     while current.next:
#         if current.next.value > current.value and prev.value > current.value:
#             count += 1
#         if current.next.value < current.value and prev.value < current.value:
#             count += 1
#         prev = current
#         current = current.next
#     return count
# # elif .next.val < current.val and .prev.val < current.val:
#     # local maxima		current = current.next
# # Example Usage:

# # song_audio linked list

# song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

# print(count_critical_points(song_audio))
# # Example Output:

# # 3
# # Explanation: There are three critical points:
# # - The third node is a local minima because 1 is less than 3 and 2.
# # - The fifth node is a local maxima because 5 is greater than 2 and 1.
# # - The sixth node is a local minima because 1 is less than 5 and 2.
# # 💡 Hint: Which technique?
# # Standard

# Problem 4: Turn Back Time
# A spell gone wrong has reversed time! Write a function reverse() that accepts the head of a singly linked list events 
# and restores order by reversing the order of elements. Return the head of the reversed list.

# reverse the order of elements
# the return the new head
# none>1>2>3>4>None
# prev = none
# start at the head
# traverse the linked list
#   before going to the next element 
#   change its next pointer to the previous address
# store prev in variable
# continue to next

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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

def reverse(events):
    prev = None#none
    current = events#Potion Brewing.next -> none
    hold = None#none
    while current:#true,true,true,true,false
        hold = current.next#spell casting,Wand Making,Dragon Taming,broomstick flying,None
        current.next = prev#none,Potion Brewing,spell casting,wand making,dragon taming
        prev = current#Potion Brewing,spell casting,wand making,dragon taming, = broomstick flying
        current = hold#spell casting,Wand Making,Dragon Taming,broomstick flying.next, None
    return prev #broomstick flying
# Example Usage:
events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))
# Example Output:
        # prev = current#Potion Brewing,spell casting,wand making,dragon taming, = broomstick flying

# Broomstick Flying -> Dragon Taming -> Wand Making -> Spell Casting -> Potion Brewing

