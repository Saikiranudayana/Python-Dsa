class GenricTree:
    def __init__(self,data):
        self.data = data
        self.children = []
        
def predefineed_genric_tree_inputs():
    root1 = GenricTree(1)
    child1 = GenricTree(2)
    child2 = GenricTree(3)
    
    root1.children.append(child1)
    root1.children.append(child2)
    
    child1.children.append(GenricTree(4))
    child1.children.append(GenricTree(5))
    
    
    root2 = GenricTree(10)
    child1 = GenricTree(20)
    child2 = GenricTree(30)
    child3 = GenricTree(40)
    root2.children.append(child1)
    root2.children.append(child2)
    root2.children.append(child3)
    child1.children.append(GenricTree(4))
    child1.children.append(GenricTree(5))
    
    
    return root1,root2


def preorder_traversl(root):
    if root is None:
        return 
    print(root.dat,end="")
    for eachchild in root.children:
        preorder_traversl(eachchild)
        
def post_order(root):
    if root is None:
        return 
    
    for eachchild in root.children:
        post_order(eachchild)
        
    print(root.data,end=" ")
        


root1,root2 = predefineed_genric_tree_inputs()
print(preorder_traversl())



root1,root2 = predefineed_genric_tree_inputs()
print(post_order())