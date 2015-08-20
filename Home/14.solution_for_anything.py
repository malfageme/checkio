
class A(object):
    def __init__(self, anything):
        pass
    def __ne__(self, b):
        return True
    def __ge__(self,b):
        return True
    def __eq__(self,b):
        return True

def checkio(anything):
    return A(anything)
    
if __name__ == '__main__':
    import re, math
    
    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'
    
    print('NO WAY :(')
