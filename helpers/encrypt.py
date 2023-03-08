"""
• Transcript the key into numbers using the ASCII table,
• Convert the numbered key into a square matrix, the smallest possible size, and filling the lines first,
• Transcript the clear message into numbers using the ASCII table,
• Convert the numbered message into a matrix; its number of columns should fit the key matrix size,
and its number of lines should be as small as possible,
• Multiply the 2 matrices, and write the answer linearly to get the encrypted message
"""

from .matrix import *

def transcript_in_ascii(key):
    key_numbers = []
    for i in range(len(key)):
        key_numbers.append(ord(key[i]))
    return key_numbers

def str_to_encrypted_matrix(message, key):
    matrix_key = arr_to_matrix(transcript_in_ascii(key))
    matrix_msg = arr_to_matrix(transcript_in_ascii(message), len(matrix_key))
    matrix_key = reverse_matrix(matrix_key, len(matrix_key), len(matrix_key[0]))
    matrix_msg = reverse_matrix(matrix_msg, len(matrix_msg), len(matrix_msg[0]))
    res = multiply_matrices(matrix_key, matrix_msg)
    return reorganize_matrix(res)
