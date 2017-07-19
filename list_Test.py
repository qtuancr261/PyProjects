string = "Let see a string"
List = list(string)
print(List)
print(List[0:3])
print("".join(List[0:3]))
print("|".join(List[4:]))
print("|".join(string[4:]))
print(string[::-1])
print(List[::-1])

inputSTR = input("Just input a word: ")
print(inputSTR)
if inputSTR.capitalize() == inputSTR[::-1].capitalize():
    print("It's a symmetric string - ignore case sensitive")
else:
    print("Just forget this word")