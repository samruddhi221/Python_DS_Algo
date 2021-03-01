# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# 1. void add(key): Inserts the value key into the HashSet.
# 2. bool contains(key): Returns whether the value key exists in the HashSet or not.
# 3. void remove(key): Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class SetNode():
    def __init__(self, key):
        self.key = key
        self.next = None


class HashSet:
    def __init__(self):
        self.size = 1000
        self.hashSet = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size
        if self.hashSet[index] is None:
            self.hashSet[index] = SetNode(key)
        else:
            node = self.hashSet[index]
            while node:
                if node.key == key:
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = SetNode(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.hashSet[index]
        if not curr:
            return
        else:
            while curr:
                if curr.key == key:
                    curr.key = None
                    break
                curr = curr.next

    def contains(self, key: int) -> None:
        index = key % self.size
        node = self.hashSet[index]
        if not node:
            return False
        else:
            while node:
                if node.key == key:
                    return True
                else:
                    node = node.next
            return False


if __name__ == '__main__':
    obj = HashSet()
    obj.add(2)
    obj.remove(key)
    param_3 = obj.contains(key)
