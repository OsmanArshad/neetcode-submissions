class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(source, destination):
            if source not in graph or destination not in graph:
                return -1
            
            queue = collections.deque([(source, 1.0)])
            seen = {(source)}

            while queue:
                node, total_value = queue.popleft()
                if node == destination:
                    return total_value
                
                for neighbor, value in graph[node]:
                    if neighbor not in seen:
                        seen.add((neighbor))
                        queue.append((neighbor, total_value * value))
            return -1.0


        graph = collections.defaultdict(list)

        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        ans = []
        for query in queries:
            c, d = query
            ans.append(bfs(c, d))
        return ans