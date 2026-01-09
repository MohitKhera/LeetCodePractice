class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
            for j in prerequisites:
                if i == j[0]:
                    preMap[i].append(j[1])
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for i in preMap[node]:
                if dfs(i) == False:
                    return False    
            visiting.remove(node)
            visited.add(node)

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True