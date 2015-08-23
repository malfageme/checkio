def digit_stack(commands):
    run_command={ 'POP': lambda s,v: s.pop() if len(s) else 0,
                  'PEEK': lambda s,v: s[-1] if len(s) else 0,
                  'PUSH': lambda s,v: 0 if s.append(v)==None else 0}
    result,stack=0,[]
    for command in commands:
        try:
            c,v = command.split()
        except:
            c,v = command,0
        
        result += run_command[c](stack,int(v))
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

