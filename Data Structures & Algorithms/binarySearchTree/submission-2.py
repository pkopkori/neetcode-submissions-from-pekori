class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                   current.right = newNode
                   return
                current = current.right
            else:
                current.value = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if current.key < key:
                current = current.right
            elif current.key > key:
                current = current.left
            else:
                return current.value
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.value if curr else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if self.root == None:
            return -1
        current = self.root
        while current != None and current.right != None:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, curr, key) -> TreeNode:
        if curr == None:
            return None

        if key < curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key > curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.value = minNode.value
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)     
        return res
    
    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
    


