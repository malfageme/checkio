def min(*args, **kwargs):
    key = kwargs.get("key", None)
    l_args = list(args) if len(args) > 1 else list(args[0])
    res = l_args[0]
    for i in l_args:
        if key != None:
            res = i if key(i)<key(res) else res
        else:
            res = i if i<res else res
    return res


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    l_args = list(args) if len(args) > 1 else list(args[0])
    res = l_args[0]
    for i in l_args:
        if key != None:
            res = i if key(i)>key(res) else res
        else:
            res = i if i>res else res
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

