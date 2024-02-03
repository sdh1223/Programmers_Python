def minute(time):
    # 시간을 분 단위로 변환
    time = time.split(':')
    result = int(time[0]) * 60 + int(time[1])
    return result

def no_crosshatch(music):
    # 음악이 정해진 시간만큼 반복되어 계산되므로 이에 맞춰 길이를 늘려야 하는데
    # crosshatch(#)가 들어가 있는 경우 계산이 어려워진다
    # (C#의 경우 음 1개를 뜻하지만 길이는 2칸이 됨)
    # 때문에 소문자로 바꿔서 한 글자로 표현한다
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music

def play(time, music):
    # 음악을 정해진 시간만큼 반복
    # 음악을 충분한 길이로 늘린 후에 정해진 시간만큼 자른다
    # 다만 정해진 시간이 음악 길이보다 짧을 수도 있음에 주의
    if time >= len(music):
        n = time // len(music) + 1
        music = music * n
    return music[:time]

def solution(m, musicinfos):
    answer = []
    for index, info in enumerate(musicinfos):
        info = info.split(',')
        # info = [["12:00"],["12:14"],["HELLO"],["CDEFGAB"]]
        time = minute(info[1]) - minute(info[0])
        music = no_crosshatch(info[3])
        played = play(time, music)
        # 만든 함수 사용
        if no_crosshatch(m) in played:
            answer.append([time, index, info[2]])
            # 조건이 일치하는 음악이 여러 개일 경우
            # (1) 재생된 시간이 긴 것
            # (2) 먼저 입력된 것
            # 순으로 정렬해야 한다
            # 때문에 time, index를 음악 제목과 같이 추가
    if answer:
        answer.sort(key=lambda x: (-x[0], x[1]))
        # 기본적으로 작은 수부터 오게 정렬되므로
        # 재생된 시간이 '긴' 것부터 오도록 하려면 -x[0]로 작성해야 함
        return answer[0][2]
    else:
        return '(None)'