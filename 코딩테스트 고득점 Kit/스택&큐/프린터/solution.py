def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities) # 리스트에서 가장 큰 수를 구한다.(목표값)
        for i in range(len(priorities)): # 리스트를 처음부터 확인한다 
            if max_num == priorities[i]: # 만약 가장 큰 수와 리스트의 요소와 일치하면
                answer += 1 # 프린트한 것으로 간주하고 answer에 1 추가
                priorities[i] = 0 # 프린트한 요소는 0으로 표시 
                max_num = max(priorities) # 가장 큰 수를 다시 구한다.
                if i == location: # 만약 location과 i가 일치하면 answer을 반환한다. 
                    return answer