a_list = []

# 5번의 입력 받음
for i in range(5):
    a = input().split()
    a_list.append(a)

result_list = []
#2중으로 들어간 리스트이기 때문에
#2중 for문으로 안에 값들 뽑아온다.
for i in a_list:
    result = 0                  # 한 리스트 돌때마다 초기화
    for j in i:
        result += int(j)        # 각 참가자 점수 더하기
    result_list.append(result)  # 참가자 점수 리스트로 추가
print(result_list.index(max(result_list)) + 1, max(result_list))