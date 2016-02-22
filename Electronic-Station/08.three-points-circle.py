
from math import sqrt

def checkio(data):
    x1,y1,x2,y2,x3,y3 = [float(x) for x in data.replace("(","").replace(")","").split(",")]
    d=2.0 * (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    x0=( (x1**2+y1**2)*(y2-y3) + (x2**2+y2**2)*(y3-y1) + (x3**2+y3**2)*(y1-y2) ) / d
    y0=( (x1**2+y1**2)*(x3-x2) + (x2**2+y2**2)*(x1-x3) + (x3**2+y3**2)*(x2-x1) ) / d
    r= sqrt((x0-x1)**2+(y0-y1)**2)
    #replace this for solution
    return "(x{:+g})^2+(y{:+g})^2={:g}^2".format(round(-x0,2),round(-y0,2),round(r,2))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

