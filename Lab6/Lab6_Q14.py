"""Finally, you hit the big time. Now you have to write a 
function huffman_tree(frequencies) that takes a dictionary mapping characters 
to their frequencies and return a Huffman Coding tree represented using the Node
and Leaf classes given in the previous examples (or extensions of those 
classes - see below). You are required to follow the algorithm in the lecture
notes, noting particularly how two trees are ordered when their root frequencies
are identical.

The lecture notes explain how a priority queue can be used to ensure O(n log n) 
performance. The Python heapq module can be used to provide a priority 
queue - read the documentation. However, while you are encouraged to use a 
priority queue you may if you wish simply use a list of (sub)trees, and sort 
the list at each stage to find the two lowest frequency trees. That gives a much
inferior O(n2logn) algorithm but is fine for smallish character sets like ASCII.

Managing the ordering of trees with equal frequency is a bit tricky. 
One approach is to extend both the Node and Leaf classes to include a min_char
attribute. For a Leaf, this is just its char attribute. For a Node it can be 
passed in as an extra parameter when building new nodes. Provided you don't 
modify the __str__ methods of the Node and Leaf classes, your code will still 
pass the tests, as it is only the string representation of the returned tree 
that is being tested.
"""

import heapq 

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count
       and left and right subtrees, assumed to be the '0' and '1' children
       respectively.
    """
    def __init__(self, count, left, right, min_char):
        self.count = count
        self.left = left
        self.right = right
        self.min_char = min_char

    def __str__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__str__(level + 1) + ',\n' +
            self.right.__str__(level + 1) + ')')

    def is_leaf(self):
        return False

class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __str__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True
    
def huffman_tree(frequencies):
    alist = []
    for char, count in frequencies.items():
        new_leaf = Leaf(count, char)
        alist.append((new_leaf.count, new_leaf.char, new_leaf))
    heapq.heapify(alist)
    if len(alist) < 2:  #for base case when there is only 1 leaf
        return new_leaf
    while len(alist) != 1:
        var1 = heapq.heappop(alist)
        var2 = heapq.heappop(alist)
        min_char = min(var1[1], var2[1])
        new_tree = Node(var1[0] + var2[0], var1[2], var2[2], min_char)
        heapq.heappush(alist, (new_tree.count, min_char, new_tree)) #use heappush to maintain the heap order
    return new_tree


## The example from the notes
#freqs = {'p': 27,
         #'q': 11,
         #'r': 27,
         #'u': 8,
         #'t': 5,
         #'s': 3}
#print(huffman_tree(freqs))

## The example from the notes
#freqs = {'a': 9,
         #'b': 8,
         #'c': 15,
         #'d': 3,
         #'e': 5,
         #'f': 2}
#print(huffman_tree(freqs))

print(huffman_tree({'x': 1000}))