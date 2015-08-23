def checkio(time_string):
    format_number=lambda n,p: "{0:0{1}b}".format(int(n),p)
    
    h,m,s = time_string.split(":")
    h = ('0' if len(h)==1 else '') + h
    m = ('0' if len(m)==1 else '') + m
    s = ('0' if len(s)==1 else '') + s

    result = ""
    result += format_number(h[0],2) + ' '
    result += format_number(h[1],4) + ' '
    result += ': ' + format_number(m[0],3) + ' '
    result += format_number(m[1],4) + ' '
    result += ': ' + format_number(s[0],3) + ' '
    result += format_number(s[1],4)
    return result.replace('1','-').replace('0','.')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"


