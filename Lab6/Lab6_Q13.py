"""
Write a function huffman_encode(s, huffman_tree) which is given a string s and a
Huffman Coding tree and returns a string containing the binary sequence of 0s 
and 1s that represents the Huffman-encoded string s.

The Node and Leaf classes have been preloaded into the answer box. You should 
not need to alter them. Simply add your huffman_encode function. You may assume
all characters in the string s are leaves in the tree.
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

def huffman_encode_pp(bin_str, huffman_tree, tree_dict):
    if huffman_tree.is_leaf():
        tree_dict[huffman_tree.char] = bin_str
    else:
        huffman_encode_pp(bin_str + str(0), huffman_tree.left, tree_dict)
        huffman_encode_pp(bin_str + str(1), huffman_tree .right, tree_dict)
    
def huffman_encode(s, huffman_tree):
    tree_dict = {}
    result = ''
    huffman_encode_pp('', huffman_tree, tree_dict)
    for char in s:
        x = tree_dict.get(char)
        result += x
    return result
        
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
print(huffman_encode('adcb', tree))