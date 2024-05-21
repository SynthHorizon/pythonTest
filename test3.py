cool_list = [1, 2, 3, 4, 5]

length = len(cool_list)

while length > 0:
    i = length
    print(i)
    cool_list.remove(cool_list[i - 1])
    length = len(cool_list)
    i -= 1

print(cool_list)