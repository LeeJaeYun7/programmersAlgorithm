
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
from collections import deque 


def equalStacks(h1, h2, h3):
    
    h1 = deque(h1) 
    h2 = deque(h2) 
    h3 = deque(h3) 
    
    answer = 0 
    height1 = sum(h1)
    height2 = sum(h2)
    height3 = sum(h3) 
    
    while True: 
        maxHeight = max(height1, height2, height3) 
        
        if maxHeight == height1 and maxHeight == height2 and maxHeight == height3:
            answer = maxHeight 
            break 
        
        if maxHeight == height1:
            num = h1[0]
            height1 -= num
            h1.popleft()
            continue   
            
        if maxHeight == height2: 
            num = h2[0]
            height2 -= num 
            h2.popleft()
            continue  
            
        if maxHeight == height3: 
            num = h3[0]
            height3 -= num
            h3.popleft() 
            continue 
        
    return answer 
    
    
