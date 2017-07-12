emptyList = []
print("An empty list in Python: ")
for obj in emptyList:
    print(obj)

print("A normal list in Python: ")
normalList = [15, 200.2, -320, 400]
for obj in normalList:
    print(obj)

print("A string list in Python: ")
stringList = ["GTX 460", "GTX 560", "GTX 660", "GTX 760", "GTX 960", "GTX 1060"]
for obj in stringList:
    print(obj)

print("A mixed-type list in Python: ")
mixedList = ["08/07/2017", "Nvidia", 220, 15.06, "ThieuQuangTuan"]
for obj in mixedList:
    print(obj)

print("Lists inside of a list")
lists = [[15, 22, 2017], ["RX460", "RX470"], [15.2, "AMD", 2016]]
for ls in lists:
    for obj in ls:
        print(obj)

vowels = ['u', 'e', 'o', 'a', 'i']
checkWord = input("Give me a word to search fo vowels: ")
checkWord += " GT "
foundChar = []
for char in checkWord:
    if char in vowels and char not in foundChar:
        foundChar.append(char)
        vowels.remove(char)
for char in foundChar:
    print(char, checkWord.capitalize())
print("vowels list contains: ",vowels)
print("the last vowel char we found: ", foundChar[len(foundChar) - 1])
print("Now we remove that one from the foundChar list: ", foundChar.pop(), foundChar)
print("We remove everything form foundChar list")
for char in range(len(foundChar)):
    foundChar.pop()
print("foundChar = ", foundChar)
print("Rebuild it again")
foundChar.extend(['u', 'e', 'o', 'a', 'i'])
print("Now foundChar = ", foundChar)