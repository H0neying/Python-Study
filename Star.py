def diamond():
    while True:
        l = int(input("�� ���� ����? "))
        if l == 0:
            print('�˾Ҿ� �׸��Ұ�')
            break

        if l%2 == 1:
            l = int((l+1)/2)
            reverse = True
            i = 1
            while(i <= l and i > 0):
                if i == l: reverse = False
                print(' ' * (l - i), '*' * (2 * i - 1))
                if reverse: i += 1
                else: i -= 1
        else:
            l = int(l/2)
            reverse = True
            i = 1
            while(i <= l and i > 0):
                if i == l:
                    print(' ' * (l - i), '*' * (2 * i - 1))
                    reverse = False
                print(' ' * (l - i), '*' * (2 * i - 1))
                if reverse: i += 1
                else: i -= 1

def pyramid():
    while True:
        l = int(input("�� ���� ����? "))
        if l == 0:
            print('�˾Ҿ� �׸��Ұ�')
            break
        i = 1
        while(i <= l and i > 0):
            print(' ' * (l - i), '*' * (2 * i - 1))
            i += 1

while True:
    s = input('���̾ư� ����? �Ƕ�̵尡 ����?')
    if s == 'd': diamond()
    elif s == 'p': pyramid()
    else: print('�� �ȱ���?')
