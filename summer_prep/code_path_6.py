# Problem 3: Glitching Out
# The following code attempts to remove the first node with a given
#  song from a singly linked list with head playlist_head but it contains a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, 
# and use print statements and the stack trace to identify and
#  fix the bug so that the function correctly removes a node by value from the list.

# Step 3: Evaluate the time and space complexity of the fixed solution.
#  Define your variables and provide a rationale for why you believe the 
# solution has the stated time and space complexity.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

# remove bob dylan
# Function with a bug!
def remove_song(playlist_head, song): #('SOS', 'ABBA'),  "Dreams"
    if not playlist_head: #('SOS', 'ABBA') we do so continue
        return None
    if playlist_head.song == song:#SOS != Dreams so continue
        return playlist_head.next

    current = playlist_head #('SOS', 'ABBA')
    while current.next:#('SOS', 'ABBA') - > ('Simple Twist of Fate', 'Bob Dylan') (yes a next exit), SongNode("Dreams", "Fleetwood Mac") -> (SongNode("Lovely Day", "Bill Withers"))(yes it has a next)
        if current.next.song == song:  #is ('Simple Twist of Fate' == Dreams)(no continue), SongNode("Dreams") == "Dreams"? yes,
            current = current.next.next #SongNode("Dreams") = SongNode("Lovely Day", "Bill Withers")
            return playlist_head
        current = current.next #current = SongNode("Simple Twist of Fate", "Bob Dylan")

    return playlist_head
# Example Usage:

playlist = SongNode("SOS", "ABBA", SongNode("Simple Twist of Fate", "Bob Dylan", SongNode("Dreams", "Fleetwood Mac", SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))
# Expected Output:

# ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')

