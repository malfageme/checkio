def checkio(number):
    minute = 0
    fed_pigeons = 0
    food = number
    while True:
        minute += 1
        pigeons = fed_pigeons + minute
        if food <= pigeons:
            fed_pigeons = food if food > fed_pigeons else fed_pigeons
            break
        fed_pigeons = pigeons
        food -= fed_pigeons
    return fed_pigeons
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
