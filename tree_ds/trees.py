# trees - a family hierarchy (Grand Parents, Parents, Children...)
#       - non linear data structure
#       - every node has only 1 parent
#       - nodes can have as many children as they want
#       - 1 root node


# Binary Tree - a tree in which every node has atmost 2 child nodes
#             - Left & Right Children


# Binary Search Tree - a binary tree that satisfy the following conditions:
#   - The key in left child node(if exist) is less then key in its parent node.
#   - The key in right child node(if exist) is greater then key in parent node.
#   - The left and right sub-trees of the root are again binary search trees.
#   - No two entries in a binary search tree may have a equal keys.


# Analogy - Think of binary search tree as a dictionary

class Node:
    # Node class containing key, reference to left & right children
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        # represent a node using this string
        return f'Node->{self.key}'


class Tree:
    # Tree class containing root attribute & other methods
    def __init__(self):
        self.root = None

    @property
    # the @property decorator treats the method as an attribute
    def isempty(self):
        # returns true if tree is empty
        if self.root is None:
            # if root node is None, tree is empty
            return True

    def isleaf(self, node):
        # returns true if the specified node is a leaf in the tree
        if not self.isempty:
            # if tree is not empty
            if node.left is None and node.right is None:
                # if node has no reference to right or left child, it is a leaf
                return True

    def lookup(self, key):
        # returns if a key is found in the tree or not
        current_node = self.root
        found = False
        if not self.isempty:
            # if tree is not empty, continue search until break
            while True:
                if key > current_node.key:
                    # target node is greater than current node
                    if current_node.right is not None:
                        # if right child of current node exists, goto right
                        current_node = current_node.right
                    else:
                        # if not exit while loop (i.e, key not found)
                        break
                elif key < current_node.key:
                    # target node is less than current node
                    if current_node.left is not None:
                        # if left child of current node exists, goto left
                        current_node = current_node.left
                    else:
                        # if not exit while loop (i.e, key not found)
                        break
                else:
                    # target node is equal to current node (i.e, key is found)
                    found = True
                    break

        return 'Key Found!' if found else 'Key Not Found!'

    def insert(self, new_key):
        # inserts a node in the tree
        new_node = Node(new_key)
        if self.isempty:
            # if tree is empty, insert node at the root
            self.root = new_node
            print(f'Inserted {new_key}')
        else:
            current_node = self.root
            while True:
                if new_key > current_node.key:
                    # target node is greater than current node
                    if current_node.right is None:
                        # if right child of current node doesn't exist,
                        # insert the new node to the right
                        current_node.right = new_node
                        print(f'Inserted {new_key}')
                        break
                    # if right child of current node exists, goto right
                    current_node = current_node.right
                elif new_key < current_node.key:
                    # target node is less than current node
                    if current_node.left is None:
                        # if left child of current node doesn't exist,
                        # insert the new node to the left
                        current_node.left = new_node
                        print(f'Inserted {new_key}')
                        break
                    # if left child of current node exists, goto left
                    current_node = current_node.left
                else:
                    # target node is equal to current node
                    # node can't be inserted (no duplicate key allowed)
                    print('Key Exists!')
                    break

    def remove(self, key):
        # removes & returns node from a tree
        removed = None
        if self.isempty:
            # tree is empty (i.e, nothing to remove)
            print('Nothing to Remove!')
        else:
            # if not continue search for target node until break
            current_node = self.root
            parent_node = None
            while True:
                if key < current_node.key:
                    # target node is less than current node
                    if current_node.left:
                        # if left child of current node exists, goto left
                        # but 1st make a reference to current node (parent)
                        parent_node = current_node
                        current_node = current_node.left
                    else:
                        # left child doesn't exist (i.e, key not found)
                        break
                elif key > current_node.key:
                    # target node is greater than current node
                    if current_node.right:
                        # if right child of current node exists, goto right
                        # but 1st make a reference to current node (parent)
                        parent_node = current_node
                        current_node = current_node.right
                    else:
                        # right child doesn't exist (i.e, key not found)
                        break
                else:
                    # target node is equal to current node (i.e, node is found)
                    if self.isleaf(current_node):
                        # if target node is leaf, just remove it
                        removed = current_node.key
                        if current_node == parent_node.left:
                            # target node is a left child of its parent,
                            # make its parent's left pointer None
                            parent_node.left = None
                        elif current_node == parent_node.right:
                            # target node is a right child of its parent,
                            # make its parent'e right pointer to None
                            parent_node.right = None
                    else:
                        # if target node is not a leaf, replace it with a node
                        # a replacement node is always a leaf node
                        # we have 2 options for replacement
                        # 1. replacment node is left most node of right sub tree
                        replacement_node = self.get_leftmost(current_node.right)
                        # If there is no right sub tree,
                        # There will be left subtree since current node is not a leaf
                        if replacement_node is None:
                            # 2. replacment node is right most node of left sub tree
                            replacement_node = self.get_rightmost(current_node.left)
                        replacement_key = replacement_node.key
                        # now remove the replacement node from its leaf position
                        self.remove(replacement_node.key)
                        removed = current_node.key
                        # replace key of removed node with the replacement node
                        current_node.key = replacement_key
                    break
        return removed

    def get_leftmost(self, node):
        # returns the left most node for a given sub tree
        if node is not None:
            # if specified node exists, continue iteration until break
            current_node = node
            while True:
                if current_node.left is not None:
                    # if node has left child, goto left
                    current_node = current_node.left
                else:
                    # if not return node
                    return current_node

    def get_rightmost(self, node):
        # returns the right most node for a given sub tree
        if node is not None:
            # if specified node exists, continue iteration until break
            current_node = node
            while True:
                if current_node.right is not None:
                    # if node has right child, goto right
                    current_node = current_node.right
                else:
                    # if not return node
                    return current_node

    def traverse(self, traversal_type):
        # prints nodes in a tree based on the traversal type
        if self.root is not None:
            if traversal_type == 'inorder':
                self.inorder(self.root)
            if traversal_type == 'preorder':
                self.preorder(self.root)
            if traversal_type == 'postorder':
                self.postorder(self.root)
            if traversal_type == 'levelorder':
                self.levelorder(self.root)
        else:
            print('Tree is Empty!')

    def inorder(self, node):
        # depth-first LPR search

        if node.left is not None:
            # if node has left child, goto left recursively
            self.inorder(node.left)
        # print key inside node
        print(node.key, end="\t")
        if node.right is not None:
            # if node has right child, goto right recursively
            self.inorder(node.right)

    def preorder(self, node):
        # depth-first PLR search

        # print key inside node
        print(node.key, end="\t")
        if node.left is not None:
            # if node has left child, goto left recursively
            self.preorder(node.left)
        if node.right is not None:
            # if node has right child, goto right recursively
            self.preorder(node.right)

    def postorder(self, node):
        # depth-first LRP search

        if node.left is not None:
            # if node has left child, goto left recursively
            self.postorder(node.left)
        if node.right is not None:
            # if node has right child, goto right recursively
            self.postorder(node.right)
        # print key inside node
        print(node.key, end="\t")

    def levelorder(self, node, children=None):
        # breadth-first search

        if node is not None:
            # if node exists, print its key
            print(node.key, end="\t")
            if children is None:
                children = []
            # append the node's children to a list
            children += [node.left, node.right]
        if children:
            # if there is/are children,
            # call ur self by passing 1st child & remaining children separately
            self.levelorder(children[0], children[1:])
