class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.left = Node()
        self.right = Node()
        self.cap = capacity
        self.size = 0
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        formerLast = self.right.prev
        formerLast.next = node
        node.prev = formerLast
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        n = self.dic[key]
        self.remove(n)
        self.insert(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            n = self.dic[key]
            n.val = value
            self.remove(n)
            self.insert(n)
        else:
            n = Node(key, value)
            self.insert(n)
            self.dic[key] = n 
            self.size+=1
            if self.size > self.cap:
                lru = self.left.next
                self.remove(lru)
                self.dic.pop(lru.key)
 