# astart
import numpy as np
import time
import os
import sys
import heapq

N = 3

# moves: left, right, up, down
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    return board == goal

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

def astar(start_board, x, y):
    pq = []                      # priority queue
    visited = set()

    g = 0
    h = manhattan(start_board)
    f = g + h

    heapq.heappush(pq, (f, g, start_board, x, y))
    visited.add(tuple(map(tuple, start_board)))

    while pq:
        f, g, board, bx, by = heapq.heappop(pq)

        if is_goal(board):
            print("Solution found at depth:", g)
            return

        for i in range(4):
            nx = bx + row[i]
            ny = by + col[i]

            if is_valid(nx, ny):
                new_board = [r[:] for r in board]

                # swap blank with neighbor
                new_board[bx][by], new_board[nx][ny] = (
                    new_board[nx][ny],
                    new_board[bx][by]
                )

                t = tuple(map(tuple, new_board))

                if t not in visited:
                    visited.add(t)
                    new_g = g + 1
                    new_h = manhattan(new_board)
                    new_f = new_g + new_h

                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_board, nx, ny)
                    )

    print("No solution found")

# Example
start_board = [[1, 2, 3],
               [4, 5, 6],
               [7, 0, 8]]

astar(start_board, 2, 1)


