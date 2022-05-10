def solution(progresses, speeds):
    answer = []
    time = 0 # 배포일
    count = 0 # 기능 수
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: # 첫번 째가 100이상이 될 때까지 time 증가
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count) # 마지막 기능 수

    return answer