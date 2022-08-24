class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.bst_list = []
        self.inorder(root)
        for i in range(1,len(self.bst_list)):
            if self.bst_list[i]>self.bst_list[i-1]:
                continue
            else:
                return False
        return True
    
    def inorder(self,root):
        if root == None:
            return
        
        self.inorder(root.left)
        
        self.bst_list.append(root.val)
        
        self.inorder(root.right)