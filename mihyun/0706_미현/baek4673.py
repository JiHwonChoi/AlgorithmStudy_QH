class boj4673():
    def __init__(self):
        self._produce_num = []

    def d(n):
        a = 0
        for value in list(str(n)):
            a = a + int(value)
            # print('n 값: {}, value 값: {}, a 값: {}'.format(n, value, a))
        return int(n) + a

    def count(self):
        for count in range(1, 10001):
            self.produce_num.append(self.d(count))

    def printd(self):
        for i in range(1, 10000):
            if i in self.produce_num:
                continue
            else:
                print(i)

b=boj4673()
b.count()
b.printd()
