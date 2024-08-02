class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get_tail_value(self):
        if self.tail:
            acc = self.tail.value
            return acc
        return None  # Or handle the case where the list is empty

# Usage
list = LinkedList()
list.append(10)
list.append(20)
list.append(30)

print(list.get_tail_value())  # Output: 30
