# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        result = []
        stack = []
        curr = root
        
        while curr!=None or stack != []:
            while curr != None:
                stack.append(curr)
                curr = curr.left

            x = stack.pop()
            result.append(x.val)
            curr = x.right
            
            
        
        return result
    
