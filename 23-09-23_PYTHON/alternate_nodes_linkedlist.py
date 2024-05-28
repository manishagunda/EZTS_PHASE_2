class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_alternate_nodes(self):
        current = self.head
        count = 0
        while current:
            if count % 2 == 0:
                print(current.data, end=" ")
            count += 1
            current = current.next

if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()
    elements = [1,2,32,4,56,61,79,8]

    for element in elements:
        linked_list.append(element)

    print("Alternate nodes in the linked list:")
    linked_list.print_alternate_nodes()
