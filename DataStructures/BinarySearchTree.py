class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.__root = None

    def insert_node(self, data: int) -> None:
        self.__root = self.__insert_implementation(self.__root, data)

    def __insert_implementation(self, node: TreeNode, data: int) -> TreeNode:
        if not node:
            node = TreeNode(data)
            return node

        if data < node.val:
            node.left = self.__insert_implementation(node.left, data)
        if data > node.val:
            node.right = self.__insert_implementation(node.right, data)
        return node

    def delete_node(self, data: int) -> None:
        self.__root = self.__delete_implementation(self.__root, data)

    def __delete_implementation(self, node: TreeNode, data: int) -> TreeNode:
        if not node:
            return None
        elif not node.right and not node.left and node.val == data:
            node = None
            return None

        if data < node.val:
            node.left = self.__delete_implementation(node.left, data)
        elif data > node.val:
            node.right = self.__delete_implementation(node.right, data)
        else:
            replacement_node = TreeNode()
            if self.height(node.left) > self.height(node.right):
                replacement_node = self.inorder_predecessor(node.left)
                node.val = replacement_node.val
                node.right = self.__delete_implementation(node.left, replacement_node.val)
            else:
                replacement_node = self.inorder_successor(node.right)
                node.val = replacement_node.val
                node.right = self.__delete_implementation(node.right, replacement_node.val)
        return node

    def inorder_predecessor(self, node: TreeNode) -> TreeNode:
        while node and node.right:
            node = node.right
        return node

    def inorder_successor(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self.height(node.right), self.height(node.left) + 1)

    def search_value(self, data: int) -> bool:
        return self.__search_helper(self.__root, data)

    def __search_helper(self, node: TreeNode, data: int) -> bool:
        if not node:
            return False
        if data == node.val:
            return True
        flag = False
        if data < node.val:
            flag = self.__search_helper(node.left, data)
        elif data > node.val:
            flag = self.__search_helper(node.right, data)
        return flag

    def inorder(self):
        print("inorder tree traversal: ")
        inorder_list = []
        self.__inorder_traversal(self.__root, inorder_list)
        print(inorder_list)

    def __inorder_traversal(self, node: TreeNode, node_list: list) -> None:
        if not node:
            return None

        self.__inorder_traversal(node.left, node_list)
        node_list.append(node.val)
        self.__inorder_traversal(node.right, node_list)
        return


if __name__ == '__main__':
    bst = BST()
    bst.insert_node(5)
    bst.insert_node(3)
    bst.insert_node(4)
    bst.insert_node(7)
    bst.insert_node(9)
    bst.insert_node(6)
    bst.insert_node(8)
    bst.insert_node(10)
    bst.insert_node(2)
    bst.inorder()
    # print(bst.search_value(8))
    # print(bst.search_value(1))
    # bst.delete_node(2)
    # bst.inorder()
    # bst.delete_node(9)
    # bst.inorder()
    bst.delete_node(5)
    bst.inorder()
