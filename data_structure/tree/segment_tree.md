## Segment Tree

[Leetcode 307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

```Java
class SegmentTreeNode {
    public int start;
    public int end;
    public int val;
    public SegmentTreeNode left;
    public SegmentTreeNode right;
    
    public SegmentTreeNode(int start, int end, int val, SegmentTreeNode left, SegmentTreeNode right){
        this.start = start;
        this.end = end;
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class SegmentTree {
    private SegmentTreeNode root;
    
    private SegmentTreeNode buildTree(int[] nums, int start, int end){
        if(start == end){
            return new SegmentTreeNode(start, end, nums[start], null, null);
        }
        
        int mid = start + (end - start) / 2;
        SegmentTreeNode left = buildTree(nums, start, mid);
        SegmentTreeNode right = buildTree(nums, mid + 1, end);
        
        return new SegmentTreeNode(start, end, left.val + right.val, left, right);
    }
    
    private void updateSegmentTreeHelper(SegmentTreeNode node, int index, int val){
        if(node.start == index && node.end == index){
            node.val = val;
            return;
        }
        
        int mid = node.start + (node.end - node.start) / 2;
        if(index <= mid){
            updateSegmentTreeHelper(node.left, index, val);
        }else{
            updateSegmentTreeHelper(node.right, index, val);
        }
        
        node.val = node.left.val + node.right.val;
    }
    
    private int sumRangeHelper(SegmentTreeNode node, int start, int end){
        if(node.start == start && node.end == end){
            return node.val;
        }
        
        int mid = node.start + (node.end - node.start) / 2;
        if(end <= mid){
            return sumRangeHelper(node.left, start, end);
        }else if(start > mid){
            return sumRangeHelper(node.right, start, end);
        }
        
        return sumRangeHelper(node.left, start, mid) + sumRangeHelper(node.right, mid + 1, end);
    }

    public SegmentTree(int[] nums) {
        if(nums.length > 0){
            root = buildTree(nums, 0, nums.length - 1);
        }
    }
    
    public void update(int i, int val) {
        updateSegmentTreeHelper(root, i, val);
    }
    
    public int sumRange(int i, int j) {
        return sumRangeHelper(root, i, j);
    }
}
```