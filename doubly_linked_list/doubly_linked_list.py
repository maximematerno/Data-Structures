"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)

        if not self.head and not self.tail:
            self.head = new_node   
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # reference the delete function first
        value = self.head.value
        self.delete(self.head)
        return value 

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)

        if not self.head and not self.tail:
            self.head = new_node   
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # reference remove from head, just switch head to tail, simple
        value = self.tail.value
        self.delete(self.tail)
        return value 

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # take advantage of the functions we've already written
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # reference move to front, simple
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    # Note can delete themselves, this handles the metadata 
    def delete(self, node):
        self.length -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head

        while current:
            # this iterates through this list, will be neccessary on any linked list problem
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
