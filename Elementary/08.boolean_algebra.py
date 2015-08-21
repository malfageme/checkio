OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    operations = {
        "conjunction": lambda x,y: 1 if x==y==1 else 0,
        "disjunction": lambda x,y: 0 if x==y==0 else 1,
        "implication": lambda x,y: 0 if x==1 and y==0 else 1,
        "exclusive" : lambda x,y: 1 if x!=y else 0,
        "equivalence": lambda x,y: 1 if x==y else 0
    }
    return operations[operation](x,y)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"

