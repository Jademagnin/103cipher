import sys
from .help import *

def check_args():
    if (len(sys.argv) >= 2 and sys.argv[1] == "-h"):
        print_help()
        sys.exit(0)
    if len(sys.argv) != 4:
        print("Invalid number of arguments, try ./103cipher -h")
        sys.exit(84)
    try:
        int(sys.argv[3])
    except:
        print("Invalid flag, try ./103cipher -h")
        sys.exit(84)

    if (int(sys.argv[3]) != 0 and int(sys.argv[3]) != 1):
        print("Invalid flag, try ./103cipher -h")
        sys.exit(84)

def check_decrypted_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] < 0 or matrix[i][j] > 255):
                return False
    return True
