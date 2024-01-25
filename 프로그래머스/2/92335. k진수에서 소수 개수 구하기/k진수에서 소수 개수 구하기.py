import math

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def convert(num, base):
        temp = "0123456789ABCDEF"
        q, r = divmod(num, base)
        if q == 0:
            return temp[r]
        else:
            return convert(q, base) + temp[r]

def solution(n, k):
    count = 0
    num = convert(n, k)
    num_list = num.split('0')
    # 0이 주변에 있는 경우를 파악한다는 것은
    # 결국 0을 기준으로 자르면 된다는 것을 의미
    for i in num_list:
        if i != '' and prime(int(i)):
        # 0이 겹쳐 있는 경우 공백이 생김
        # 따라서 이 경우를 제거
            count += 1
    return count