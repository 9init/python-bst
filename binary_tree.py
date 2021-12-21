class Node():
  def __init__(self, data):
    self.data  = data
    self.left  = None
    self.right = None
  
def insert(node, data):
  if(node == None):
    return Node(data)
  else:
    if(node.data < data):
      return insert(node.right, data)
    else:
      return insert(node.left, data)
      
      
def print_in_order(node):
  if(node == None):
    return
    
  print_in_order(node.left)
  print(node.data)
  print_in_order(node.right)
  
def print_pre_order(node):
  if(node == None):
    return
    
  print(node.data)
  print_pre_order(node.left)
  print_pre_order(node.right)
  
def print_post_order(node):
  if(node == None):
    return
    
  print_post_order(node.left)
  print_post_order(node.right)
  print(node.data)
  
def size(node):
  if(node == None):
    return 0
  else:
    return (1 + size(node.left) + size(node.right))
    

def minValue(node):
  current = node
  
  while(current.left != None):
    current = current.left
    
  return current.data
  
  
def main():
  head = None
  
  head       = insert(head, 2)
  head.left  = insert(head, 1)
  head.right = insert(head, 3)
  
  print("The size of the binary search tree is %d" % size(head))
  print("The smallest value in the binary search tree is %d" % minValue(head))
  
  print("Print In order")
  print_in_order(head)
  
  print("Print pre order")
  print_pre_order(head)
  
  print("Print post order")
  print_post_order(head)
  
  
if __name__ == '__main__':
  main()
  
  
  
    
