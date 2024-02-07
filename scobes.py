def scobkoruler(string_skobok):
    count = 0
    list_skobok = list(string_skobok)
    for i in range(len(list_skobok)):
        s = list_skobok[i]
        if s == '(':
            count += 1
        elif s == ')':
            count -= 1
            if count < 0:
                break
    if count == 0:
        print('yes')
    elif count != 0:
        print('no')

scobkoruler('()())(')