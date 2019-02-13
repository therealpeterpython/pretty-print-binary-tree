# Example of how to use tree_pprint
#
# 13.02.2019 by therealpeterpython

import tree_pprint as tree_pprint

class my_node:
    def __init__(self, own = None, left = None, right = None, parent = None):
        self.own = own
        self.left = left
        self.right = right
        self.parent = parent

    def printTree(self):
        tree_pprint.pprint(self, "own")
    
    

if __name__ == '__main__':
    # prep the tree...
    #
    # root: 2 *(3+12) + !22 / 66
    # big_node: a = 2 *(3+12) + !22 / 66

    # layer 1
    root = my_node('+')

    # layer 2
    root.left = my_node('*')
    root.right = my_node('/')

    # layer 3
    root.left.left = my_node('2')
    root.left.right = my_node('+')
    root.right.left = my_node('!')
    root.right.right = my_node('6')

    # layer 3
    root.left.right.left = my_node('3')
    root.left.right.right = my_node('12')
    root.right.left.left = my_node('22')

    big_node = my_node("=",my_node("a"),root)

    #root.printTree()
    #print("\n\n")
    big_node.printTree()
  
  