#Find whether an array is a subset of another array using Hashing
def isSubset(arr1, m, arr2, n):
    Hashset = set()
    for j in range(0, m):
        Hashset.add(arr1[j])

    for i in range(0, n):
        if arr2[i] in Hashset:
            continue
        else:
            return False
    return True
    
if __name__ == '__main__':
    arr1 = [12,4,8,1,3,2,5]
    arr2 = [4,3,12,1,9]
    m = len(arr1)
    n = len(arr2)

    if (isSubset(arr1, m, arr2, n)):
        print("arr2[] is a subset of arr1[]")
    else:
        print("arr2[] is not a subset of arr1[]")

isSubset(arr1,m,arr2,n)
print("---------------------------")

#    Union and Intersection of two linked list using Hashing
# Time Complexity: O(m+n). Here ‘m’ and ‘n’ are number of elements present in first
# and second lists respectively. Reason:
# For Union: Traverse both the lists, store the elements in Hash-map and update the respective
# count. 
# For Intersection: Check if count of an element in hash-map is ‘2’.
# Auxiliary Space: O(m+n). Use of Hash-map data structure for storing values.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

# Define a function to perform an inorder traversal of a binary tree
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)


#using a hash table to keep track of the nodes and their indices
#for a Binary tree.
def create_tree(parent):
    n = len(parent)
# Initialize an empty dictionary to keep track of nodes created so far
    nodes = {}
    root = None
    for i in range(0, n):
# If the current node is the root node, create it
        if parent[i] == -1:
            root = Node(i)
            nodes[i] = root
        else:
# If the parent node exists, get it from the dictionary
            parent_node = nodes.get(parent[i], None)
            # If the parent node does not exist yet, create it
            if parent_node is None:
                parent_node = Node(parent[i])
                nodes[parent[i]] = parent_node
# Create a new node and link it to its parent node
            current_node = Node(i)
            if parent_node.left is None:
                parent_node.left = current_node
            else:
                parent_node.right = current_node
            # Add the new node to the dictionary
            nodes[i] = current_node
    # Return the root node of the constructed tree
    return root
parent = [-1, 0, 0, 1, 1, 3, 5]
root = create_tree(parent)
 
print("Inorder traversal of constructed tree:")
inorder(root)
print("")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertNode(self,new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.tail.next = Node(new_data)
            self.tail = self.tail.next

# return the head of new list containing the Intersection of 2 linkedList

def FindIntersection(List1, List2):
    HashMap = {}
    while (List1 != None):
        data = List1.data
        if (data not in HashMap.keys()):
            HashMap[data] = 1
        List1 = List1.next

    #making a new list
    ans = LinkedList()
    while (List2 != None):
        data = List2.data
        if (data in HashMap.keys()):
            #adding data to new list
            ans.InsertNode(data)
        List2 = List2.next
    return ans.head

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# return the head of new list containing the Union of 2 linkedList
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
    #making a new list
    ans = LinkedList()
    #traverse HashMap
    for key,value in HashMap.items():
        ans.InsertNode(key)
    return ans.head
    
def printPairs(arr, arr_size, sum):
 
    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {}
 
    for i in range(0, arr_size):
        diff = sum-arr[i]
        if (diff in hashmap):
            print(f"Yes! there is a pair ({diff},{arr[i]})")
            return
        hashmap[arr[i]] = i
    print("No")
 
 

A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)

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

print("Second list is ")
printList(ll2.head)

print("Intersection list is")
printList(FindIntersection(ll1.head, ll2.head))

print("Union list is ")
printList(Union(ll1.head, ll2.head))

