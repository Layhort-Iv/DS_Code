class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    def append(self,data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.count +=1
    def delete(self,data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                    self.count -=1
                return
            prev = current
            current = current.next

words = DoublyLinkedList()
words.append('a')
words.append('b')
words.append('c')
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 10:
        break