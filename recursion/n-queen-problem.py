def can_place(row, col, queens):
    for q in queens:
        q_row = q[0]
        q_col = q[1]
        q_sum = q_row + q_col
        q_diff = q_row - q_col
        if q_row == row or q_col == col or row + col == q_sum or row - col == q_diff:
            return False
    return True


def n_queen_backtrack(n, row, queens, result):
    if row == n:
        print(queens)
        result.append(queens.copy())
    else:
        for col in range(0, n):
            if can_place(row, col, queens):
                queens.append((row, col))
                n_queen_backtrack(n, row + 1, queens, result)
                # queens.append((row, col))
        # comment the line below and uncomment the line above for all solutions
        queens.pop()


def visualize_result(result):
    size = len(result[0])

    for queens in result:
        board = [[0 for x in range(size)] for y in range(size)]
        for queen in queens:
            q_row = queen[0]
            q_col = queen[1]
            board[q_row][q_col] = 1
        for i in board:
            print(i)
        print()


if __name__ == '__main__':
    res = []
    n_queen_backtrack(4, 0, [], res)
    visualize_result(res)
