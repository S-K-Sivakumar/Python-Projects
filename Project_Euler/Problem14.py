def euler_14(n):
    if n % 2 == 0:
        n *= 0.5
    elif n % 2 == 1:
        n = 3 * n + 1
    while True:
        if n > 1:
            euler_14(n)

euler_14(5)
