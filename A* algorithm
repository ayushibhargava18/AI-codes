def que(graph, start, goal, h):
    n=len(graph)
    list=[(start, 0)]  
    parent={start: None}
    costyet={start: 0}

    while list:
        list.sort(key=lambda x: x[1])
        current,_=list.pop(0)

        if current==goal:
            break

        for neighbor in range(n):
            if graph[current][neighbor]!=0:  
                newcost=costyet[current]+graph[current][neighbor]
                if neighbor not in costyet or newcost<costyet[neighbor]:
                    costyet[neighbor]=newcost
                    score=newcost+h[neighbor]
                    list.append((neighbor, score))
                    parent[neighbor]=current

    path=[]
    while current is not None:
        path.append(current)
        current=parent[current]
    path.reverse()

    return path, costyet[goal]

graph=[
    [0, 6, 0, 0, 0, 3, 0, 0, 0, 0],  
    [6, 0, 3, 2, 0, 0, 0, 0, 0, 0],  
    [0, 3, 0, 1, 5, 0, 0, 0, 0, 0],  
    [0, 2, 1, 0, 8, 0, 0, 0, 0, 0], 
    [0, 0, 5, 8, 0, 0, 0, 0, 5, 3], 
    [3, 0, 0, 0, 0, 0, 1, 7, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 3, 0], 
    [0, 0, 0, 0, 0, 7, 0, 0, 2, 0],  
    [0, 0, 0, 0, 5, 0, 3, 2, 0, 3],  
    [0, 0, 0, 0, 5, 0, 0, 0, 3, 0]   ]

h=[10,8,5,7,3,6,5,3,1,0]
start=0 
goal=9   
path,cost=que(graph, start, goal, h)

nodenames=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
pathnames=[nodenames[node] for node in path]

print("Path:", pathnames)
print("Total cost:", cost)
