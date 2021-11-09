n = int(input('Введите n: '))
while n >= 10:
    res = 0
    while n >= 10 :
        res += n % 10
        n //= 10
    n += res
print(n)
