class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def insert_after_node(self, prev_node,data):
        if prev_node is None:
            print("previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def getcount(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1  
        return count

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else: 
            print(name + ":" + node.data)

    def reverse_list(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CUR")
            self.print_helper(nxt, "NXT")
            print("------------------------------")
            prev = curr
            curr = nxt
        self.head = prev

    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and position > index:
            previous = current
            current = current.next
            index += 1
        if position > index:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
            print("Deleted node is: ", current.data)
            # current = None #Optional statement

    def GetNth(self, index):
        count = 0
        curr = self.head

        while curr:
            if count == index:
                return curr.data
            count += 1
            curr = curr.next

    def printNthFromLast(self, N):
            main_ptr = self.head
            ref_ptr = self.head
    
            count = 0
            if(self.head is not None):
                while(count < N):
                    print("while 'count' = ", count)
                    if(ref_ptr is None):
                        print("% s is greater than the no. of nodes in list" % (N))
                        return
                    ref_ptr = ref_ptr.next
                    count += 1
    
            if(ref_ptr is None):
                self.head = self.head.next
                print(N)
                if(self.head is not None):
                    print("Node no. % s from last is % s " % (N, main_ptr.data))
                    
            else:
                while(ref_ptr is not None):
                    main_ptr = main_ptr.next
                    ref_ptr = ref_ptr.next
    
                print("Node no. % s from laaast is % s " % (N, main_ptr.data))


# 1 2 3 4 5 pos
# 0 1 2 3 4 index
# A B C D E

# node = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# node4 = Node("D")
# single = SinglyLinkedList()
# single.head = node
# single.head.next = node2
# node2.next = node3
# node3.next = node4
# single.insert_after_node(node,"E")
# single.print_list()


result = SinglyLinkedList()
result.append("A")
result.append("B")
result.append("C")
result.append("D")
# # result.printNthFromLast(4)
# # n = 3
# # print(f"Element at index {n} is ", result.GetNth(n))
# # result.deleteNodeAtGivenPosition(2)
# result.reverse_list()
# print("The length of the list is: ", result.getcount())
# result.print_list()
    
# def twoSum(nums: list[int], target: int) -> list[int]:

#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             sum = nums[i] + nums[j]
#             print(f"({nums[i]},{nums[j]}) = {sum}")
#             print(f"[{i},{j}]")
#             if sum == target:
#                 return [i, j]
# result = twoSum([2,4,6,7], 13)
# print("the indices of both numbers that adds up to 9 is: ", result)



