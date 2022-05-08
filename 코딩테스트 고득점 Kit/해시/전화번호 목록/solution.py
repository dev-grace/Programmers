def solution(phone_book):
    hash_map = {}
    answer = True
    
    # 모든 전화번호 HashMap에 넣기
    for x in phone_book:
        hash_map[hash(x)] = 0 # value는 작게 -> 공간복잡도 개선

    # 접두어가 hash map에 존재하는지 확인
    for phone_number in phone_book:
        for i in range(len(phone_number)):
            if hash(phone_number[:i]) in hash_map:
                answer = False

    
    return answer