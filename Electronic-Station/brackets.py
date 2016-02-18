def checkio(expression):
    brackets=("()","[]","{}")
    # Get only the brackets on initial string
    new_text="".join(x for x in expression if x in "".join(brackets))
    
    # Remove pairs of brackets until all are gone (True) or until we can't
    # remove any more because they are not correctly sorted
    post_len=len(new_text)
    while post_len > 0:
        pre_len=len(new_text)
        for bracket in brackets:
            new_text=new_text.replace(bracket,"")
        post_len=len(new_text)
        if post_len==pre_len:
            return False
    return True
​
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"

