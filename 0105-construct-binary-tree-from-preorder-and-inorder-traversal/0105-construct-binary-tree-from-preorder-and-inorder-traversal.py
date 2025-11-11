# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: index for index, val in enumerate(inorder)}
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            mid = inorder_index[root_val]

            left_size = mid - in_left

            root.left = helper(1 + pre_left, pre_left + left_size, in_left, mid - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, mid + 1, in_right)

            return root
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)      