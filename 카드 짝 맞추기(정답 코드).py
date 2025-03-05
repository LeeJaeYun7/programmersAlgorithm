from collections import deque

dx = [0, 0, -1, 1]  # 좌우이동
dy = [1, -1, 0, 0]  # 상하이동

# Ctrl 이동: 해당 방향으로 끝까지 이동
def ctrl_move(x, y, d, board):
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < 4 and 0 <= ny < 4):  # 범위 벗어나면 종료
            return x, y
        if board[nx][ny] != 0:  # 카드 발견하면 종료
            return nx, ny
        x, y = nx, ny  # 계속 이동

def bfs(board, start_x, start_y, target_x, target_y):
    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * 4 for _ in range(4)]
    visited[start_x][start_y] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == target_x and y == target_y:
            return cnt

        # 4방향 이동 (일반 이동)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

        # Ctrl + 이동
        for d in range(4):
            nx, ny = ctrl_move(x, y, d, board)
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

    return float('inf')  # 도달 불가능한 경우

def find_pairs(board):
    pairs = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                if board[i][j] in pairs:
                    pairs[board[i][j]].append((i, j))
                else:
                    pairs[board[i][j]] = [(i, j)]
    return pairs

def dfs(board, x, y, pairs, cnt):
    if not pairs:  # 모든 카드 제거 완료
        return cnt
    
    min_cost = float('inf')

    for num in list(pairs.keys()):
        (x1, y1), (x2, y2) = pairs[num]

        # 첫 번째 카드 방문 후 두 번째 카드 방문
        cost1 = bfs(board, x, y, x1, y1) + bfs(board, x1, y1, x2, y2) + 2
        board[x1][y1], board[x2][y2] = 0, 0
        min_cost = min(min_cost, dfs(board, x2, y2, {k: v for k, v in pairs.items() if k != num}, cnt + cost1))
        board[x1][y1], board[x2][y2] = num, num

        # 두 번째 카드 먼저 방문하는 경우도 고려
        cost2 = bfs(board, x, y, x2, y2) + bfs(board, x2, y2, x1, y1) + 2
        board[x1][y1], board[x2][y2] = 0, 0
        min_cost = min(min_cost, dfs(board, x1, y1, {k: v for k, v in pairs.items() if k != num}, cnt + cost2))
        board[x1][y1], board[x2][y2] = num, num

    return min_cost

def solution(board, r, c):
    pairs = find_pairs(board)
    return dfs(board, r, c, pairs, 0)
