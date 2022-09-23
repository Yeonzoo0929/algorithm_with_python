#숫자 카드 게임
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

result = max(result, min_value)
# 8, 9번 라인을 result = max(result, min_value)로 작성 가능

print(result)