# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.isMirror(root,root)
    def isMirror(aN,bN):
        if aN!=None and bN!=None:
            here = aN.val==bN.val
            #print(aN.val,bN.val,aN.left,aN.right,bN.left,bN.right)
            outer = Solution.isMirror(aN.left,bN.right)
            inner = Solution.isMirror(aN.right,bN.left)
            return here and outer and inner
        else:
            return aN==None and bN==None
        
        """def outer (Node):
            return Node.left.left==Node.right.right
        def inner(Node):
            return Node.left.right==Node.right.left"""