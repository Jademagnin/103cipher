def arr_to_matrix(arr, cols=None):
    if (cols == None): cols = get_matrix_size_from_arr(arr)
    matrix = []
    for i in range(len(arr)):
        if (i % cols == 0):
            matrix.append([])
        matrix[i // cols].append(arr[i])
    if (len(arr) % cols != 0):
        for i in range(cols - len(arr) % cols):
            matrix[len(arr) // cols].append(0)
    return matrix

def get_matrix_size_from_arr(arr):
    size = 0
    while (size * size < len(arr)):
        size += 1
    return size

def get_matrix_size(matrix):
    return len(matrix[0])

def reorganize_matrix(matrix):
    # entry: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    # exit: [[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]]
    res = []
    for i in range(len(matrix[0])):
        res.append([])
        for j in range(len(matrix)):
            res[i].append(matrix[j][i])
    return res

def str_to_matrix(message, cols=None):
    if (cols == None): cols = get_matrix_size_from_arr(message)
    matrix = []
    for i in message.split(" "):
        if (i != ""):
            matrix.append(int(i))
    return arr_to_matrix(matrix, cols)

def reverse_matrix(matrix, rows=3, cols=3):
    res = []
    for i in range(cols):
        res.append([])
        for j in range(rows):
            res[i].append(matrix[j][i])
    return res

def multiply_matrices(matrix1, matrix2):
    """Multiply 2 matrices"""
    res = []
    for i in range(len(matrix1)):
        res.append([])
        for j in range(len(matrix2[0])):
            res[i].append(0)
            for k in range(len(matrix1[0])):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res

def multiply_matrix_by_scalar(matrix, scalar):
    """Multiply a matrix by a scalar"""
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in range(len(matrix)):
            res[i].append(matrix[i][j] * scalar)
    return res

def round_matrix(matrix, round_to=3):
    """Round the matrix to the given number of decimals"""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], round_to)
            if (matrix[i][j] == -0.0): matrix[i][j] = 0.0
    return matrix


def cofactor_matrix(matrix):
    """Get the cofactor of a matrix"""
    cofactor = []
    for i in range(len(matrix)):
        cofactor.append([])
        for j in range(len(matrix)):
            cofactor[i].append(determinant_matrix(minor_matrix(matrix, i, j)) * ((-1) ** (i + j)))
    return cofactor

def inverse_matrix(matrix):
    """Get the inverse of a matrix"""
    if (determinant_matrix(matrix) == 0): return None
    # for matrix of size 1
    if (len(matrix) == 1): return [[1 / matrix[0][0]]]
    return multiply_matrix_by_scalar(adjugate_matrix(matrix), 1 / determinant_matrix(matrix))

def adjugate_matrix(matrix):
    """Get the adjugate of a matrix"""
    return transpose_matrix(cofactor_matrix(matrix))

def minor_matrix(matrix, i, j):
    """Get the minor of a matrix"""
    minor = []
    for k in range(len(matrix)):
        if (k != i):
            minor.append([])
            for l in range(len(matrix)):
                if (l != j):
                    minor[-1].append(matrix[k][l])
    return minor

def determinant_matrix(matrix):
    """Get the determinant of a matrix"""
    if (len(matrix) == 1):
        return matrix[0][0]
    det = 0
    for i in range(len(matrix)):
        det += matrix[0][i] * determinant_matrix(minor_matrix(matrix, 0, i)) * ((-1) ** i)
    return det

def transpose_matrix(matrix):
    """Transpose a matrix"""
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in range(len(matrix)):
            res[i].append(matrix[j][i])
    return res
