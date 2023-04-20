
"""lis = ['bob', 'non', 'con', 'son', 'mon']

lis.append('don')
print(lis)

lis.insert(2,'lon')
print(lis)

lis.remove('don')
print(lis)

lis.clear()
print(lis)"""


def move_zero(inp_lis):

    for i in inp_lis:
        if i == 0:
            inp_lis.remove(i)
            inp_list.append(0)
    return inp_list


if __name__ == '__main__':

    inp_list = [0, 1, 0, 3, 12]
    print(move_zero(inp_list))
