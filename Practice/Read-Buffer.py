# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:34:06 2021

@author: SethHarden
"""

import sys
class Solution(object):
    

    
    fp = 0
    
    def read(buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buffRead = buf[0:n]
        print("buffer: ", buf[0:n])
        fp = buf[n:n*2]
        print("buffer is now at:", fp)
        
        return saveBuff(fp, buf[0:n])
    
    def saveBuff(fp, reader):
        arr = []
        
        
        
    buf = "sethharden"
    n = 4
    read(buf,n)
    read(buf,n)
    read(buf,n)
    read(buf,n)