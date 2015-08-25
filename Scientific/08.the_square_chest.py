def checkio(lines_list):
    """Return the quantity of squares"""
    lines_list = [sorted(x) for x in lines_list]
    count=0
    for c in range(1,4):
        for r in range(0,3):
            # Check every possible length
            for s in range(1,4-max(c-1,r)):
                #print "Start on: (%d,%d) Length: %d" % (r+1,c,s)
                #print "top edge:",    all([([r*4+c+i, r*4+c+i+1] in lines_list) for i in range(s)])
                #print "bottom edge:", all([([(r+s)*4+c+i, (r+s)*4+c+i+1] in lines_list) for i in range(s)])
                #print "left edge:",   all([([(r+i)*4+c, (r+i+1)*4+c] in lines_list) for i in range(s)])
                #print "right edge:",  all([([(r+i)*4+c+s, (r+i+1)*4+c+s] in lines_list) for i in range(s)])
                top_edge = all([([r*4+c+i, r*4+c+i+1] in lines_list) for i in range(s)])
                bottom_edge = all([([(r+s)*4+c+i, (r+s)*4+c+i+1] in lines_list) for i in range(s)])
                left_edge = all([([(r+i)*4+c, (r+i+1)*4+c] in lines_list) for i in range(s)])
                right_edge = all([([(r+i)*4+c+s, (r+i+1)*4+c+s] in lines_list) for i in range(s)])
                if all([top_edge, bottom_edge, left_edge, right_edge]):
                    #print "Square of size %d in %d" % (s,r*4+c)
                    count+=1
    return count


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
