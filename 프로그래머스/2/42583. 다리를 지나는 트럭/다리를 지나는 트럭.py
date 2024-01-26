from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_truck = 0
    # 다리 위 트럭들의 무게
    # 원래는 sum을 사용했는데, 시간 초과로 변수를 이용해 확인하는 것으로 변경
    bridge = deque([0] * bridge_length)
    # 다리의 한칸한칸을 queue로 표현한다
    # 칸 위에 트럭이 올라가 있으면 트럭 무게 값을 넣고, 없다면 0을 넣는다
    # popleft()와 append()를 계속 시행해서 다리 길이만큼 queue 길이를 유지
    # 다만 truck_weight에서도 popleft()를 시행하기 때문에
    # 더이상 truck_weight에 원소가 없다면, 다리에 올라올 트럭이 없다면
    # append()를 시행하지 않게 되어 while문이 종료된다
    truck_weights = deque(truck_weights)
    while bridge:
        time += 1 # 1초가 지나면
        bridge_truck -= bridge.popleft()
        # 다리 위의 트럭들이 한 칸 이동
        # 다리 위의 트럭들의 무게를 업데이트
        if truck_weights: # 아직 다리에 올라올 트럭이 있다면
            if bridge_truck + truck_weights[0] <= weight:
            # bridge의 sum을 구하면
            # 현재 다리 위에 올라와 있는 트럭 무게의 합을 구할 수 있다
            # 때문에 트럭이 없는 경우는 0으로 표현하는 것
            # 현재 다리 위에 올라와 있는 트럭 무게의 합 + 다음 트럭의 무게를 구해서
            # 다리가 견딜 수 있는 무게보다 작다면 새로 트럭이 올라오는 것이 가능
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_truck += truck
                # 때문에 트럭을 꺼내서 추가하고 무게를 업데이트
            else:
                bridge.append(0)
                # 올라올 수 없다면 0을 추가 (다리 길이 유지를 위해)
    return time