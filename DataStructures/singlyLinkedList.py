class ListNode:
    def __init__(self, value=0):
        self.val = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def add_at_head(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head = newNode
        self.len += 1
        return

    def add_at_tail(self, val: int) -> None:
        if not self.head:
            self.add_at_head(val)
        else:
            node = self.head
            newNode = ListNode(val)
            while node.next:
                node = node.next
            node.next = newNode
            self.len += 1
        return

    def add_at_index(self, index: int, val: int) -> None:  # index starts from 0
        if index > self.len:
            return
        if index == 0:
            self.add_at_head(val)
        elif index == (self.len):
            self.add_at_tail(val)
        else:
            i = 0
            prev = self.head
            newNode = ListNode(val)
            while i < index - 1:
                prev = prev.next
                i += 1
            newNode.next = prev.next
            prev.next = newNode
            self.len += 1
        return

    def delete_at_index(self, index: int) -> None:
        if not self.head:
            return
        if index < 0 or index >= self.len:
            return
        if index == 0:
            self.head = self.head.next  # How to deallocate memory?
        elif index == self.len - 1:
            node = self.head
            while node.next.next:
                node = node.next
            node.next = None
        else:
            prev = ListNode()
            node = self.head
            prev.next = node

            while index > 0:
                prev = prev.next
                node = node.next
                index -= 1
            prev.next = node.next
            node.next = None
        self.len -= 1
        return

    def search(self, val: int) -> bool:
        if self.head:
            node = self.head
            while node:
                if node.val == val:
                    return True
                else:
                    node = node.next
            return False
        else:
            return False

    def print_linked_list(self) -> list:
        ll = []
        node = self.head
        while node:
            ll.append(node.val)
            node = node.next
        return ll

    def reverse_recursive(self) -> None:
        self.head = self.__in_place_reverse_recursive(self.head)
        return

    def reverse_iterative(self) -> None:
        self.head = self.__in_place_reverse_iterative(self.head)
        return

    def __in_place_reverse_recursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev = self.__in_place_reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return prev

    def __in_place_reverse_iterative(self, head: ListNode) -> ListNode:
        prev = None
        curr = self.head
        next = None

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        head = prev
        return head

    def __str__(self):
        return f'{self.print_linked_list()}'


if __name__ == '__main__':
    sll = SinglyLinkedList()
    print(sll)
    sll.add_at_tail(4)
    sll.add_at_head(2)
    print(sll)
    sll.add_at_head(5)
    sll.delete_at_index(1)
    print(sll)
    sll.add_at_index(2, 7)
    print(sll)
    sll.add_at_index(1, 6)
    print(sll)
    sll.delete_at_index(1)
    print(sll)
    sll.reverse_recursive()
    print(sll)
    sll.reverse_iterative()
    print(sll)
