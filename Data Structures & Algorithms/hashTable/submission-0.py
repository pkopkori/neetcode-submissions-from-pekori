class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity
    
    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.table[index]

        if not head:
            self.table[index] = Node(key, value)
        else:
            prev = None
            while head:
                if head.key == key:
                    head.val = value
                    return
                prev, head = head, head.next
            prev.next = Node(key, value)

        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()
            
    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.table[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.table[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[index] = head.next
                self.size -= 1
                return True
            prev, head = head, head.next
        
        return False   

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for head in self.table:
            while head:
                new_index = head.key % new_capacity
                if new_table[new_index] is None:
                    new_table[new_index] = Node(head.key, head.val)
                else:
                    new_head = new_table[new_index]
                    while new_head.next:
                        new_head = new_head.next
                    new_head.next = Node(head.key, head.val)
                head = head.next

        self.capacity = new_capacity
        self.table = new_table
