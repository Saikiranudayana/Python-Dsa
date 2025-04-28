##Take input of linjked list


##return a head to bnewly created linked list

class Node:
    def __init__(self,value):
        self.data = value
        self.next= None
        
def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data,end="-->")
        temp = temp.next
        
    return 
def take_input_better():
    value = int(input("Enter a number"))
    head = None
    tail = None
    
    while value != -1:
        newNode= Node(value)
        if head==None:
            head = newNode
            tail = newNode
            
        else:
            tail.next = newNode
            tail = newNode
            
           
           
        
            
            
        value = int(input("Enter the value of node"))
    return head



##Take input of linjked list


##return a head to bnewly created linked list

class Node:
    def __init__(self,value):
        self.data = value
        self.next= None
        
def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data,end="-->")
        temp = temp.next
        
    return 
def take_input():
    value = int(input("Enter a number"))
    head = None
    
    while value != -1:
        newNode= Node(value)
        if head==None:
            head = newNode
            
        else:
            temp = head 
            while (temp.next != None):
                temp = temp .next
            
            temp.next = newNode
            
        value = int(input("Enter the value of node"))
    return head




def createLLfromlist(l1):
    head= None
    tail = None
    for value in l1:
        newnode= Node(value)
        if head==None:
            head= newnode
            tail = newnode
        else:
            tail.next= newnode
            tail = newnode
    return head

def lengthofll(head):
    temp = head
    ans = 0
    while (temp !=None):
        temp = temp.next
        ans = ans +1
    return ans