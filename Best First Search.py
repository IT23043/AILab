# best first search
import heapq

GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)
# Precompute goal positions for Manhattan distance
goal_pos = {}
for i in range(3):
    for j in range(3):
        goal_pos[GOAL[i][j]] = (i, j)

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gi, gj = goal_pos[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(tuple(tuple(row) for row in new_state))

    return moves

def best_first_search(start):
    pq = []
    visited = set()

    heapq.heappush(pq, (manhattan(start), start, []))

    while pq:
        h, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (manhattan(neighbor), neighbor, path + [state])
                )

    return None

def print_solution(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

# Example start state
START = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = best_first_search(START)

if solution:
    print_solution(solution)
else:
    print("No solution found.")
