class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
# Looks for a pair in the list that adds up
# sum_vals.

    def pairs_with_sum(self, sum_vals):
        pairs = []
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_vals:
                    # pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                    pairs.append((p.data, q.data))
                q = q.next
            p = p.next
        return pairs


dllist = DoublyLinkedList()
dllist.append(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
sum_vals = 5

ans = dllist.pairs_with_sum(sum_vals)
print(f"The pair {ans} from the list gives the sum of {sum_vals}.")
