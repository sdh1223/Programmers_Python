def solution(n):
    next = n
    b = bin(n)[2:]
    one = b.count('1')
    while True:
        next += 1
        b = bin(next)[2:]
        ONE = b.count('1')
        if ONE == one:
            break
    return next