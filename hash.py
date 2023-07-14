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

