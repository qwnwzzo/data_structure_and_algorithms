## Java Version
### BFS
```Java
class DirectedGraphNode {
    int label;
    ArrayList<DirectedGraphNode> neighbors;
    DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
}

public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */    
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        ArrayList<DirectedGraphNode> result = new ArrayList<DirectedGraphNode>();
        HashMap<DirectedGraphNode, Integer> map = new HashMap();
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                if (map.containsKey(neighbor)) {
                    map.put(neighbor, map.get(neighbor) + 1);
                } else {
                    map.put(neighbor, 1); 
                }
            }
        }
        Queue<DirectedGraphNode> q = new LinkedList<DirectedGraphNode>();
        for (DirectedGraphNode node : graph) {
            if (!map.containsKey(node)) {
                q.offer(node);
                result.add(node);
            }
        }
        while (!q.isEmpty()) {
            DirectedGraphNode node = q.poll();
            for (DirectedGraphNode n : node.neighbors) {
                map.put(n, map.get(n) - 1);
                if (map.get(n) == 0) {
                    result.add(n);
                    q.offer(n);
                }
            }
        }
        return result;
    }
}
```

### DFS
```Java
class DirectedGraphNode {
    int label;
    ArrayList<DirectedGraphNode> neighbors;
    DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
}

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        if (graph == null || graph.size() == 0) {
            return new ArrayList<DirectedGraphNode>();
        }
        LinkedList<DirectedGraphNode> result = new LinkedList<>();
        Set<DirectedGraphNode> gray = new HashSet<>();
        Set<DirectedGraphNode> dark = new HashSet<>();
        for (DirectedGraphNode node : graph) {
            if (!gray.contains(node) && !dark.contains(node)) {
                dfs(node, gray, dark, result);
            }
        }
        return new ArrayList<DirectedGraphNode>(result);
    }
    
    void dfs(DirectedGraphNode node, Set<DirectedGraphNode> gray, Set<DirectedGraphNode> dark, LinkedList<DirectedGraphNode> result) {
        gray.add(node);
        for (DirectedGraphNode child : node.neighbors) {
            if (!gray.contains(child) && !dark.contains(child)) {
                dfs(child, gray, dark, result);
            }
        }
        dark.add(node);
        gray.remove(node);
        result.addFirst(node);
    }
}
```