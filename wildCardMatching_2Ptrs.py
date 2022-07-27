'''
Time Complexity : O(n) averagely 
Space Complexity : O(n)
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : no
'''
class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        '''Two ptrs approach'''
        
        # ptr to string
        sp = 0
        sStar = -1
        
        # ptr to pattern
        pp = 0
        pStar = -1
        
        
        while sp != len(s):
            
            # Case-1 match of char
            if pp < len(p) and (p[pp] == s[sp] or p[pp] == '?'):
                sp += 1
                pp += 1
                
            # Case-2 Wildcard
            elif pp < len(p) and p[pp] == '*':
                sStar = sp
                pStar = pp
                pp += 1
            
            # Case-3 No wildcard, exit
            elif pStar == -1:
                return False
            
            # Case-4 Check if we have a wildcard
            else:
                pp = pStar + 1
                sp = sStar + 1
                sStar = sp
        '''done with while loop'''
        
        while pp < len(p):
            # chk if we have remaining wild card
            if p[pp] == '*':
                pp += 1
            else:
                return False
        
        return True