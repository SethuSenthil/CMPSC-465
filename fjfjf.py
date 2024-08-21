def multiply(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    elif b % 2 == 0:
        k = b // 2
        return 2 * multiply(a, k)
    else:
        k = (b - 1) // 2
        return a + 2 * multiply(a, k)