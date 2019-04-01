Pretty-prints a binary tree with nodes with two child fields and a data field.
You can use it as method in your code like this: 
```
import tree_pprint

class my_node:
    def printTree(self):
        tree_pprint.pprint(self, your_data_attr_name, your_left_attr_name, 
                           your_right_attr_name)

[...]

root_node = my_node(val)

root_node.printTree()
```

or as extern method:
```
import tree_pprint

tree_pprint.pprint(root_node, your_data_attr_name, your_left_attr_name, 
                   your_right_attr_name)
```


You can find an example code in the `test_nodes.py` or run `python test_nodes.py` and check out the results.

The tree may be of any depth, but usually after 6 levels it's too wide for most screens.

Looks best when the nodes' printed values are under 3 characters long (especially on leaf nodes).

I've deleted the methods which generates a tree so this is just for pretty printing your own tree. Thanks to the `..._attr_name` attributes you can name the attributes of you node class however you want. Just make sure to put the right names in there and then it will do the work for you.

I've ported it to Python 3 (but it's still Python 2 compatible).

Here is a little example what it can do:

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
