import sys
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
found = {"u": 0,
         "e": 0,
         "o": 0,
         "a": 0,
         "i": 0}
word = input("Give me a word: ");
for char in word:
    if char in vowels:
        found[char] += 1
for key in sorted(found):
    if found[key] > 0:
        print(key, "was found ", found[key], " times")

for key, value in sorted(found.items()):
    if value > 0:
        print(key, "was found ", value, " times")

