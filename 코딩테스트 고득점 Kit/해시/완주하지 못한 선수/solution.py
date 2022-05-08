def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for x in participant:
        hashDict[hash(x)] = x
        sumHash += hash(x)
        
    for y in completion:
        sumHash -= hash(y)
        print(hash(y))
        
    
    answer = hashDict[sumHash]
    return answer