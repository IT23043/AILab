# aostar
N = 3
GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def is_goal(board):
    return board == GOAL

def manhattan(board):
    h = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                goal_row = (val-1)//N
                goal_col = (val-1)%N
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

def find_blank(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j

def get_neighbors(board):
    x, y = find_blank(board)
    neighbors = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            new_board = [r[:] for r in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def ao_star(board, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    t = tuple(map(tuple, board))
    if t in visited:
        return None  # dead end
    visited.add(t)

    path = path + [board]  # extend path

    if is_goal(board):
        return path  # goal reached

    # Get neighbors and sort by f = g + h
    neighbors = get_neighbors(board)
    neighbors.sort(key=lambda b: manhattan(b))

    for neighbor in neighbors:
        result = ao_star(neighbor, visited, path)
        if result:
            return result  # OR-node: pick first successful child

    return None  # no solution found

# Example usage
start_board = [[1,2,3],
               [4,0,6],
               [7,5,8]]

solution_path = ao_star(start_board)

if solution_path:
    print("Solution found! Steps:", len(solution_path)-1)
    for step, board in enumerate(solution_path):
        print(f"Step {step}, Heuristic = {manhattan(board)}")
        for row in board:
            print(row)
        print()
else:
    print("No solution found.")
