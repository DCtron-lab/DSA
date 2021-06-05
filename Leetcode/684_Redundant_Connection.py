class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [ i for i in range(n+1)]
        
        for v, e in edges:
            p1 = self.get_parent(v)
            p2 = self.get_parent(e)
            
            if p1 == p2:
                return [v,e]
            
            self.parent[p2] = p1
            
    # for get parent of any node       
    def get_parent(self, node):
        
        if self.parent[node] == node:
            return node
        else:
            return self.get_parent(self.parent[node])