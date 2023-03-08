from .decrypt import matrix_to_str
from .matrix import round_matrix

def display_matrix_key(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (j == len(matrix[0]) - 1):
                print(matrix[i][j], end="")
            else:
                print(matrix[i][j], end="\t")
        print()

def display_encrypted_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == len(matrix) - 1 and j == len(matrix[0]) - 1):
                print(matrix[i][j], end="")
            else:
                print(matrix[i][j], end=" ")

def display_encrypted(encrypted_matrix, matrix_key):
    print("Key matrix:")
    display_matrix_key(matrix_key)
    print()
    print("Encrypted message:")
    display_encrypted_matrix(encrypted_matrix)
    print()


def display_decrypted(decrypted_matrix, matrix_key):
    print("Key matrix:")
    matrix_key = round_matrix(matrix_key)
    display_matrix_key(matrix_key)
    print()
    print("Decrypted message:")
    print(matrix_to_str(decrypted_matrix))
