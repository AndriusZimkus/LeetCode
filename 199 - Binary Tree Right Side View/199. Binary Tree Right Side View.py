
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rightValues = []
        n = 1
        while 2**n < len(root):
            print(2**n)
            rightValues.append(root[2**n]-2)
            n+=1
        
        rightValues.append(root[len(root)-1])
        return rightValues


sol = Solution()

root = [1,2,3,None,5,None, 4]
##root = [1,None,3]

print(sol.rightSideView(root))
