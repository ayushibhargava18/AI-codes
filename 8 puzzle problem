import heapq

goal=[
    [0,1,2],
    [3,4,5],
    [6,7,8]]

a=[(-1,0),(1,0),(0,-1),(0,1)]

def dist(state):
    distance=0
    for r in range(3):
        for c in range(3):
            value=state[r][c]
            if value!=0:
                goal_r,goal_c=divmod(value,3)
                distance+=abs(r-goal_r)+abs(c-goal_c)
    return distance

def neigh(state):
    zeroth=next((r,c)for r in range(3)for c in range(3)if state[r][c]==0)
    r,c=zeroth
    neighbors=[]
    
    for dr,dc in a:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            new=[row[:]for row in state]
            new[r][c],new[nr][nc]=new[nr][nc],new[r][c]
            neighbors.append(new)
    
    return neighbors

def astar(initial):
    open=[]
    closed_list=set()
    
    g=0
    h=dist(initial)
    f=g+h
    
    pq=tuple(tuple(row)for row in initial)
    
    heapq.heappush(open,(f,g,initial,[]))
    
    explored=[]
    
    while open:
        f,g,current,path=heapq.heappop(open)
        
        current_tuple=tuple(tuple(row)for row in current)
        explored.append(current)

        print(f"g(n):{g},h(n):{dist(current)},f(n):{f}")
        for row in current:
            print(row)
        print()
        
        if current==goal:
            print("\nFinal Solution Matrix:")
            for row in current:
                print(row)
            return current 
        
        closed_list.add(current_tuple)

        for neighbor in neigh(current):
            neighbor_tuple=tuple(tuple(row)for row in neighbor)
            
            if neighbor_tuple not in closed_list:
                new_g=g+1
                new_h=dist(neighbor)
                new_f=new_g+new_h                
                heapq.heappush(open,(new_f,new_g,neighbor,path+[neighbor]))

    return None  

board=[
    [7,2,4],
    [5,0,6],
    [8,3,1]]

solution=astar(board)
if solution:
    print("\nSolution found:")
    for row in solution:
        print(row)
else:
    print("No solution found")

