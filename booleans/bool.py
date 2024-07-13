def dup(lst, i):
    if i in lst:
        return True
    return False

l = ['a', 'b', 'c', 'd']
i = 'a'

check = dup(l, i)
# print(check)

if check:
    print('duplicate')
else:
    print('New')