from collections import Counter

def checkio(game_result):
    for row in game_result + zip(*game_result) + [(game_result[0][0],game_result[1][1],game_result[2][2])] + [(game_result[0][2],game_result[1][1],game_result[2][0])]:
        if row.count('X') == 3 or row.count('O') == 3:
            return row[0]
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"


