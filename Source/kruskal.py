graph = [(0, 1, 9), (0, 3, 24), (1, 2, 35), (1, 3, 12), (1, 6, 27), (2, 4, 31), 
        (2, 6, 12), (3, 4, 10), (4, 5, 20), (5, 6, 9)]
graph.sort(key = lambda x: x[2]) 

mst = []
n = 7 
p = [] 

for i in range(0, n+1):
    p.append(i)

def find(u):
    if u != p[u]:
        p[u] = find(p[u]) 
    return p[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

tree_edges = 0
mst_cost = 0

while True:
    if tree_edges == n-1: 
        break
    
    u,v,wt = graph.pop(0) 

    if find(u) != find(v):
        union(u,v)
        mst.append((u,v)) 
        mst_cost += wt
        tree_edges += 1

print('최소 신장 트리 : ',mst)
print('최소 신장 트리 가중치 : ', mst_cost)

notclose = input()