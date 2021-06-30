class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.__root = None

    def insert_node(self, data: int) -> None:
        self.__root = self.__insert_implementation(self.__root, data)
        return

    def __insert_implementation(self, node: TreeNode, data: int) -> TreeNode:
        if not node:
            new_node = TreeNode(data)
            return new_node

        if data <= node.val:
            node.left = self.__insert_implementation(node.left, data)
        if data > node.val:
            node.right = self.__insert_implementation(node.right, data)
        return node

    def delete_node(self, data: int) -> None:
        self.__root = self.__delete_implementation(self.__root, data)

    def __delete_implementation(self, node: TreeNode, data: int) -> TreeNode:
        if not node:
            return None
        elif not node.left and not node.right and node.val == data:
            node = None
            return None

        if data < node.val:
            node.left = self.__delete_implementation(node.left, data)
        elif data > node.val:
            node.right = self.__delete_implementation(node.right, data)
        else:
            replacement_node = TreeNode()
            left_height = self.height(node.left)    # Height of left subtree of the current node
            right_height = self.height(node.right)  # Height of right subtree of the current node

            # if left_height > right_height, replace the node with its inorder
            # predecessor(largest element in the left subtree)
            if left_height > right_height:
                replacement_node = self.inorder_predecessor(node.left)
                node.val = replacement_node.val
                node.right = self.__delete_implementation(node.left, replacement_node.val)
            else:
                # if left_height <= right_height, replace the node with its inorder
                # successor(smallest element in the right subtree)
                replacement_node = self.inorder_successor(node.right)
                node.val = replacement_node.val
                node.left = self.__delete_implementation(node.right, replacement_node.val)
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
        return max(self.height(node.right), self.height(node.left)+1)

    def search_value(self, data: int) -> bool:
        return self.__search_helper(self.__root, data)

    def __search_helper(self, node: TreeNode, data: int) -> bool:
        if not node:
            return False
        if node.val == data:
            return True
        if data < node.val:
            return self.__search_helper(node.left, data)
        if data > node.val:
            return self.__search_helper(node.right, data)

    def inorder(self):
        print("inorder tree traversal: ")
        inorder_list = []
        # self.__inorder_traversal_recursive(self.__root, inorder_list)
        self.__inorder_traversal_iterative(self.__root, inorder_list)
        print(inorder_list)

    def __inorder_traversal_recursive(self, node: TreeNode, node_list: list) -> None:
        if not node:
            return

        self.__inorder_traversal_recursive(node.left, node_list)
        node_list.append(node.val)
        self.__inorder_traversal_recursive(node.right, node_list)
        return

    def __inorder_traversal_iterative(self, node: TreeNode, node_list: list) -> None:
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            node_list.append(node.val)
            node = node.right
        return

    def preorder(self):
        print("preorder tree traversal: ")
        preorder_list = []
        # self.__preorder_traversal_recursive(self.__root, preorder_list)
        self.__preorder_traversal_iterative(self.__root, preorder_list)
        print(preorder_list)

    def __preorder_traversal_recursive(self, node: TreeNode, node_list: list) -> None:
        if not node:
            return

        node_list.append(node.val)
        self.__preorder_traversal_recursive(node.left, node_list)
        self.__preorder_traversal_recursive(node.right, node_list)
        return

    def __preorder_traversal_iterative(self, node: TreeNode, node_list: list) -> None:
        stack = []
        stack.append(node)

        while stack:
            node = stack.pop()
            node_list.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder(self):
        print("postorder tree traversal: ")
        postorder_list = []
        # self.__postorder_traversal_recursive(self.__root, postorder_list)
        self.__postorder_traversal_iterative(self.__root, postorder_list)
        print(postorder_list)

    def __postorder_traversal_recursive(self, node: TreeNode, node_list: list) -> None:
        if not node:
            return

        self.__postorder_traversal_recursive(node.left, node_list)
        self.__postorder_traversal_recursive(node.right, node_list)
        node_list.append(node.val)
        return

    def __postorder_traversal_iterative(self, node: TreeNode, node_list: list) -> None:
        stack = []
        stack.append(node)

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node_list.append(node.val)
        node_list.reverse()


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert_node(5)
    tree.insert_node(3)
    tree.insert_node(4)
    tree.insert_node(7)
    tree.insert_node(9)
    tree.insert_node(6)
    tree.insert_node(8)
    tree.insert_node(10)
    tree.insert_node(2)
    tree.inorder()
    tree.preorder()
    tree.postorder()
    print(tree.search_value(8))
    print(tree.search_value(1))
    tree.delete_node(2)
    tree.inorder()
    tree.delete_node(9)
    tree.inorder()
    # bst.delete_node(5)
    # bst.inorder()
