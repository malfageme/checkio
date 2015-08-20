def checkio(text):
    my_dict = {}
    for c in text:
        if c.isalpha() and c != " ":
            c_ = c.lower()
            if c_ in my_dict:
                my_dict[c_] += 1
            else:
                my_dict[c_] = 0
    max_count = max(my_dict.values())
    return sorted([k for (k,v) in my_dict.items() if v == max_count])[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")

