def d(n):
    a = 0
    for value in list(str(n)):
        a = a + int(value)
        # print('n 값: {}, value 값: {}, a 값: {}'.format(n, value, a))
    return int(n) + a


produce_num = []

for count in range(1, 10001):
    produce_num.append(d(count))

for i in range(1, 10000):
    if i in produce_num:
        continue
    else:
        print(i)
