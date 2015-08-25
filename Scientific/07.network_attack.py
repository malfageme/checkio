def capture(matrix):
    
    count=0
    while any([matrix[i][i] for i in range(len(matrix))]):
        
        infected = [i for i in range(len(matrix)) if matrix[i][i]==0]
        neighbours = [(node,matrix[node][node]) for node in range(len(matrix)) for i in infected if matrix[i][node]==1 and matrix[node][node]>0]
        
        next = sorted(neighbours, key=lambda x: x[1])[0]
        count += next[1]
        
        #Update time to hack neighbours
        for i in range(len(matrix)):
            if i in map(lambda x: x[0], neighbours):
                matrix[i][i]-=next[1]
                
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"

