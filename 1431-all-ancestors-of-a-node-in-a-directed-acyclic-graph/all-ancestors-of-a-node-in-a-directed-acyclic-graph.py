class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Build the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # Create the reverse graph
        reverse_graph = defaultdict(list)
        for u, v in edges:
            reverse_graph[v].append(u)
        
        # Perform topological sort
        in_degree = [0] * n
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Compute ancestors using the reverse graph and topological order
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for parent in reverse_graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(ancestors[parent])
        
        # Convert sets to sorted lists
        result = [sorted(list(anc)) for anc in ancestors]
        
        return result
        