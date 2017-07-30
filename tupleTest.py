from datetime import datetime

print(datetime.today().time())
vowels = ['u', 'e', 'o', 'a', 'i']
print("vowels = ", vowels, " -> square brackets ", type(vowels))
print()
vowels2 = ('u', 'e', 'o', 'a', 'i')
print("vowels2 = ", vowels2, " -> parentheses ", type(vowels2))

print(" As tuples are closely related to lists")

print("Be careful with this ->it's just a comma: ")
str = ("Python")
print("str = (\"Python\")", type(str))

str2 = ("Python",)
print("str2 = (\"Python\"),", type(str2))
