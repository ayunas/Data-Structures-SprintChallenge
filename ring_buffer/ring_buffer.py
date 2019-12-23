from doubly_linked_list import DoublyLinkedList
'''
adding values to the buffer, check the capacity. if capacity is not reached, simply add to the tail of the storage (doubly linked list). if capacity is reached, remove the head of the storage and then add to the tail."
'''
# dll = DoublyLinkedList()
# print(dir(dll))
# Properties/Methods on the Linked List: 'add_to_head', 'add_to_tail', 'delete', 'get_max', 'head', 'length', 'move_to_end', 'move_to_front', 'remove_from_head', 'remove_from_tail', 'tail'
# appending:
    # check capacity.  
    # if length of list < capacity: add to tail. 
    # else list length >= capacity: delete the head. and add new element to tail
    #if reaching capacity. 

#adding new value: check capacity, if not reached, simply add to tail: in this case, capacity = 7
# dll.add_to_tail(1)
# dll.add_to_tail(2)
# dll.add_to_tail(3)
# dll.add_to_tail(4)
# dll.add_to_tail(5)
# dll.add_to_tail(6)
# dll.add_to_tail(7)

# adding new value: check capacity, if reached, remove from head and add to tail 
# dll.remove_from_head()
# dll.add_to_tail(8)

# adding new value: check capacity, if reached, remove from head and add to tail 
# dll.remove_from_head()
# dll.add_to_tail(9)

# dll.print_list()

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None  #pointer to a node
        self.storage = DoublyLinkedList()

    def append(self, item):
        # self.storage.add_to_tail(item)

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        else: #self.storage.length >= self.capacity
            if self.current is self.storage.tail:
                self.current = self.storage.head
                self.current.value = item
            else: #current is not tail
                self.current = self.current.next
                self.current.value = item


        # print('length', self.storage.length)
        # if self.storage.length < self.capacity:
        #     if self.storage.length <= 1 and self.storage.head:
        #         self.storage.head.oldest = True
        #     self.storage.add_to_tail(item)
        # else:
        #     # self.storage.head.oldest = True
        #     self.storage.add_to_tail(item)
        #     self.storage.move_to_front(self.storage.tail)
        #     self.storage.shift_oldest()

        # o = self.storage.find_oldest()
        # print('oldest', o)
        '''   
        add to tail
        remove old head
        take tail, move it to head
        set newhead.next = oldhead
        '''
        # if self.storage.length < self.capacity:
        #     self.storage.add_to_tail(item)
        # else: #buffer capacity met.  remove from buffer (linked list)
        #     self.storage.remove_from_head()
        #     self.storage.add_to_tail(item)



            # self.storage.move_to_front(self.storage.tail)
            #move head to tail
            # print('head',self.storage.head.value)
            # print('tail', self.storage.tail.value)
            

    def get(self):
        # Note:  This is the only [] allowed
        # list_buffer_contents = self.storage.print_list()
        # print('list_buffer_contents', list_buffer_contents)
        # return list_buffer_contents
        buffer = []
        n = self.storage.head
        while n:
            for i in range(self.storage.length):
                print('val in buffer: ',n.value)
                buffer.append(n.value)
                n = n.next
        # first = buffer[0]
        # last = buffer[-1]
        # buffer[0] = last
        # buffer[-1] = first

        return buffer

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')

exp = ['f','g','c','d','e']
act = buffer.get()
print('actual', act)
print('expected', exp)


# print('initial full capacity:', buffer.get())
# b = buffer.get()
# print('\nactual: ', b)
# print('expected: ',['f', 'b', 'c', 'd', 'e'])

# set new head to head.next
# remove old_head from linked list
# set tail.next -> 

# buffer.append('g')
# # buffer.append('h')
# # buffer.append('i')
# c = buffer.get()
# e = ['f', 'g', 'h', 'i', 'e']

# print('\nactual: ', c)
# print('expected: ',e)



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
