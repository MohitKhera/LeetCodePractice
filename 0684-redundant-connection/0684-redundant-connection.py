class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        
        visited = set()

        def dfs(node, target, parent):
            if node == target:
                return True
            if node in visited:
                return False
            visited.add(node)
            for i in connections[node]:
                if i == parent:
                    continue
                if dfs(i, target, node):
                    return True

        for i in edges:
            visited.clear()
            if dfs(i[1], i[0], -1):
                return i
            else:
                connections[i[0]].append(i[1])
                connections[i[1]].append(i[0])