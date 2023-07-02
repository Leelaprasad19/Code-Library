#LeetCode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if(not root):
            return 0
        else:
            left = 1 + self.height(root.left)
            right = 1 + self.height(root.right)

            return max(left, right)

    def eachLevel(self, root, level):
        if(not root):
            return 0
        if(level == 1):
            self.cur.append(root.val)
        else:
            self.eachLevel(root.left, level-1)
            self.eachLevel(root.right, level-1)



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        h = self.height(root)

        sol = []

        for i in range(1,h+1):
            self.cur = []
            self.eachLevel(root, i)
            sol.append(self.cur)

        # print(sol)

        return sol
