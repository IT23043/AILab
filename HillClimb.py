# hill climb
N = 3
row = [0, 0, -1, 1]  
col = [-1, 1, 0, 0]

GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def is_goal(board):
    return board == GOAL


def manhattan(board):
    h = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                goal_row = (val - 1) // N
                goal_col = (val - 1) % N
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
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            new_board = [r[:] for r in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors


def hill_climbing(start_board, max_steps=1000):
    current = start_board
    for step in range(max_steps):
        print(f"Step {step}, heuristic: {manhattan(current)}")
        if is_goal(current):
            print("Goal reached!")
            return current

        neighbors = get_neighbors(current)
        # Choose neighbor with lowest heuristic
        next_board = min(neighbors, key=manhattan)

        # If no improvement, local maxima reached
        if manhattan(next_board) >= manhattan(current):
            print("Stuck at local maxima or plateau.")
            return current

        current = next_board

    print("Max steps reached without solution.")
    return current


start_board = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

hill_climbing(start_board)
