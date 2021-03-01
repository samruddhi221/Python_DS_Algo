class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def add_at_head(self, val: int) -> None:
        new_node = ListNode(val)
        if self.len == 0:
            self.head = new_node
            self.len += 1
            return
        else:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            self.len += 1
            return

    def add_at_tail(self, val: int) -> None:
        if self.len == 0:
            self.add_at_head(val)
            return
        else:
            new_node = ListNode(val)
            curr_head = self.head
            while curr_head.next:
                curr_head = curr_head.next
            curr_head.next = new_node
            self.len += 1
            return

    def add_at_index(self, index: int, val: int) -> None:       # index starts from 0
        if (self.len > index) or (index < 0):
            print("Index out of bounds")
            return
        elif self.len == 0 and index == 0:
            self.add_at_head(val)
            return
        elif self.len > 0 and self.len == index:
            self.add_at_tail(val)
            return
        else:
            new_node = ListNode(val)
            prev = self.head
            count = 0
            while count < index - 1:
                prev = prev.next
                count += 1
            new_node.next = prev.next
            prev.next = new_node
            self.len += 1
            return

    def delete_at_index(self, index: int) -> None:
        if index >= self.len or index < 0:
            print("Invalid index")
            return
        elif index == 0:            # deleting a head
            if self.len == 1:
                self.head = None
            else:
                curr_node = self.head
                self.head = curr_node.next
                curr_node = None
            self.len -= 1
            return
        else:
            count = 0
            curr_node = self.head
            prev_node = ListNode
            prev_node.next = curr_node
            while count < index:
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1
            prev_node.next = curr_node.next
            curr_node = None
            self.len -= 1
            return

    def search(self, val: int) -> bool:
        curr_head = self.head
        while curr_head:
            if curr_head.val == val:
                return True
            curr_head = curr_head.next
        return False

    def print_linked_list(self) -> list:
        linked_list = []
        curr_node = self.head
        while curr_node:
            linked_list.append(curr_node.val)
            curr_node = curr_node.next
        return linked_list

    def reverse(self) -> None:
        self.head = self.__in_place_reverse_recursive(self.head)
        return

    def __in_place_reverse_recursive(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        prev = self.in_place_reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return prev

    def __in_place_reverse_iterative(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        while curr_node:
            temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_node
        return prev_node

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
    sll.reverse()
    print(sll)