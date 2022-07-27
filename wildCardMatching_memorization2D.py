'''
Time Complexity : O(mn)
Space Complexity : O(mn)
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : no
'''
class Solution:
    
    def memorization2D(self,string,pattern):
        
        # 1. initialize a boolean 2D memory
            # string is rows
            # pattern is cols
        rows = len(string)+1
        cols = len(pattern)+1
        
        # 2. fill-up the memory2D
        memory2D = [[False for col in range(0,cols)] for row in range(0,rows)]
        memory2D[0][0] = True
        
        # 2.1. fill up the 0th row
        for col in range(1,cols):
            if pattern[col-1] == '*':
                # value is 1 step back
                memory2D[0][col] = memory2D[0][col-1]
        
        # 2.2. fill up the entire memory2D
        for row in range(1,rows):
            for col in range(1,cols):
                
                # Case-1 char or ?
                if string[row-1] == pattern[col-1] or pattern[col-1] == '?':
                    # get value diagonally up
                    memory2D[row][col] = memory2D[row-1][col-1]
                    
                # Case-2 an * i.e. wildcard
                elif pattern[col-1] == '*':
                    # Case not choose --- 1 step back
                    notChoose = memory2D[row][col-1]
                    if notChoose == True:
                        memory2D[row][col] = notChoose
                        continue
                    
                    # Case choose --- 1 step above
                    choose = memory2D[row-1][col]
                    if choose == True:
                        memory2D[row][col] = choose
                        continue
        
        '''
        # print the memory2D
        print('Memory 2D is:')
        for row in range(0,rows):
            print(memory2D[row])
        print('\n')
        '''
        # return the result
        return memory2D[-1][-1]
    
    def isMatch(self, s: str, p: str) -> bool:
        return self.memorization2D(s,p)
        