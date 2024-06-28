class Solution(object):
    def maximumImportance(self, n, roads):
        degree = [0] * n
        
        # Calculate the degree of each city
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Create a list of cities and sort by degree
        cities = list(range(n))
        cities.sort(key=lambda x: -degree[x])
        
        # Assign values to cities starting from the highest degree
        total_importance = 0
        for i in range(n):
            total_importance += (n - i) * degree[cities[i]]
        
        return total_importance
        