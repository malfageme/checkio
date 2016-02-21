
def find_four(data):
    for i in range(len(data)-3):
        if data[i:i+4].count(data[i])==4:
            return True
    return False

def checkio(matrix):
    #replace this for solution
    for row in matrix:
        if find_four(row):
            return True
    for col in zip(*matrix):
        if find_four(col):
            return True
    # Get diagonals
    for row_i in range(3,len(matrix)):
        data = []
        for i in range(row_i+1):
            data.append(matrix[row_i-i][i])
        if find_four(data):
            return True
    for row_i in range(1,len(matrix)-3):
        data = []
        for i in range(len(matrix)-row_i):
            data.append(matrix[row_i+i][len(matrix)-i-1])
        if find_four(data):
            return True
    for row_i in range(0,len(matrix)-3):
        data = []
        for i in range(len(matrix)-row_i):
            data.append(matrix[row_i+i][i])
        if find_four(data):
            return True
    for col_i in range(1,len(matrix)-3):
        data = []
        for i in range(len(matrix)-col_i):
            data.append(matrix[i][col_i+i])
        if find_four(data):
            return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

