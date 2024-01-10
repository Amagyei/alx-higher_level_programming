#!/usr/bin/python3
<<<<<<< HEAD

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
=======
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d} ".format(matrix[i][j]), end="")
        print()

>>>>>>> refs/remotes/origin/main
