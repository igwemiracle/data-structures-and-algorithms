class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertNode(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next

# TIME COMPLEXITY: O(m+n). Here ‘m’ and ‘n’ are number
# of elements present in first and second lists respectively. Reason:
# For Union: Traverse both the lists, store the elements in Hash-map and update the respective count.
# AUXILIARY SPACE--> O(m+n). Use of Hashmap data structure for storing values.
# Return the head of new list containing the Union of 2 linkedList


def Union(List1, List2):
    HashMap = {}
    while (List1 != None):
        data = List1.data
        if (data not in HashMap.keys()):
            HashMap[data] = 1
        List1 = List1.next

    while (List2 != None):
        data = List2.data
        if (data not in HashMap.keys()):
            HashMap[data] = 1
        List2 = List2.next
    # making a new list
    ans = LinkedList()
    # traverse HashMap
    for key, value in HashMap.items():
        ans.InsertNode(key)
    return ans.head


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


ll1 = LinkedList()
ll1.InsertNode(1)
ll1.InsertNode(2)
ll1.InsertNode(3)
ll1.InsertNode(4)
ll1.InsertNode(5)

ll2 = LinkedList()
ll2.InsertNode(1)
ll2.InsertNode(3)
ll2.InsertNode(5)
ll2.InsertNode(2)

print("First list is ")
printList(ll1.head)
print("")
print("Second list is")
printList(ll2.head)
print("")
print("Union list is ")
printList(Union(ll1.head, ll2.head))
