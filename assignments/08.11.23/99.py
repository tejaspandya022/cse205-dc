class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, pre = None, None, None
        current = root
        
        while current is not None:
            if current.left is None:
                if pre is not None and pre.val > current.val:
                    if first is None:
                        first = pre
                    second = current
                pre = current
                current = current.right
            else:
                node = current.left
                while node.right is not None and node.right != current:
                    node = node.right
                if node.right is None:
                    node.right = current
                    current = current.left
                else:
                    node.right = None
                    if pre is not None and pre.val > current.val:
                        if first is None:
                            first = pre
                        second = current
                    pre = current
                    current = current.right
        
        if first is not None and second is not None:
            first.val, second.val = second.val, first.val