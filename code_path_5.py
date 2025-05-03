# Problem Set Version 1
# Problem 1: Pokemon Class
# Step 1: Copy the following code into Replit.

# Step 2: Add a line of code (outside of the class) to instantiate an instance of the class 
# Pokemon and store it in a variable named my_pokemon. The Pokemon instance created should have name 
# "Pikachu" and its types should be ["Electric"].

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

# my_pokemon = Pokemon("Pickachu",["Electric"])
# # 💡 Hint: Intro to Object Oriented Programming
# print(my_pokemon.types)
# print(my_pokemon.name)
# Problem 2: Create Squirtle
# Step 1: Add the print_pokemon definition below to your code on Replit.

# Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. 
# The Pokemon instance created should have name "Squirtle" 
# and its types should be ["Water"].

# Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })
# # 💡 Hint: Class Methods




# # first lets instatiat Pokemon and call it by storing it in a variable pokemon

# # pokemon = Pokemon()
# # pokemon.print_pokemon
# Squirtle = Pokemon("Squirtle",["Water"])
# Squirtle.print_pokemon()


# Problem 3: Is Caught
# Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. 
# Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

# Expected Output:

# {
#     "name": "Squirtle",
#     "types": ["Water"],
#     "is_caught": True
# }
# 💡 Hint: Class Attributes

# Problem 4: Catch Pokemon
# Update the Pokemon class with a new method catch() that takes in no parameters except self.

# The method should update the Pokemon's is_caught attribute to True and not return any value.

# class Pokemon():
# 	...
	
# 	def catch(self):
# 		pass
# Example Usage:

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()
# Example Output:

# {
#     "name": "Rattata",
#     "types": ["Normal"],
#     "is_caught": False
# }

# {
#     "name": "Rattata",
#     "types": ["Normal"],
#     "is_caught": True
# }
# 💡 Hint: Writing Methods

# Problem 5: Choose Pokemon
# Update the Pokemon class with a new method choose() that takes in no parameters except self.

# If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

# Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

# class Pokemon():
# 	...
	
# 	def choose(self):
# 		pass
# Example Usage:

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()
# Example Output:

# {
#     "name": "Rattata",
#     "types": ["Normal"],
#     "is_caught": False
# }

# Rattata is wild! Catch them if you can!
# Rattata I choose you!

# Problem 6: Add Pokemon Type
# Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

# It should add new_type to the Pokemon's list of types.

# class Pokemon():
# 	...
	
# 	def add_type(self, new_type):
# 		pass
# Example Usage:

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()
# Example Output:

# {
#     "name": "Jigglypuff",
#     "types": ["Normal"]
#     "is_caught": False
# }

# {
#     "name": "Jigglypuff",
#     "types": ["Normal", "Fairy"]
#     "is_caught": False
# }

# Problem 7: Get Pokemon
# Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

# The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

# Hint: To test, loop over Pokemon in return list and print the Pokemon's name

# class Pokemon():
# 	...
	
# def get_by_type(my_pokemon, pokemon_type):
# 	pass
# Example Usage:

# # initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)
# Example Output: [jigglypuff, meowth, pidgeot]


# Problem 8: Pokemon Evolution
# Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

# Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

# The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.

# class Pokemon():
# 	def  __init__(self, name, types, evolution = None):
# 		self.name = name
# 		self.types = types
# 		self.is_caught = False
# 		self.evolution = evolution
 
# def get_evolutionary_line(starter_pokemon):
# 	pass
# Example Usage:

# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)
# Example Output:

# [`Charmander`, `Charmeleon`, `Charizard`]
# [`Charmeleon`, `Charizard`]
# ['Charizard']


# Problem 9: Node Class
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create two nodes:

# The first node should have value a and be stored in a variable node_one.
# The second node should have value b and be stored in a variable node_two.
# You do not need to connect the nodes together yet.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# Example Usage:

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next) 
# Example Output:

# a
# None
# b
# None
# 💡 Hint: Intro to Linked Lists

# Problem 10: Linking Nodes
# Building off the Node class from Problem 9, now we will link the nodes together.

# To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.

# Example Usage (after updating node_one's next property):

# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)
# Example Output:

# a
# b
# b

# Problem 11: Mario Party
# Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# Result Linked List would be: Mario -> Luigi -> Wario -> Toad

# Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):
node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")


node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
# Example Output:

# Mario -> Luigi
# Luigi -> Wario
# Wario -> Toad
# Toad -> None

# Problem 12: Printing Linked List
# Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.

# Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next= next
		
# def print_linked_list(head):
# 	while head:
# 		print(head.cur)
# 		head = head.next

# # # input linked list: a->b->c->d->e
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# print_linked_list(a)
# # Example Output:

# # a -> b -> c -> d -> e