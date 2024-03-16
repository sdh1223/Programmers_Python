def solution(s):
    # s의 길이가 1000 이하이므로 완전탐색을 사용할 수 있다
    # 같은 이유로 문자열 슬라이싱을 사용해도 시간 제한에 걸리지 않는다
    minimum = len(s)
    for i in range(1, len(s)+1):
    # 1부터 len(s)까지 문자열을 자를 단위를 설정한다
        result, word, count = '', s[:i], 1
        # 현재 문자열을 확인할 때, 반복 되었는지 확인하기 위해 이전 문자열이 필요하다
        # 때문에 word로 이전 문자열을 확인하고, count에 이전 문자열의 반복 횟수를 저장한다
        # 초기값은 슬라이싱을 한 번 수행한 상태로 설정
        # result에는 문자열을 계속 붙여 압축이 끝난 문자열을 만든다
        for j in range(i, len(s)+i, i):
        # j의 범위는 i부터 len(s)까지가 된다
        # i만큼의 증가치를 가지고 있는 것을 확인할 수 있는데, 
        # 끝 범위를 len(s)+i로 설정해야 len(s)까지 순회할 수 있다 (len(s)+i에 도달하는 순간 종료)
        # len(s)에서 슬라이싱이 필요한 이유는 후에 설명
            temp = s[j:j+i] # 문자열 슬라이싱
            if temp == word:
                count += 1 # 이전 문자열과 현재 문자열이 같다면 반복이므로 count를 증가
            else: # 문자열이 서로 다르다면 word를 result에 붙인다
                if count != 1:
                    result += str(count) # count가 1이 아니면 count도 붙여준다
                result += word # word를 result에 붙이고
                word = temp # 현재 문자열을 word에 저장해서 다음에 활용될 수 있도록 함
                count = 1 # count는 1로 초기화
            # 현재 문자열(temp)이 아닌, 이전 문자열(word)을 result에 추가하고 있기 때문에
            # len(s)-i까지만 시행된다면 이때의 문자열은 temp에 저장되나 result에 더해지지 않는 문제가 발생한다
            # 때문에 len(s)까지 시행할 필요가 있다
        if len(result) < minimum:
            minimum = len(result) # 최솟값 추적
    return minimum