```Java
class UnionFindSet{
    private int[] parents;
    private int[] ranks;

    public UnionFindSet(int n){
        parents = new int[n + 1];
        ranks = new int[n + 1];
        for(int i = 0; i < parents.length; i++){
            parents[i] = i;
            ranks[i] = 1;
        }
    }

    public int find(int u){
        while(parents[u] != u){
            // not a root
            parents[u] = parents[parents[u]];
            u = parents[u];
        }

        return u;
    }

    public boolean union(int u, int v){
        int rootU = find(u);
        int rootV = find(v);
        if(rootU == rootV){
            return false;
        }

        if(ranks[rootU] > ranks[rootV]){
            parents[rootV] = parents[rootU];
        }else if(ranks[rootU] < ranks[rootV]){
            parents[rootU] = parents[rootV];
        }else{
            parents[rootV] = parents[rootU];
            ranks[rootU]++;
        }

        return true;
    }

}
```