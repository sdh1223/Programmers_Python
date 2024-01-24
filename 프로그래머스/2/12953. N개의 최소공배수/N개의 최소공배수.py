def solution(arr):
    m = max(arr)
    for i in arr:
        if m % i == 0:
            arr.remove(i) # 해당 수의 배수가 arr 안에 존재하는 경우 삭제
    n = 1
    while True:
        n += 1
        multiple = m * n # arr 내 가장 큰 수의 배수를 구해서
        common = True
        for i in arr:
            if multiple % i != 0:
                common = False
        if common: # 나머지 수들도 해당 배수의 약수인 경우에 값 반환
            return multiple