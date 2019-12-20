from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
# print(dir(dll))
# Properties/Methods on the Linked List: 'add_to_head', 'add_to_tail', 'delete', 'get_max', 'head', 'length', 'move_to_end', 'move_to_front', 'remove_from_head', 'remove_from_tail', 'tail'
# appending:
    # check capacity.  
    # if length of list < capacity: add to tail. 
    # else list length >= capacity: delete the head. and add new element to tail
    #if reaching capacity. 

dll.add_to_tail(1)
dll.add_to_tail(2)
dll.add_to_tail(3)
dll.add_to_tail(4)
dll.add_to_tail(5)
dll.add_to_tail(6)
dll.add_to_tail(7)


dll.print_list()


# def print_list(ll):
#     for i in range(ll.length):
#         print(ll.head.value)
#         ll.head = ll.head.next

# print_list(dll)







class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
