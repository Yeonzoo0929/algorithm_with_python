#큰 수의 법칙
#주어진 수를 M번 더하여 가장 큰 수를 만들되, 특정 인덱스의 숫자는 연속해서 K번을 초과해 나올 수 없다. 배열의 크기 = N
n, m, k = map(int, input().split()) 
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

