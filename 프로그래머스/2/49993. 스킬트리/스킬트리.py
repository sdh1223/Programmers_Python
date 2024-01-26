def solution(skill, skill_trees):
    count = 0
    for tree in skill_trees:
        tree_check = ""
        # 올바른 스킬 트리인지 확인하기 위한 문자열
        # for문 시작마다 초기화
        for sk in tree:       
            if sk in skill:
                tree_check += sk
        if skill[:len(tree_check)] == tree_check:
        # 처음부터 tree_check의 길이만큼 slice한다
        # 선행 스킬 때문에 무조건 맨 처음부터 확인해야 한다
        # 예를 들어, skill = "CBD", sk = "BDA"인 경우
        # tree_check = "BD", skill[:len(tree_check)] = "CB"로 불가능하다
        # 이는 B 스킬 이전에 C 스킬을 배워야 하기 때문이다
        # 그러므로 무조건 0번째 index부터 확인해야 한다
            count += 1
    return count