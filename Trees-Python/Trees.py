import json

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTree(root):
    if root is not None:
        inOrderTree(root.left)
        print(root.data, end=" ")
        inOrderTree(root.right)

def postOrderTree(root):
    if root is not None:
        postOrderTree(root.left)
        postOrderTree(root.right)
        print(root.data, end=" ")

def build_sample_tree():
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

    return root

def tree_to_json(node):
    if node is None:
        return None
    return json.dumps({
        "name": node.data,  # Use "name" for better compatibility with tree templates
        "children": list(filter(None, [tree_to_json(node.left), tree_to_json(node.right)]))
    })

root = build_sample_tree()

# #visualize tree_to_json(root)
inOrderTree(root)
postOrderTree(root)
vis = tree_to_json(root)