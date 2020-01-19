from itertools import combinations

f = open("a_example.in")
line_1 = f.readline()
line_2 = f.readline()
M = int(line_1.split()[0])
Str_Pizza_Slices = (line_2.split())
show = 1
Pizza_slices = []
Item_List = []
for i in Str_Pizza_Slices:
    Pizza_slices.append(int(i))
for i in Pizza_slices:
    diffs = []
for n in range(1, len(Pizza_slices) + 1):
    numbers = combinations(Pizza_slices, n)
    # list the combinations and their absolute difference to target
    for combi in numbers:
        diffs.append([combi, abs(M - sum(combi))])

diffs.sort(key=lambda x: x[1])
for item in diffs[:show]:
    Item_List = (item[0])

Type = [index for index, value in enumerate(Pizza_slices) if value in Item_List]

First = str(Item_List.__len__())

line_02 = (' '.join(map(str, Type)))

O = open("output.in", "w")
O.writelines(First)
O.writelines('\n')
O.writelines(line_02)
O.close()


O = open("output.in", "r")
print(O.readline())
O.close()

