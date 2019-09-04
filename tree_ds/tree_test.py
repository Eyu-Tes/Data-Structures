from trees import Tree

tree = Tree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
tree.insert(1)

print()
print(tree.lookup(5))
print(tree.lookup(1))
print(tree.lookup(17))

print('\nInorder ... (Shows real sequence on number line.')
tree.traverse('inorder')
print('\nPreorder')
tree.traverse('preorder')
print('\nPostorder')
tree.traverse('postorder')
print('\nLevelorder')
tree.traverse('levelorder')             # breadth first

print('\n')

removed = tree.remove(4)
print(f'removed : {removed}' if removed is not None else 'Key Not Found!')
print('\nLevelorder')
tree.traverse('levelorder')
