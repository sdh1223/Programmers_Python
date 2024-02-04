from collections import Counter

def solution(weights):
    # 단순히 가능한 수열을 모두 구해 계산하면 시간초과 오류가 발생한다
    # 때문에 Counter를 이용해 원소의 개수를 세서 답을 구한다
    answer = 0
    count = Counter(weights) 
    for i in count.values():
        if i != 1:
        # 같은 수가 1개 이상 존재하는 경우
        # {100, 100}과 같이 같은 거리에 마주보고 앉는 쌍을 만들 수 있다
            answer += i * (i-1) // 2
            # # 이때 nC2의 조합만큼 만드는 것이 가능하므로
            # n * (n-1) / 2를 계산해준다
    weights = set(weights)
    # 같은 거리 쌍을 모두 만들었으므로 중복을 제거해도 된다
    for i in weights:
        pair1, pair2, pair3 = i*2/3, i*3/4, i*1/2
        # 거리는 2, 3, 4의 세 가지이기 때문에,
        # 거리 비는 이 세가지밖에 나오지 않는다
        # {180, 360}과 {360, 180}은 같은 경우이므로,
        # 거리 비도 1:2, 2:1로 구분하지 않고 한 가지만 판단한다
        if pair1 in weights:
            answer += count[i] * count[pair1]
        if pair2 in weights:
            answer += count[i] * count[pair2]
        if pair3 in weights:
            answer += count[i] * count[pair3]
            # 만약, {180, 360}의 비를 만든다고 하면
            # 총 개수는 180의 수 * 360의 수가 될 것이다
            # weights 자체는 중복을 제거해서 순환하는 데 소요되는 시간을 줄이고
            # 개수는 앞서 만든 count를 이용해 계산한다
    return answer