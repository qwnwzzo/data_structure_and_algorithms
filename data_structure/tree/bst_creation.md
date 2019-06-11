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