#You can import some modules or create additional functions


def checkio(number):
    result = "Fizz" if number % 3 == 0 else ""
    result += (" " if len(result) else "") + "Buzz" if number % 5 == 0 else ""
    return result if len(result) else str(number)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"

