import math
from itertools import permutations

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    permu = set() # 0이 있을 경우 생기는 중복을 제거
    numbers = [i for i in numbers] # 숫자는 split이 안 됨
    for i in range(1, len(numbers)+1): # 조합의 길이
        for j in permutations(numbers, i):
            number = int(''.join(j)) # 숫자를 생성해서
            permu.add(number) # set에 추가
    for i in permu:
        if prime(i):
            answer += 1 # 소수면 count
    return answer