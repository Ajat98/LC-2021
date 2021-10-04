class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        
       #Need to use stack to keep track of what we are pushing
        stack = []
        #dict to keep track of closing brackets pairs
        d = {"]":"[", "}":"{", ")":"("}
        
        for c in s:
            if c in d.values(): #the opening brackets, if found append to stack
                stack.append(c)
            elif c in d.keys(): #Closing brackets, if found and stack is empty --> error, else if the opening bracket is not popped then out of sequence
                if stack == [] or d[c] != stack.pop(): #We should never find a closing bracket before we have already found it's opening bracket (d[c] != stack.pop)
                    return False
            else:
                return False
                
       #if stack empty then correct num of parentheses
        if stack == []:
            return True
        
        
            
        
