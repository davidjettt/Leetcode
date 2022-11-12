class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if 0 > index or index >= self.length:
            return -1
        curr = self.head
        
        while index != 0:
            index -= 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        
        if self.head:
            self.head.prev = node
        
        node.next = self.head
        self.head = node
        
        self.length += 1
        if self.length == 1:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        
        if self.length == 1:
            self.head = new_node
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            
            while index - 1 != 0:
                index -= 1
                curr = curr.next
            
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next.prev = new_node
            new_node.prev = curr
            curr.next = new_node
            self.length += 1
            # h     c           t
            # 1 <-> 2 <-> 3 <-> 4
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        elif index == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            
        elif index == self.length - 1:
            
            self.tail.prev.next = None
            self.tail = self.tail.prev
            
            self.length -= 1
        else:
            curr = self.head
            
            while index - 1 != 0:
                index -= 1
                curr = curr.next
            if curr.next:
                curr.next = curr.next.next
                curr.next.prev = curr
            self.length -= 1
            
# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.length: 
#             return -1
        
#         curr = self.head
        
#         while index != 0:
#             index -= 1
#             curr = curr.next
            
#         return curr.val
        

#     def addAtHead(self, val: int) -> None:
#         new_node = ListNode(val)
        
#         new_node.next = self.head
        
#         if self.head:
#             self.head.prev = new_node
        
#         self.head = new_node
#         self.length += 1
        
#         if self.length == 1:
#             self.tail = new_node

#     def addAtTail(self, val: int) -> None:
#         new_node = ListNode(val)
        
#         if self.tail:
#             self.tail.next = new_node
#             new_node.prev = self.tail
            
#         self.tail = new_node
        
#         self.length += 1
#         if self.length == 1:
#             self.head = new_node
        
#         # new_node.prev = self.tail
#         # if self.tail:
#         #     self.tail.next = new_node
#         # self.tail = new_node
#         # self.length += 1
#         # if self.length == 1:
#         #     self.head = new_node
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.length:
#             return
#         elif index == 0:
#             self.addAtHead(val)
#         elif index == self.length:
#             self.addAtTail(val)
#         else:
#             curr = self.head
#             while index - 1 != 0:
#                 index -= 1
#                 curr = curr.next
            
#             new_node = ListNode(val)
#             new_node.next = curr.next
#             curr.next.prev = new_node
#             new_node.prev = curr
#             curr.next = new_node
            
#             self.length += 1
        
#     # 1 <-> 2 <-> 3
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 and index >= self.length:
#             return
#         # delete from head
#         elif index == 0:
#             if self.head.next:
#                 self.head.next.prev = None
#             self.head = self.head.next
#             self.length -= 1
#             if self.length == 0:
#                 self.tail = None
#         # delete from tail
#         elif index == self.length - 1:
#             if self.tail.prev:
#                 self.tail.prev.next = None
#             self.tail = self.tail.prev
#             self.length -= 1
#             if self.length == 0:
#                 self.head = None
#         else:
#             curr = self.head
#             while index - 1 != 0:
#                 index -= 1
#                 curr = curr.next
#             if curr.next:
#                 curr.next = curr.next.next
#                 curr.next.prev = curr

#             self.length -= 1
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)