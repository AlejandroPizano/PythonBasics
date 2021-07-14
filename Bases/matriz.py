from random import randint 

filas = 5
colunmas = 5
matriz = []
val=1

for f in range(filas):
    matriz.append([])
    for c in range(colunmas):
        if f == 0:
            matriz[f].append(c+1)
            val=c+1
        else:
            matriz[f].append(None)

"""
        elif c== colunmas-1 and f!=filas -1:
            matriz[f].append(val+1)
            val=val+1
        elif f == filas-1:
            matriz[f].append(val+1)
            val = val + 1
            matriz[f].sort()
            matriz[f].reverse()
        else:
            matriz[f].append(None)


"""


def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row - 1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir = 0

    while (top <= bottom and left <= right):
        if dir == 0:
            for i in range(left, right + 1):  # moving left->right
                print(arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top += 1
            dir = 1

        elif dir == 1:
            for i in range(top, bottom + 1):  # moving top->bottom
                print(arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -= 1
            dir = 2

        elif dir == 2:
            for i in range(right, left - 1, -1):  # moving right->left
                print(arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -= 1
            dir = 3

        elif dir == 3:
            for i in range(bottom, top - 1, -1):  # moving bottom->top
                print(arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left += 1
            dir = 0


# Driver code
# Change the following array and the corresponding row and
# column arguments to test on some other input
array = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]

spiralMatrixPrint(4, 4, array)
