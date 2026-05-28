# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        print(result)
        result += self.inorderTraversal(root.right)
        return result
        
""" VAMOS ACUMULANDO DENTRO DE RESULT 
    python va agregando los elementos al final de la lista
"""