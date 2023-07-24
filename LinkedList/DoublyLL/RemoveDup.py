class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_duplicates(self):
        current = self.head
        unique_values = set()

        while current:
            if current.data in unique_values:
                # Duplicate node found, remove it from the list
                prev_node = current.prev
                next_node = current.next

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                current = next_node
            else:
                unique_values.add(current.data)
                current = current.next


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(2)
    dll.append(4)
    dll.append(1)

    print("Original Doubly Linked List:")
    dll.print_list()

    dll.remove_duplicates()

    print("\nDoubly Linked List after removing duplicates:")
    dll.print_list()
