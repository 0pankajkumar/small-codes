# 1 2 3
# 4 5 6
# 7 8 9

# 3 6 9
# 2 5 8
# 1 4 7

# 7 4 1
# 8 5 2
# 9 6 3

def rotate(start_point, rangex, matrix):
    # print(start_point, rangex)
    
    # p = 0
    # for i in range(start_point, rangex+1):
    #     # print(start_point, p+i, end=" ")
    #     # print(p+i, start_point)
    #     v = start_point
    #     w = p+i
    #     x = p+i
    #     y = start_point

    #     temp = matrix[x][y]
    #     matrix[x][y] = matrix[v][w]
    #     matrix[v][w] = temp

    p = 0
    for i in range(start_point, rangex+1):
        # print(start_point, p+i, end=" ")
        # print(p+i, rangex)
        v = start_point
        w = p+i
        x = p+i
        y = rangex

        temp = matrix[x][y]
        matrix[x][y] = matrix[v][w]
        matrix[v][w] = temp
    return

    p = 0
    for i in range(start_point, rangex+1):
        # print(rangex, p+i, end=" ")
        # print(p+i, rangex)
        v = rangex
        w = p+i
        x = p+i
        y = rangex

        temp = matrix[x][y]
        matrix[x][y] = matrix[v][w]
        matrix[v][w] = temp

    p = 0
    for i in range(start_point, rangex+1):
        # print(p+i, start_point, end=" ")
        # print(rangex, p+i)
        v = p+i
        w = start_point
        x = rangex
        y = p+i
        
        temp = matrix[x][y]
        matrix[x][y] = matrix[v][w]
        matrix[v][w] = temp
    

        

    

def start_rotation(matrix):
    n = len(matrix)
    rangex = n-1
    end_at = n // 2

    for start_point in range(end_at):
        rotate(start_point, rangex, matrix)
        break
        rangex -= 1

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(matrix)
start_rotation(matrix)
print(matrix)

