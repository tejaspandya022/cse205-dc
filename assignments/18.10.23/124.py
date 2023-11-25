class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -inf

        
        def pathsum(node):
            if not node:
                return 0

            
            left = max(pathsum(node.left),0)
            right = max(pathsum(node.right),0)

            self.maxsum = max(self.maxsum,node.val+left+right)

            
            return node.val+max(left,right)

        pathsum(root)
        return self.maxsum