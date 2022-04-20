a = [chr(i) for i in range(48, 58)]
a += [chr(i) for i in range(65, 71)]


def sist(n, s):
    if n >= 1:
        sist(n // s, s)
        print(a[n % s], end='')


sist(int(input()), int(input()))
