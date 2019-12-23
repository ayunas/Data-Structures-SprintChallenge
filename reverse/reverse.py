# Node - get_value , get_next, set_next
# LinkedList - add_to_head, contains, reverse_list

class Node:
  def __init__(self,val, next=None):
    self.value = val
    self.next = next
  
  def get_value(self):
    return self.value
  
  def get_next(self):
    return self.next
  
  def set_next(self,new_node):
    self.next = new_node

  def __repr__(self):
    return repr(self.value)

class LinkedList:
  def __init__(self):
    self.head = None
  
  def prepend(self,val): #add_to_head
    self.head = Node(val,self.head)
  
  def append(self,val):  #add_to_tail
    if self.head is None:
      self.head = Node(val)
    else:
      n = self.head
      while n.next:
        n = n.next
      n.next = Node(val)
    
  def contains(self,val):
    n = self.head
    while n:
      if n.value == val:
        return True
      n = n.next
    return False
  
  def __repr__(self):
    nodes = []
    n = self.head
    while n:
      nodes.append(repr(n))
      n = n.next
    return '[' + ', '.join(nodes) + ']' if len(nodes) else '[]'


# n = Node(10,Node(20))

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll.contains(21))

print(ll)



















# class Node:
#   def __init__(self, value=None, next_node=None):
#     # the value at this linked list node
#     self.value = value
#     # reference to the next node in the list
#     self.next_node = next_node

#   def get_value(self):
#     return self.value

#   def get_next(self):
#     return self.next_node

#   def set_next(self, new_next):
#     # set this node's next_node reference to the passed in node
#     self.next_node = new_next

# class LinkedList:
#   def __init__(self):
#     # reference to the head of the list
#     self.head = None

#   def add_to_head(self, value):
#     node = Node(value)
#     if self.head is not None:
#       node.set_next(self.head)
    
#     self.head = node

#   def contains(self, value):
#     if not self.head:
#       return False
#     # get a reference to the node we're currently at; update this as we traverse the list
#     current = self.head
#     # check to see if we're at a valid node 
#     while current:
#       # return True if the current value we're looking at matches our target value
#       if current.get_value() == value:
#         return True
#       # update our current node to the current node's next node
#       current = current.get_next()
#     # if we've gotten here, then the target node isn't in our list
#     return False

#   def reverse_list(self):
#     # TO BE COMPLETED
#     pass


# l = LinkedList()
# l.add_to_head(10)
# l.add_to_head(20)
# l.add_to_head(30)

# print(l.head.next_node.next_node.value)
# print(l.head.next.value)


