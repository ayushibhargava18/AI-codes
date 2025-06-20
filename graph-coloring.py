graph = [
    [0, 7, 0, 0, 1], 
    [7, 0, 3, 0, 8],   
    [0, 3, 0, 6, 2],   
    [0, 0, 6, 0, 7],    
    [1, 8, 2, 7, 0],
]
n=len(graph)
result=[-1]*n
result[0]=0

for u in range (1,n):
    avail=[False]*n
    for v in range(n):
        if graph[u][v]!=0 and result[v]!=-1:
            avail[result[v]]=True
    for c in range(n):
        if not avail[c]:
            result[u]=c
            break

for u in range(n):
    print(f"Vertex {u} Color {result[u]}")
