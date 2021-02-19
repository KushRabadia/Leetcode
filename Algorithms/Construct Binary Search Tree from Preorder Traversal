# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        
        first = root
                
        for i in preorder[1:]:
            while first!=None:
                if i<first.val:
                    if first.left == None:
                        first.left = TreeNode(i)
                        first = first.left
                    first = first.left
                else:
                    if first.right == None:
                        first.right = TreeNode(i)  
                        first = first.right
                    first = first.right
            
            first = root
            
        return root
