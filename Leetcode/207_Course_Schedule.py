class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        self.adj = [None]*numCourses
        for i in range(numCourses):
            self.adj[i]=[]
        
        for pre in prerequisites:
            self.adj[pre[0]].append(pre[1])
    
        self.visited = [0]*numCourses
        for i in range(numCourses):
            if self.visited[i]==0 and not self.dfs(i):return False
        
        return True
    
    def dfs(self,v):
        if self.visited[v]==1: return False
        self.visited[v]=1
            
        for ad in self.adj[v]:
            if not self.visited[ad]==2 and not self.dfs(ad):return False
            
        self.visited[v]=2
        
        return True