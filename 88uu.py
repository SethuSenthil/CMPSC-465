# we assume the multiply function has a O(log n) time complexity
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = power(a, n // 2)
        return multiply(temp, temp)
    else:
        temp = power(a, n // 2)
        return multiply(multiply(temp, temp), a)