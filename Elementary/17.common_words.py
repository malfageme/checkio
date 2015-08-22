def checkio(first, second):
    # Probably much better with sets
    return ','.join(sorted([word for word in first.split(',') if word in second.split(',')]))
   
def checkio_sets(first, second):
    # A solution using sets. Must get used to them
    first_set=set(first.split(','))
    second_set=set(second.split(','))
    return ','.join(sorted(first_set.intersection(second_set)))
 
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"

    assert checkio_sets(u"hello,world", u"hello,earth") == "hello", "Sets - Hello"
    assert checkio_sets(u"one,two,three", u"four,five,six") == "", "Sets - Too different"
    assert checkio_sets(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "Sets - 1 2 3"

