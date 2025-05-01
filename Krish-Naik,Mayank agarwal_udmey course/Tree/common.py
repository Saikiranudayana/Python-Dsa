
##p[rint function
class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        
        








# print(root.children[0].data)


def print_tree(root):
    if root==None:
        return
    
    print(root.data)
    for child in root.children:
        print_tree(child)
        
# print_tree(root)


def print_tree_detailed(root):
    if root==None:
        return 
    print(root.data,end = ":")
    for child in root.children:
        print(child.data,end = ",")
    print()
    for child in root.children:
        print_tree_detailed(child)

