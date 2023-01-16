N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]    # 1 ~ N+1번까지 리스트로 저장

result = []             # 결과값
num = 0                 # 인덱스 찾기

for i in range(N):      # N번동안 for문
    num += (K-1)        # K-1인 이유 : 인덱스 번호는 한칸씩 뒤에(?) 있어서
    if num >= len(lst): # 만약 인덱스 값이 lst 크기보다 크면
        num = num % len(lst)    # 인덱스 값을 lst 크기로 나머지를 구한다. # 나머지 값으로 다시 인덱스 번호 시작
                                
    result.append(str(lst.pop(num)))    #lst에서 인덱스 num자리 값을 빼고, result에 저장
print("<"+", ".join(result)+">")