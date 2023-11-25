class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L=[]
        def pot(node):
            if node is None:
                return
            pot(node.left)
            pot(node.right)
            L.append(node.val)
            return L
        return pot(root)
            