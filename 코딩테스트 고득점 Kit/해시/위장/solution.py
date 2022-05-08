def solution(clothes):
    answer = 1
    hash_map = {}
    
    # 1. 옷을 종류별로 구분하기
    for clothe, type in clothes:
        # get 메소드는 Key에 해당하는 Value가 있으면 가져오고,
        # 아닐 경우 0을 Default로 지정하여 사용하겠다는 의미의 함수
        hash_map[type] = hash_map.get(type, 0) + 1
        

    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기 
    for type in hash_map:
        # 모든 옷 종류에 대해서 안 입는 경우가 있기 때문에 + 1 곱하기
        answer *= (hash_map[type] + 1)
        
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1