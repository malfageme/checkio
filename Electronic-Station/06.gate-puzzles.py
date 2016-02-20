import string

def likeness(word, word_list):
    result_list = []
    for word_check in word_list:
        res=0.0
        res += 10 if word_check[0] == word[0] else 0
        res += 10 if word_check[-1] == word[-1] else 0
        coef = float(len(word))/len(word_check)
        res += (30*coef) if coef < 1 else (30/coef)
        res += len(set.intersection(set(word),set(word_check))) * 50.0 / len(set(word+word_check))
        result_list.append(res)
    return sum(result_list)/len(result_list)
    

def find_word(message):
    message_list="".join([x for x in message.lower() if x in string.lowercase+" "]).split()
    best = ("",0.0)
    for word_i in range(len(message_list)):
        new_like = likeness(message_list[word_i],message_list[:word_i]+message_list[word_i:])
        if new_like >= best[1]:
            best = (message_list[word_i], new_like)
    return best[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"

