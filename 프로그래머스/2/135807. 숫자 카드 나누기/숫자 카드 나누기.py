import math

def GCD(array1, array2):
    # arrayA, arrayB의 최대공약수를 구해서
    # arrayB, arrayA의 원소들을 나눌 수 없는지 확인
    gcd = array1[0]
    for i in range(1, len(array1)):
        gcd = math.gcd(gcd, array1[i])
        # gcd는 list를 인자로 받을 수 없으므로
        # for문을 이용해 원소 하나씩 gcd를 구해준다
        if gcd == 1:
            return 0
            # 카드들의 최대공약수가 1이 되는 경우
            # 상대방 카드들의 수를 1로 모두 나눌 수 있어지므로 의미가 없다
            # 때문에 0을 반환함 (조건 만족하는 값이 없으면 0을 반환해야 함)
    for i in array2:
        if i % gcd == 0:
            return 0
            # 최대공약수가 1이 아닌 값으로 존재하더라도
            # 상대방의 카드의 수를 나눌 수 있다면 조건을 만족할 수 없음
    return gcd

def solution(arrayA, arrayB):
    A = GCD(arrayA, arrayB)
    B = GCD(arrayB, arrayA)
    return max(A, B) # 두 값 중 최댓값 반환