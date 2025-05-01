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
    
    
    
    