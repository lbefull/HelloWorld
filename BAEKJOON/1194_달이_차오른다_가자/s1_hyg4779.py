from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            graph[i][j] = "."
            q.append((i, j, 0))
            break

while q:
    r, c, key = q.popleft()
    for d in direct:
        nr, nc = r + d[0], c + d[1]
        nkey = key
        # 범위 안 이면서 벽도 아니고 동일한 키를 가지고 그곳에 방문한 적이 없어야 한다.
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != "#" and visited[nr][nc][key] == 0:
            # 문인 경우
            # 열쇠가 없으면 continue
            # & 연산으로 1 혹은 0이 나오게 된다.
            if graph[nr][nc].isupper():
                if not (key & 1 << (ord(graph[nr][nc]) - ord("A"))):
                    continue
            # 열쇠인 경우
            # or 연산을 통해 key를 교체
            # a키만 가지고 c키를 먹는다면
            # 1 -> 101이 된다.
            elif graph[nr][nc].islower():
                nkey |= 1 << ord(graph[nr][nc]) - ord("a")
            elif graph[nr][nc] == "1":
                print(visited[r][c][key] + 1)
                exit()
            q.append((nr, nc, nkey))
            visited[nr][nc][nkey] = visited[r][c][key] + 1
print(-1)