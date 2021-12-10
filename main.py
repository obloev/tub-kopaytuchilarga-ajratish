n = int(input())
l = len(str(n))

f = lambda i, n: print(str(n) + ' ' * (l - len(str(n)) + 1) + f'| {i}')

while n != 1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            f(i, n)
            n //= i
            break
    else:
        f(n, n)
        n = 1
        break

f('', 1)