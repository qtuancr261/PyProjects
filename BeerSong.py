print("range(10, 0, -1) : ")
for num in range(10, 5, -1):
    print(num)
print("--------------------\nrange(10, 20)")
for num in range(10, 15):
    print(num)

print("--------------------\nrange(4)")
for num in range(4):
    print(num)
print("Beer Song Python");
word = "bottles"
for beer_num in range(4, 0, -1):
    print(beer_num, word, " of beer on the wall")
    print(beer_num, word, " of beer")
    print("Take one down.\nPass it around")
    if beer_num == 1:
        print("No more bottles of beer on the wall")
    elif beer_num == 2:
        word = "bottle"

