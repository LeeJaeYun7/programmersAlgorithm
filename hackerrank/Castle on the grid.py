#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque 

def minimumMoves(grid, startX, startY, goalX, goalY):
    
    q = deque() 
    q.append([startX, startY, 0])
    n = len(grid) 
    
    visited = [[False]*n for _ in range(n)]
    visited[startX][startY] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while q: 
        x, y, dist = q.popleft() 
    
        if x == goalX and y == goalY:
            return dist 
        
        for i in range(4):
            nx = x 
            ny = y 
            while True:
                nx += dx[i]
                ny += dy[i]
                
                if 0<=nx and nx<n and 0<=ny and ny<n and grid[nx][ny] == '.':
                    if not visited[nx][ny]:
                        visited[nx][ny] = True 
                        q.append([nx, ny, dist+1])         
                else:
                    break 
                                
    
  
