"""
• Transcript the key into numbers using the ASCII table,
• Convert the numbered key into a square matrix, the smallest possible size, and filling the lines first,
• Transcript the clear message into numbers using the ASCII table,
• Convert the numbered message into a matrix; its number of columns should fit the key matrix size,
and its number of lines should be as small as possible,
• Multiply the 2 matrices, and write the answer linearly to get the encrypted message

./103cipher “26690 21552 11810 19718 16524 13668 25322 22497 14177
28422 26097 16433 12333 11874 5824 27541 23754 14452 17180 17553 7963 26387 22047
13895 18804 14859 12033 27738 23835 15331 21487 16656 13238 21696 15978 6976 20750
23307 14093 16788 11751 8981 22339 24861 15619 21295 16524 13668 26403 23610 15190
29451 25764 16106 26394 23307 14093 3312 5106 5014” “Homer S” 1
Key matrix:
0.0 0.0 0.012
-0.004 0.012 -0.012
0.013 -0.013 0.004
Decrypted message:
Just because I don't care doesn't mean I don't understand.
"""

from .matrix import *

def decrypt_matrix(encrypted_matrix, key_inv):
    """Decrypt the message using the key"""
    decrypted_matrix = multiply_matrices(encrypted_matrix, key_inv)
    decrypted_matrix = round_matrix(decrypted_matrix)
    return decrypted_matrix

def matrix_to_str(matrix):
    """Convert a matrix to a string"""
    res = ""
    for i in matrix:
        for j in i:
            if (j >= 0 and j <= 127): res += chr(int(j))
    return res
