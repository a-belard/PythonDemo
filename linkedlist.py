class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.current = None

    def isEmpty(self) -> bool:
        return True if self.head is None else False

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index -= 1

        return current_node.data

    def addAtHead(self, val: int) -> None:
        if self.isEmpty():
            self.head = Node(val, None)
            self.current = self.head
            self.length += 1
            return
        temp_head = self.head
        self.head = Node(val, temp_head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.isEmpty():
            self.head = Node(val, None)
            self.current = self.head
            self.length += 1
            return
        current_node = self.current
        current_node.next = Node(val, None)
        self.current = current_node.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if self.isEmpty():
            self.head = Node(val, None)
            self.length += 1
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            current_node = self.current
            current_node.next = Node(val, None)
            self.current = current_node.next
            self.length += 1
            return
        prev = None
        current_node = self.head
        while index > 0:
            prev = current_node
            current_node = current_node.next
            index -= 1

        prev.next = Node(val, current_node)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.isEmpty():
            return
        if index >= self.length:
            return
        if index == 0:
            tempHead = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.current = None
            del tempHead
            return
        indexCopy = index
        prev = None
        current_node = self.head
        while index > 0:
            prev = current_node
            current_node = current_node.next
            index -= 1

        prev.next = current_node.next
        if indexCopy == self.length - 1:
            self.current = prev
        self.length -= 1
        del current_node

    def print(self):
        if self.isEmpty():
            return
        current_node = self.head
        mystring = ""
        while current_node:
            mystring += str(current_node.data) + "-->"
            current_node = current_node.next
        print(mystring)


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtIndex(1,0)
    print(obj.get(0))

    # obj.addAtHead(1)
    # obj.addAtTail(3)
    # obj.addAtIndex(1,2)
    # obj.get(1)
    # obj.deleteAtIndex(1)
    # obj.get(1)
    # obj.get(3)
    # obj.deleteAtIndex(3)
    # obj.deleteAtIndex(0)
    # obj.get(0)
    # obj.deleteAtIndex(0)
    # obj.get(0)

    # obj.addAtHead(0)
    # obj.addAtIndex(1,4)
    # obj.addAtTail(8)
    # obj.addAtHead(5)
    # obj.addAtIndex(4,3)
    # obj.addAtTail(0)
    # obj.addAtTail(5)
    # obj.addAtIndex(6,3)
    # obj.deleteAtIndex(7)
    # obj.deleteAtIndex(5)
    # obj.addAtTail(4)

    # obj.addAtIndex(0, 10)
    # obj.addAtIndex(0,20)
    # obj.addAtIndex(1,30)
    # obj.get(0)
    # obj.addAtHead(7)
    # obj.addAtHead(2)
    # obj.addAtHead(1)
    # obj.addAtIndex(3,0)
    # obj.deleteAtIndex(2)
    # obj.addAtHead(6)
    # obj.addAtTail(4)
    # obj.get(4)
    # obj.addAtHead(4)
    # obj.addAtIndex(5,0)
    # obj.addAtHead(6)
    obj.print()


# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)