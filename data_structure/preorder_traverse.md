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

        result.add(node.val);
        traverse(root.left, result);
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
        result.add(node.val);
        result.addAll(leftResult);
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

        Stack<Integer> stack = new Stack<>();
        stack.push(root);

        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            result.add(node.val);

            // push right child
            if(node.right != null){
                stack.push(node.right);
            }

            // push left child
            if(node.left != null){
                stack.push(node.left);
            }
        }

        return result;
    }
}
```