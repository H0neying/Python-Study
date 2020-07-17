def new_a_even(a):
    return a - 1

def new_a_odd(a):
    return 2*a + 1

a_n = []
for i in range(0, 64):
    a_n.append(0)

for a in range(-10, 10):
    for n in range(1, 32):
        a_n[1] = a
        a_n[2*n] = new_a_even(a_n[n])
        a_n[2*n+1] = new_a_odd(a_n[n])

    print(f'a_1은 {a}일 때, a_20은 {a_n[20]}')

    sum = 0
    for i in a_n:
        sum += i

    if a_n[20] == 1:
        print(f'그러므로 a_1은 {a}이고, 답은 {sum}')
        break
