number = 0


def check_prime_number():
    """Just test it"""
    print("Perform check with: ", number)
    if number < 2:
        return False
    for checkValue in range(2, int(number / 2) + 1, 1):
        if number % checkValue == 0:
            return False
    return True


def check_prime(numberPara:int = 2) -> bool:
    """With argument"""
    if numberPara < 2:
        return False
    for checkValue in range(2, int(numberPara / 2) + 1, 1):
        if numberPara % checkValue == 0:
            return False
    return True


def searchLetters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the letters found in phrase"""
    return set(letters).intersection(set(phrase))


if check_prime(int(input("Give me the number: "))):
    print("-> a prime number")
else:
    print("-> not a prime number")

if check_prime():
    print("-> a prime number")
else:
    print("-> not a prime number")

if check_prime_number():
    print("-> a prime number")
else:
    print("-> not a prime number")
help(searchLetters)
phrase = input("Input a phrase: ")
print(searchLetters(phrase))
