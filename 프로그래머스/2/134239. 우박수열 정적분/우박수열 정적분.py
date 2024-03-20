def collatz(k):
    rain = []
    while k > 1:
        rain.append(k)
        if k % 2 == 0:
            k //= 2
        else:
            k  = k * 3 + 1
    rain.append(1)
    return rain

def solution(k, ranges):
    answer = []
    rain = collatz(k)
    n = len(rain) - 1
    for r in ranges:
        a, b = r
        b = n + b
        if b < a:
            answer.append(-1)
        else:
            result = 0
            for i in range(a, b):
                result += (rain[i] + rain[i + 1]) / 2
            answer.append(result)
    return answer