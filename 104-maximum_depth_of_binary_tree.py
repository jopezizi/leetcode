class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
    
sol = Solution()
t4 = TreeNode(15)
t5 = TreeNode(7)
t2 = TreeNode(9)
t3 = TreeNode(20,t4,t5)
t1 = TreeNode(3,t2,t3)
print(sol.maxDepth(t1)) 
