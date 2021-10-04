m, n = map(int, input().split())

lst = [input() for _ in range(n)]
cnt = 0

for i in range(n):
# - 를 세는 for문. 따라서 전체 for문은 세로 크기만큼 동작
    j = 0
    while j < m:
        # m-2 일 때 경우와 m-1일 때의 경우를 나누기 
        if j < m-1:
            if lst[i][j] == '|':
            # - 타일을 세는 것이므로 | 타일일 경우 다음 타일로
                j += 1
            else: 
            # - 가 시작되면 cnt + 1
                cnt += 1
                while j < m and lst[i][j] == '-':
                    j += 1
        elif j == m-1:
            # 마지막일때 세는 방법을 다르게 
            


for j in range(m):
# | 를 세는 for문. 따라서 전체 for문은 가로 크기만큼 동작
    i =0
    while i < n:
        if lst[i][j] == '-':
            i += 1
        else:
            cnt += 1
            while i < n and lst[i][j] == '|':
                i += 1

print(cnt)

