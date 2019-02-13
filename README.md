Pretty-prints a binary tree with child fields `left` and `right`. Each node contains a `data` field, which is printed.

Run `python test_nodes.py` and check out the results.

The tree may be of any depth, but usually after 6 levels it's too wide for most screens.

Looks best when the nodes' printed values are under 3 characters long (especially on leaf nodes).

Is now ported to Python 3 (but still Python 2 compatible).

```python
# prep the tree...
#

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

big_node.printTree()


```
                  ______________=______________
                 /                             \
                a                         ______+______
                                         /             \
                                      __*__           __/__
                                     /     \         /     \
                                    2       +       !       6
                                           / \     /
                                          3  12  22