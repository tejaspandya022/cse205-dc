class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root if not root or root.val == val else self.searchBST(root.left if root.val > val else root.right, val)