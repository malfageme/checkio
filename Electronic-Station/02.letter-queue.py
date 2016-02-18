# Simple class implementing a FIFO with a list
class FIFO:
    def __init__(self):
        self.fifo=[]
        
    def push(self,c):
        self.fifo.append(c)
        
    def pop(self):
        if self.fifo:
            return self.fifo.pop(0)
    
    def __str__(self):
        return "".join(self.fifo)


def letter_queue(commands):
    fifo=FIFO()
    for command in commands:
        if command=="POP":
            fifo.pop()
        else:
            fifo.push(command[-1])
    return str(fifo)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

