import random
import sys
print(sys.platform)
print("For the purpose of Creating sets Efficiently")
foundOddNums = []
for time in range(5):
    inputNum = int(input("Give me an integer: "))
    if inputNum % 2 == 1:
        foundOddNums.append(inputNum)
print(foundOddNums)

initSet = {'t', 'u', 'a', 'n', 'u', 'n'}
print(initSet)

initSet2 = set("quangtuan")
print(initSet2)

initSet3 = set([15, 33, 15, 52, 102, 52])
print(initSet3)

vowels = set("ueoai")
word = input("Let input a word: ")
unionSet = vowels.union(set(word))
print("unionSet = vowels.union(set(word)) => ",sorted(unionSet))

diffSet = vowels.difference(set(word))
print("diffSet = vowels.difference(set(word)) => ",sorted(list(diffSet)))

intersectionSet = vowels.intersection(word)
print("intersectionSet = vowels.intersection(word)", intersectionSet)

