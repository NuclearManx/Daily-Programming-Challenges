def num_paths_calculator(matrix):
    num_columns = len(matrix[0])
    num_rows = len(matrix)

    if matrix[0][0] != 0 or matrix[num_rows - 1][num_columns - 1] != 0:
        return -1

    def next(pos_x, pos_y):
        val = 0
        if (pos_x == num_columns - 1) and (pos_y == num_rows - 1) and (matrix[pos_y][pos_x] == 0):
            return 1

        try:
            if matrix[pos_y][pos_x + 1] == 0:
                val += next(pos_x + 1, pos_y)
        except IndexError:
            pass
        
        try:
            if matrix[pos_y + 1][pos_x] == 0:
                val += next(pos_x, pos_y + 1)
        except IndexError:
            pass

        return val

    val = next(0, 0)

    return val

def matrix_printer(matrix):
    output = "\n"
    for row in matrix:
        output += f"{row}\n"
    return output

def num_paths_tester(matrix, expected):
    print(f"Matrix: {matrix_printer(matrix)}has {num_paths_calculator(matrix)} paths. Should be {expected}.\n")


example_matrix = [[0, 0, 1],
                  [0, 0, 1],
                  [1, 0, 0]]

non_square_matrix = [[0, 0, 1],
                     [1, 0, 0]]

blocked_entrance_matrix = [[0, 1, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0]]

blocked_exit_matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 1, 0]]

blocked_exit_matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]

non_valid_start_matrix = [[1, 0, 1],
                          [1, 0, 0]]

non_valid_finish_matrix = [[0, 0, 1],
                           [1, 0, 1]]

num_paths_tester(example_matrix, 2)
num_paths_tester(non_square_matrix, 1)
num_paths_tester(blocked_entrance_matrix, 0)
num_paths_tester(blocked_exit_matrix, 252)#Not sure
num_paths_tester(non_valid_start_matrix, -1)
num_paths_tester(non_valid_finish_matrix, -1)
