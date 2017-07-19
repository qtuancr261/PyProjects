phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

words = ['o', 'n', 't', 'a', 'p', ' ']
for word in phrase:
    if word not in words:
        plist.remove(word)
plist.pop()
plist.insert(3, plist.pop())
plist.insert(4, plist.pop())
plist.insert(2, plist.pop())


newPhrase = "".join(plist)
print(plist)
print(newPhrase)

list1 = [22.5, 30.6, 47, 55]
list1_Ref = list1
list1_Ref.append(1000.0)
print("list1 = ", list1)
print("list1_Ref = ", list1_Ref)

list1_Copy = list1.copy()
list1_Copy.remove(1000)
print("list1 = ", list1)
print("list1_Copy = ", list1_Copy)


print(words[2:100])
print(phrase[-6:])
