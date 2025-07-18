# Problem 3: Find All Duplicate Treasure Chests in an Array

# Captain Blackbeard has an integer array chests of length n 
# where all the integers in chests are in the range [1, n] and each integer appears once or twice. 
# Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

# notes:
# we basically want to return a list containing the duplicates that we have found
# and we may acomplish this with a set to check for duplicates and add the ununique elements to the empty list
#  and return the list containing those elements

# plan:
#  1.start create a set and an empty list
# 2. loop through the chest:
        # check if the element we are on in set:
                # add to the list
        # else:
            # add to the set and continue to the next iteration 
#end 3. return the list
# o(n) time operation because we looped through once and o(n) space because we stored 2 list with worst case length of n elements 


def find_duplicate_chests(chests):
    numSet = set()
    numList = []
    for elements in chests:
        if elements in numSet:
            numList.append(elements)
        numSet.add(elements)
    return numList

# Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
# Example Output:

# [2, 3]
# [1]
# []
