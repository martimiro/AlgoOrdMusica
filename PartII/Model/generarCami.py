import random

def generarCami(graph, attempts=1000):
    nodes = list(graph.nodes)
    
    for _ in range(attempts):
        path = [random.choice(nodes)]
        visited = set(path)
        
        while len(path) < len(nodes):
            neighbors = list(graph.neighbors(path[-1]))
            random.shuffle(neighbors)
            for neighbor in neighbors:
                if neighbor not in visited:
                    path.append(neighbor)
                    visited.add(neighbor)
                    break
            else:
                break
        
        if len(path) == len(nodes):
            return path
    
    return None
