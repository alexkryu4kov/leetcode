from pprint import pprint

BOARD_SIZE = 8

# Все возможные ходы коня
move_x_map = [2, 1, -1, -2, -2, -1, 1, 2]
move_y_map = [1, 2, 2, 1, -1, -2, -2, -1]


def is_safe(x: int, y: int, board: list[list[int]]) -> bool:
    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == -1:
        return True
    return False


def solve_problem(
    step_number: int,
    current_x: int,
    current_y: int,
    board: list[list[int]]
) -> bool:
    if step_number == BOARD_SIZE**2:
        return True

    for i in range(8):  # здесь 8 - это кол-во возможных ходов коня
        new_x = current_x + move_x_map[i]
        new_y = current_y + move_y_map[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = step_number
            if solve_problem(step_number+1, new_x, new_y, board):
                return True
            board[new_x][new_y] = -1  # в случае неуспеха
    return False


board = [[-1 for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]
board[0][0] = 0
step_number = 1

pprint(board)

solve_problem(step_number, 0, 0, board)
pprint(board)
