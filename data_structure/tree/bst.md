## Create a BST from an array

```Java
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x){
        val = x;
    }
}

class BST {
    public TreeNode root;

    public BST(int[] nums){
        TreeNode node = null;
        for(int i = 0; i < nums.length; i++){
            node = insertNodeToBST(node, val);
        }
        root = node;
    }

    private TreeNode insertNodeToBST(TreeNode node, int val){
        if(node == null){
            return new TreeNode(val, null, null);
        }

        if(val <= node.val){
            node.left = insertNodeToBST(node.left, val);
        }else{
            node.right = insertNodeToBST(node.right, val);
        }

        return node;
    }
}
```

```python
class TreeNode:
    def __init__(self. val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def BST_creation(self, nums):
        node = None
        for num in nums:
            node = self.insert_node(node, num)

        return node

    def insert_node(self, node, num):
        if node is None:
            return TreeNode(num)

        if num <= node.val:
            node.left = self.insert_node(node.left, num)
        else:
            node.right = self.insert_node(node.right, num)

        return node
```

### insert a node in BST
```Python
def insert_node_in_BST(node, val):
    if node is None:
        return TreeNode(val)

    if val <= node.val:
        node.left = self.insert_node_in_BST(node.left, val)
    else:
        node.right = self.insert_node_in_BST(node.right, val)

    return node
```

### delete a node in BST
分治法
三种大情况
1. 节点的值大于目标，那么去右子树去删除节点
2. 小于目标，去左子树
3. 等于目标
    1. 节点是叶子，直接删除节点即可
    2. 节点只有一个子节点，那么就让这个子节点代替节点
    3. 节点有两个子节点，我的方案是找到左子节点的最大值，然后将其替换给当前节点，然后删掉那个最大值的左侧节点
```Python
def delete_node_in_BST(node, val):
    if node is None:
        return None

    if node.val == val:
        if node.left is None and node.right is None:
            return None
        elif node.left is not None and node.right is not None:
            max_left = find_max(node.left)
            root.val = max_left
            root.left = delete_node_in_BST(node.left, max_left)
        elif node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
    elif node.val > val:
        node.left = delete_node_in_BST(node.left, val)
    elif node.val < val:
        node.right = delete_node_in_BST(node.right, val)

    return node

def find_max(node):
    if node.right is None:
        return node.val

    return find(node.right)
```