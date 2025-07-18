# # # # Breakout Problems Session 1
# # # # Standard Problem Set Version 1
# # # # Problem 1: New Horizons
# # # # Step 1: Copy the following code into your IDE.

# # # # Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# # # # The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
# # class Villager:
# #     def __init__(self, name, species, catchphrase):
# #         self.name = name
# #         self.species = species
# #         self.catchphrase = catchphrase
# #         self.furniture = []


# #     def greet_player(self, player_name):
# #         return f"Hey there, {player_name}! How's it going, ruff it up!"

# # # # u: given villager request, instatiate in the name applo variable
# # # # 
# # # apollo = Villager("Apollo","Egale","pah")
# # bones = Villager("Bones","Dog","yip yip")
# # print(bones.greet_player("Zion")
# # )

# # # # # Instantiate your villager here
# # # # Example Usage:

# # # print(apollo.name)  
# # # print(apollo.species)  
# # # print(apollo.catchphrase) 
# # # print(apollo.furniture) 
# # # # Example Output:

# # # # Apollo
# # # # Eagle
# # # # pah
# # # # []

# # # Problem 2: Greet Player
# # # Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

# # # Step 2: Create a second instance of Villager in a variable named bones.

# # # The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
# # # Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

# # # Example Usage:

# # print(bones.name)
# # print(bones.species)  
# # print(bones.catchphrase) 
# # print(bones.furniture) 
# # # Example Output:

# # # Bones
# # # Dog
# # # yip yip
# # # []
# # print(bones.greet_player("Samia"))



# # Problem 4: Set Character
# # In the previous exercise, we accessed and modified a player’s catchphrase attribute directly.
# #  Instead of allowing users to update their player directly, it is common to create setter methods that users
# #  can call to update class attributes. This has a few different benefits, including allowing us to 
# # validate data before updating our class instance.

# # Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

# # If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
# # Otherwise, it should print out "Invalid catchphrase".
# # Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

#     def set_catchphrase(self, new_catchphrase):

#         if len(new_catchphrase) < 20 and new_catchphrase.replace(' ', '').isalpha():

#             self.catchphrase = new_catchphrase

#             print("Catchphrase Updated!")

#         else:

#             print("Invalid catchphrase")

        
#         # understand:
#         # we need to validate if a catchphrase should be updated

#         # if catchphrase has a length < 20:
#             # go through the length of catch phrase and check if a digit 1 - 9 is present:
#             # if true :
#             #     self.catchphrase = new_catchphrase
#             # else:
#             #     print("Invalid catchphrase".)
        
# # Example Usage:

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)
# # Example Output:

# # Example 1:
# # Catchphrase Updated!
# # sweet dreams
# # Invalid catchphrase
# # sweet dreams





# # Problem 5: Add Furniture
# # Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

# # Update the Villager class with a new method add_item() that takes in one parameter, item_name.

# # The method should validate the item_name.

# # If the item is valid, add item_name to the player’s furniture attribute.
# # The method does not need to return any values.
# # item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".

# # class Villager:
# #     # ... methods from previous problems
	
# #     # New method
# #     def add_item(self, item_name):
# #         pass
# # Example Usage:

# # alice = Villager("Alice", "Koala", "guvnor")
# # print(alice.furniture)

# # alice.add_item("acoustic guitar")
# # print(alice.furniture)

# # alice.add_item("cacao tree")
# # # print(alice.furniture)

# # # alice.add_item("nintendo switch")
# # # print(alice.furniture)
# # # Example Output:

# # # []
# # # ["acoustic guitar"]
# # # ["acoustic guitar", "cacao tree"]
# # # ["acoustic guitar", "cacao tree"]
# # # session 2 
# # # In the Villager class below, each villager has a 
# # # friends attribute, which is a list of other villagers 
# # # they are friends with.

# # # Write a method get_mutuals() that takes one parameter, a 
# # # Villager instance new_contact, and returns a list with 
# # # the name of all friends the current villager and 
# # # new_contact have in common.

# # class Villager:
# #     def __init__(self, name, species, catchphrase):
# #         self.name = name
# #         self.species = species
# #         self.catchphrase = catchphrase
# #         self.friends = []

# #     def get_mutuals(self, new_contact):
# #         for i in new_contact:
# #             self.friends.append(i)
        

# # # Example Usage:

# # bob = Villager("Bob", "Cat", "pthhhpth")
# # marshal = Villager("Marshal", "Squirrel", "sulky")
# # ankha = Villager("Ankha", "Cat", "me meow")
# # fauna = Villager("Fauna", "Deer", "dearie")
# # raymond = Villager("Raymond", "Cat", "crisp")
# # stitches = Villager("Stitches", "Cub", "stuffin")

# # bob.friends = [stitches, raymond, fauna]
# # marshal.friends = [raymond, ankha, fauna]
# # print(bob.get_mutuals(marshal))

# # ankha.friends = [marshal]
# # print(bob.get_mutuals(ankha))

# Problem 2: Linked Up
# A linked list is a data structure that, similar to a 
# normal list or array, allows us to store pieces of data 
# sequentially. The key difference is how the elements are 
# stored in memory.

# In a normal list, elements are stored in adjacent memory 
# locations. If we know the location of the first element,
# we can easily access any other element in the list.

# In a linked list, individual elements, called nodes, 
# are not stored in sequential memory locations. 
# # Instead, each node stores a reference or pointer to the 
# # next node in the list, allowing us to traverse the list.

# # Connect the provided node instances below to create the
# # linked list kk_slider -> harriet -> saharah -> isabelle.

# # A function print_linked_list() which accepts the head, 
# # or first element, of a linked list and prints the values
# # of the list has also been provided for testing purposes.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# # Add code here to link the above nodes
# # Example Usage:

# print_linked_list(kk_slider)
# # Example Output:

# # K.K. Slider -> Harriet -> Saharah -> Isabelle
# # ✨ AI Hint: Linked Lists




# Problem 1: Greatest Node
# Write a function find_max() that takes in the head of 
# a linked list and returns the maximum value in the linked list.
# You can assume the linked list will contain only numeric values.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution
# has the stated time and space complexity.

# UNDERSTAND
# we are taking the head of a LL & returning the max integer in the LL
# Linked List: 5 -> 8 -> 6 -> 7 -> None
#          max 8|          current |
# PLAN
# We will traverse the linkedList: while current not none
#   start at head
#   compare the current value to the max value
#   if the current > max:  repeat
        # max = current
#   current = head.next
#   end when head or current is None
# Implement



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

def find_max(head) -> int:
    maxi = 0
    current = head
    while current:
        if current.value > maxi:
            maxi = current.value
        current = current.next
    return maxi
# Example Usage:

head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))
# Expected Output:

# 8
# 8
# 💡 Hint: Linked List Traversal
