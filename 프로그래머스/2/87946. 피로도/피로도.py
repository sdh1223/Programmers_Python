from itertools import permutations

def solution(k, dungeons):
    count_list = []
    for permu in permutations(dungeons, len(dungeons)):
    # permutation을 통해 전부 확인해서 최댓값을 찾음
        count = 0
        now = k
        for need, use in permu:
            if now >= need:
                count += 1
                now -= use
            count_list.append(count)
    return max(count_list)