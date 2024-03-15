import heapq

def solution(n, k, enemy):
    # 한 라운드씩 순회하면서 적의 수를 모두 더한다
    # 적 수의 합이 n을 넘었을 때 무적권을 사용하기 시작
    # 이때 max heap을 사용하여 가장 적이 많은 라운드에 무적권을 사용할 수 있도록 한다
    # 적 수의 합이 n을 넘고, k가 0이 되면 라운드를 더 진행할 수 없으므로 종료
    # answer는 라운드 하나를 넘길 때마다 카운트한다
    # answer를 enemy의 index 값으로 설정하면 몇 케이스는 오류가 생김
    if len(enemy) <= k:
        return len(enemy) # 모든 라운드를 막을 수 있다면 총 라운드 수를 return
    max_heap = []
    answer, enemies = 0, 0
    for i in range(len(enemy)):
        enemies += enemy[i] # 적의 수를 계속해서 더하고
        heapq.heappush(max_heap, -enemy[i]) # max heap에 라운드 당 적의 수를 저장
        if enemies > n: # 적 수의 합이 n을 넘었을 때
            if k == 0:
                break # 무적권을 쓸 수 없다면 종료
            enemies += heapq.heappop(max_heap)
            # 가장 많은 적의 수를 적 수의 합에서 빼준다
            # max heap이라 음수로 저장했기 때문에 더해주면 됨
            k -= 1 # 무적권 하나 사용
        answer += 1 # 막을 수 있는 라운드 수도 count
    return answer