import sys
sys.setrecursionlimit(10**6)
answer = 1e9  
    
def solution(board, r, c):
    
    visited =[[False]*4 for _ in range(4)] 
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def allDone():
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    return False
        
        return True 
    
    def isInside(x, y):
        if 0<=x and x<4 and 0<=y and y<4:
            return True
        else:
            return False 
    
    def dfs(x, y, cnt):
        global answer 
        
        if answer < cnt:
            return 
        
        if allDone():
            answer = min(answer, cnt)
            return 
        
        if board[x][y] != 0:
            num = board[x][y]
            nx, ny = -1, -1 
            
            for i in range(4):
                for j in range(4):
                    if i != x and j!=y and board[i][j] == num:
                        nx = i
                        ny = j 
            if nx == -1 and ny == -1:
                board[x][y] = 0
                dfs(x, y, cnt+1)
                board[x][y] = num 
            else:
                if (x == nx and y != ny) or (x != nx and y == ny) and visited[nx][ny] == False:
                    board[x][y] = 0 
                    visited[nx][ny] = True 
                    dfs(nx, ny, cnt+2)
                    visited[nx][ny] = False 
                    board[x][y] = num
                elif (x!=nx and y!=ny) and visited[nx][ny] == False:
                    board[x][y] = 0 
                    visited[nx][ny] = True 
                    dfs(nx, ny, cnt+3)
                    visited[nx][ny] = False 
                    board[x][y] = num
            
        else:
            for i in range(4):
                for j in range(1, 4):
                    nx = x + j*dx[i]
                    ny = y + j*dy[i]
                    
                    if isInside(nx, ny) and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        dfs(nx, ny, cnt+1)
                        visited[nx][ny] = False 
        
    visited[r][c] = True 
    dfs(r, c, 0)
    
    
    
    
    
    return answer
