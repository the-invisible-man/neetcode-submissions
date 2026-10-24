class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.tracker = {}

    def get(self, key: int) -> int:
        if key in self.tracker:
            node = self.tracker[key]

            self.pluck(node)

            self.promoteHead(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.tracker:
            node = self.tracker[key]
            node.value = value
            self.pluck(node)
        else:
            node = Node(key, value)
            self.tracker[key] = node
            self.evictTail()

        self.promoteHead(node)

    def promoteHead(self, node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return

        curHead = self.head

        if node.key == curHead.key:
            # This is already the head. Nothing to do.
            return

        if node.prev is not None and node.key == self.tail.key:
            self.tail = node.prev

        node.prev = None
        node.next = curHead
        curHead.prev = node
        self.head = node

    def evictTail(self) -> None:
        if len(self.tracker) <= self.capacity:
            return

        key = self.tail.key

        if self.tail.prev != None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            
        del self.tracker[key]

    def pluck(self, node) -> None:
        if self.shouldPluck(node) is False:
            return

        if node.prev != None:
            node.prev.next = node.next

        if node.next != None:
            node.next.prev = node.prev

    def shouldPluck(self, node) -> bool:
        return self.head.key != node.key and self.tail.key != node.key

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
