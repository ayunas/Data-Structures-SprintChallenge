class Node:
    def __init__(self,val,next=None):
        self.value = val
        self.next = next
    
    def __repr__(self):
        return repr(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = Node(val)
    
    def prepend(self,val):
        self.head = Node(val,self.head)
    
    def find(self,val):
        n = self.head
        while n and n.value != val:
            n = n.next
        return n
    
    def remove(self,val):
        n = self.head
        
        if self.head.value == val:
            self.head = self.head.next
            return

        while n and n.value != val:
            prev = n
            n = n.next

        print('prev', prev.value, 'n', n.value, 'n.next', n.next.value)
        prev.next = n.next
        n.next = None  #this removes the pointer of the removed n node from memory pointing to any elements in the linked list.  

    def reverse(self):
        #flip the pointers at ever node.
        #define 3 pointers: current, prev, and next
        # while current exists: set next to be current.next.  then set current.next to point to the previous node.  then shift both prev and current to be current and next
        # at the end of the loop, set the head to be the final element after traversing the list.  namely, the prev node, because next is none.  and that was the last thing that current was set to.  prev was set to current in the last iteration
        current = self.head
        prev = None
        next = None

        while current:
            next = current.next #stash next to be actual current.next
            # print('prev', prev.value, 'current', current.value, 'current.next', current.next.value)
            current.next = prev  #flip the next to point to the previous.  
            # print('prev', prev.value, 'current', current.value, 'current.next flipped', current.next.value)
            prev = current #move prev to next node
            current = next #move current to next node
        self.head = prev
        # print('prev', prev.value, 'current', current.value, 'current.next', current.next.value)

    def __repr__(self):
        nodes = []
        n = self.head
        while n:
            nodes.append(repr(n))
            n = n.next
        return '[' + ', '.join(nodes) + ']'

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)

ll.reverse()

print(ll)
























# class Node:
#     def __init__(self,val,next=None):
#         self.value = val
#         self.next = next
    
#     def __repr__(self):
#         return repr(self.value)


# class LinekdList:
#     def __init__(self):
#         self.head = None

#     def append(self,val):

#         if self.head is None:
#             self.head = Node(val)
#         else:
#             n = self.head
#             while n.next:
#                 n = n.next
#             n.next = Node(val)
    
#     def prepend(self,val):
#         # old_head = self.head
#         # self.head = Node(val)
#         # self.head.next = old_head
#         self.head = Node(val,self.head)

    
#     def __repr__(self):
#         nodes = []
#         n = self.head
#         while n:
#             nodes.append(repr(n))
#             n = n.next
#         return '[' + ', '.join(nodes) + ']'
    


# ll = LinekdList()
# n = Node(40)

# ll.append(5)
# ll.prepend(4)
# ll.prepend(3)
# ll.append(6)



# print(ll)






















# class Node:
#     def __init__(self,val,next_node=None):
#         self.value = val
#         self.next = next_node
        

# class LinekdList:
#     def __init__(self,start=None,end=None):
#         self.head = Node(start,end)
#         self.tail = Node(end)
#         self.head.next = self.tail
#         self.length = 0 if not self.head else 1
    
#     def add_to_head(self):
#         pass

#     def add_to_tail(self,val):
#         self.length = self.length + 1

#         if self.head.next is self.tail:
#             new_node = Node(val)
#             self.head.next = new_node
#             new_node.next = self.tail
#             self.tail = new_node
#         else:
#             new_node = Node(val)
            


# ll = LinekdList(20,30)
# # ll.add_to_tail(30)
# print(ll.head.value)
# print(ll.head.next.value)
# print(ll.tail.value)




