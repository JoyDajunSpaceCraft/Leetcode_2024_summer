def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        
        # 检查是否从当前节点出发存在匹配链表的路径
        def dfs(head, root):
            if not head:  # 链表已经匹配结束
                return True
            if not root:  # 树节点为空
                return False
            if root.val != head.val:  # 节点值不匹配
                return False
            # 递归检查左子树和右子树是否存在匹配路径
            return dfs(head.next, root.left) or dfs(head.next, root.right)
        
        # 从当前节点出发，或者左子树或者右子树
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
