def get_available_positions(board, i, j):
    positions = ((1, 2), (-1, 2), (1, -2), (-1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1))
    size = len(board)
    available_positions = []
    for pos in positions:
        new_i = i + pos[0]
        new_j = j + pos[1]
        if -1 < new_i < size and size > new_j > -1 and board[new_i][new_j] == 0:
            available_positions.append((new_i, new_j))

    return available_positions


def print_board(board):
    [print(row) for row in board]
    print()


def chess_tour(board, curr_pos, count):
    positions = get_available_positions(board, curr_pos[0], curr_pos[1])

    if count == len(board) * len(board):
        print_board(board)
        return

    for pos in positions:
        count += 1
        board[pos[0]][pos[1]] = count

        chess_tour(board, (pos[0], pos[1]), count)

        board[pos[0]][pos[1]] = 0
        count -= 1


def print_all_knight_tours(board_size, start_pos=(0, 0)):
    board = [[0 for _ in range(0, board_size)] for _ in range(0, board_size)]
    board[start_pos[0]][start_pos[1]] = 1
    chess_tour(board=board, curr_pos=(0, 0), count=1)


print_all_knight_tours(board_size=5)
