class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()
        visited = set()
        order = []

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
            order.append(node)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return order 