class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root != j_root:
            self.parent[i_root] = j_root
            return True
        return False

def kruskals_mst(edges, num_vertices):
    edges.sort()
    ds = DisjointSet(num_vertices)
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if ds.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
    return mst_weight, mst_edges

if __name__ == '__main__':
    edges = [
        (4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7),
        (7, 2, 3), (2, 2, 8), (4, 3, 4), (14, 3, 5),
        (9, 4, 5), (10, 5, 6), (1, 6, 7), (2, 6, 8),
        (6, 7, 8)
    ]
    num_vertices = 9
    weight, mst_edges = kruskals_mst(edges, num_vertices)
    print(f"Minimum Spanning Tree Weight (Kruskal's with Union-Find): {weight}")
    print("Edges in MST:")
    print(mst_edges)
