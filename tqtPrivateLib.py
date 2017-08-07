def check_prime(numberPara: int = 2) -> bool:
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