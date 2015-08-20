def safe_pawns(pawns):
    pawns_list = [(int(r)-1,ord(c)-ord('a')) for c,r in pawns]
    return sum([1 for pawn in pawns_list if (pawn[0]-1,pawn[1]-1) in pawns_list or (pawn[0]-1,pawn[1]+1) in pawns_list])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

