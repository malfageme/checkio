from math import acos, degrees

def checkio(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a: return [0,0,0]
    angle_a = round(degrees(acos(float(c**2 + b**2 - a**2) / (2*b*c))))
    angle_b = round(degrees(acos(float(c**2 + a**2 - b**2) / (2*c*a))))
    angle_c = 180 - angle_b - angle_a

    return sorted([angle_a, angle_b, angle_c])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

