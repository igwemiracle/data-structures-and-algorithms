import queue
class Queue:
    def __init__(self) -> None:
        self.queue = []
    def addTop(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    def removeQ(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    def reverse(self):
        return self.queue.reverse()
    
    def print_queue(self):
        for i in self.queue:
            print(i)


    def size(self):
        return len(self.queue)

TheQueue = Queue()
TheQueue.addTop("Mon")
TheQueue.addTop("Tue")
TheQueue.addTop("Wed")
TheQueue.reverse()
TheQueue.print_queue()
# print(TheQueue.removeQ())
# print(TheQueue.removeQ())
print("The size of the queue is",TheQueue.size())


