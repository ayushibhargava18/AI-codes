from collections import deque

def waterjugs(vol1, vol2, targetvol):
    visited = set()
    queue = deque([(0, 0, 0, [])])  

    while queue:
        jug1, jug2, steps, path = queue.popleft()

        if jug1 == 0 and jug2 == targetvol:
            print(f"Minimum steps: {steps}")
            for step in path:
                print(f"Jug1: {step[0]}, Jug2: {step[1]}")
            return steps
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        if jug1 < vol1:
            queue.append((vol1, jug2, steps + 1, path + [(vol1, jug2)]))
        
        if jug2 < vol2:
            queue.append((jug1, vol2, steps + 1, path + [(jug1, vol2)]))
        
        if jug1 > 0:
            queue.append((0, jug2, steps + 1, path + [(0, jug2)]))
        
        if jug2 > 0:
            queue.append((jug1, 0, steps + 1, path + [(jug1, 0)]))
        
        if jug1 > 0 and jug2 < vol2:
            pour = min(jug1, vol2 - jug2)
            queue.append((jug1 - pour, jug2 + pour, steps + 1, path + [(jug1 - pour, jug2 + pour)]))
        
        if jug2 > 0 and jug1 < vol1:
            pour = min(jug2, vol1 - jug1)
            queue.append((jug1 + pour, jug2 - pour, steps + 1, path + [(jug1 + pour, jug2 - pour)]))

    return -1 

vol1 = 4  
vol2 = 3  
target = 2 

steps = waterjugs(vol1, vol2, target)

if steps == -1:
    print("No solution found.")
