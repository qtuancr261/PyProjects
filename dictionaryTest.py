import sys
import math
import random
print("System platform: " + sys.platform)
print("System version: " + sys.version)
print("This py file for testing dictionary structure only :3")
person = {"name": "Thieu Quang Tuan",
          "gender": "male",
          "occupation": "student",
          "class": "D14CQCN02-N"}


print(person)
print("Name: " + person["name"])
print("Gender: " + person["gender"])
print("Occupation: " + person["occupation"])

person["age"] = 21;
print(person)
for key in person:
    print(person[key])

vowels = ["u", "e", "o", "a"]
foundVowels = {}
word = input("Give me a word: ")
for char in word:
    if char in vowels and char in foundVowels:
        foundVowels[char] += 1
    elif char in vowels and char not in foundVowels:
        foundVowels[char] = 1
print("We test for loop: for key in sorted(foundVowels)")
for key in sorted(foundVowels):
    if foundVowels[key] > 0:
        print(key, "was found ", foundVowels[key], " times")
print("Now test for loop: for key, value in sorted(foundVowels.items())")
for key, value in sorted(foundVowels.items()):
    if value > 0:
        print(key, "was found ", value, " times")
print("found = ", foundVowels)

primeNumbers = {}
isPrimeNumber = True
for i in range(100):
    number = random.randint(1, 100)
    if number < 2:
        isPrimeNumber = False
    for testValue in range(2, int(number/2) + 1, 1):
        if number % testValue == 0:
            isPrimeNumber = False
            break
    if isPrimeNumber:
        primeNumbers.setdefault(number, 0)
        primeNumbers[number] += 1
    isPrimeNumber = True
print(sorted(primeNumbers.items()))
print(primeNumbers)

