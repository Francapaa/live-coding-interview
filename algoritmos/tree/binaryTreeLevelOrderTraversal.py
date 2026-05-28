# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        current=[]
        if not root:
            return result
        current.append(root)

        while current: 
            currentList = []
            for val in current: 
                currentList.append(val.val)
            parents = current
            result.append(currentList)
            current = []
            for node in parents:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)

        return result