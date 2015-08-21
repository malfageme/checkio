def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    # Copy the initial pyramid and reverse it in the process
    weight = [list(row) for row in pyramid[::-1]]
    for row_i in range (1,len(pyramid)):
        for cel_i in range(len(weight[row_i])):
            weight[row_i][cel_i] += max(weight[row_i-1][cel_i], weight[row_i-1][cel_i+1])
    return weight[-1][0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

