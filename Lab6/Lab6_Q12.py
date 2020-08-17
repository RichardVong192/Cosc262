"""
Write a function huffman_decode(s, tree) that takes a string s of zeros and ones
and a Huffman Coding tree tree. It is assumed that the string s has been encoded
using the given tree and this function must decode it again to yield the 
original string.


The Huffman Coding tree is represented using two classes Node (which represents
an internal node in a Huffman encoding tree) and Leaf (which represents a leaf 
node). It is assumed that the edge from a parent to its left child node is 
labelled '0' and to its right child node '1'. The Node and Leaf classes have
been preloaded into the answer box. You should not need to alter them. 
"""

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count
       and left and right subtrees, assumed to be the '0' and '1' children
       respectively.
    """
    def __init__(self, count, left, right):
        self.count = count
        self.left = left
        self.right = right

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

    def __str__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True
    

def huffman_decode(s, tree):
    result = []
    alist = list(s)
    new_tree = tree
    for i in range(len(alist)):
        if int(alist[i]) == 0:
            new_tree = new_tree.left
            if new_tree.is_leaf():
                result.append(new_tree.char)
                new_tree = tree 
        else:
            new_tree = new_tree.right
            if new_tree.is_leaf():
                result.append(new_tree.char)
                new_tree = tree
    str1 = ''.join(result)
    return str1

    
# The example from the lecture notes
tree = Node(42,
  Node(17,
    Leaf(8, 'b'),
    Leaf(9, 'a')),
  Node(25,
    Node(10,
      Node(5,
        Leaf(2, 'f'),
        Leaf(3, 'd')),
      Leaf(5, 'e')),
    Leaf(15, 'c')))
print(huffman_decode('0110011100', tree))