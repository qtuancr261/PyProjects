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
help(check_prime)
listA = []
print(listA)
