import math
import os
import random
import re
import sys
import heapq 

def cookies(k, A):
    
    q = []
    answer = 0 
    possible = True 
    
    for num in A:
        heapq.heappush(q, num)
    
    while True:
        if q[0] >= k:
            break 
               
        if len(q) >= 2:
            num1 = heapq.heappop(q) 
            num2 = heapq.heappop(q) 
            
            newNum = num1+num2*2 
            heapq.heappush(q,newNum) 
            answer += 1        
        else:
            possible = False 
            break 
            
    if possible == False:
        return -1 
    
    return answer 
            
