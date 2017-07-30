import pprint
people1 = {'Name': 'Tuan',
           'Gender': 'Male'}
people2 = {'Name': 'Quang',
           'Gender': 'Male'}

People = {}
People["Tuan"] = people1
People["Quang"] = people2

for key, value in sorted(People.items()):
    print(key, " -> ", value)
print(People)
pprint.pprint(People)