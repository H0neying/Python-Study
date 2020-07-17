def diamond():
    while True:
        l = int(input("몇 줄을 원해? "))
        if l == 0:
            print('알았어 그만할게')
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
        l = int(input("몇 줄을 원해? "))
        if l == 0:
            print('알았어 그만할게')
            break
        i = 1
        while(i <= l and i > 0):
            print(' ' * (l - i), '*' * (2 * i - 1))
            i += 1

while True:
    s = input('다이아가 좋아? 피라미드가 좋아?')
    if s == 'd': diamond()
    elif s == 'p': pyramid()
    else: print('다 싫구나?')
