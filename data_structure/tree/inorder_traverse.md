### Tree Node
```Java
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x){
        val = x;
    }
}
```

### Traverse
```Java
class Solution{
    private void traverse(TreeNode node, List<Integer> result){
        if(node == null){
            return;
        }

        traverse(root.left, result);
        result.add(node.val);
        traverse(root.right, result);
    }

    public List<Integer> preorderTraverse(TreeNode root){
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }
}
```

### Divide and Conquer
```Java
class Solution{
    private List<Integer> traverse(TreeNode node){
        if(node == null){
            return new ArrayList<Integer>();
        }

        List<Integer> leftResult = traverse(node.left);
        List<Integer> rightResult = traverse(node.right);

        List<Integer> result = new ArrayList<>();
        result.addAll(leftResult);
        result.add(node.val);
        result.addAll(rightResult);

        return result;
    }

    public List<Integer> preorderTraverse(TreeNode root){
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }
}
```

### Non-recursion
```Java
class Solution{
    public List<Integer> traverse(TreeNode root){
        List<Integer> result = new ArrayList<>();
        if(root == null){
            return result;
        }

        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while(curr != null || !stack.isEmpty()){
            while(curr != null){
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            result.add(curr.val);
            curr = curr.right;
        }

        return result;
    }
}
```