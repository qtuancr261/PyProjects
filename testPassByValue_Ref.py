import sys


def pass_by_int(arg: int):
    print('Before: ', arg)
    arg=1000
    print('After: ', arg)


def pass_by_list(arg: list):
    print('Before: ', arg)
    arg.append('Crush cua Thieu la ai ?')
    print('After: ', arg)


def pass_by(arg):
    print('Before: ', arg)
    arg = arg * 10
    print('After: ', arg)


print(sys.platform)
print('Let demonstrate Call-By-Value')
value = 100
pass_by_int(value)
print('Let see the value after passing it to pass_by_int(int) function: ', value)
text = list('Cau hoi kho trong ngay -> ')
pass_by_list(text)
print('Let see the text after passing it to pass_by_str(str) function: ', text)
#-------------------------------------------------
print('After that, python will show us a magic: ')
pass_by(value)
print('Outside pass_by(value): value = ', value)
#---------------------------------------------------
listNums = [15, 20, 25, 30, 35, 40]
pass_by(listNums)
print('Outside pass_by(listNums): listNums = ', listNums)
print('Type: ', type(listNums))