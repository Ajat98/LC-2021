"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == '': return ""
        if len(strs) == 1: return strs[0]
        
        pref = strs[0]
        
        
        for w in strs:
            if len(pref) > len(w): #check if current word is smaller than prefix
                pref, w = w, pref  #If pref is longer than current word, switch values and make prefix the smaller word
                
            while len(pref) > 0:
                if w[:len(pref)] == pref: #Compare up to the length of the prefix by using smallest word, 
                                          #if they match we move to next word, else we decrease current prefix by 1 and compare again
                    break
                else:
                    pref = pref[:-1]
     
        return pref
        
        
       
        
    """
    Old Attempt
     
        longest = ''
        #Get the smallest word in an array
        smallest =   (min(strs, key=len))
        print(smallest)
        
        #Start with the smallest string, compare it to every string
        for i in range(len(smallest)):
            if strs[len(strs)-1][i] == smallest[i]:
                longest += strs[len(strs)-1][i] #Need to add first index of the compared word, not the smallest
            else:
                return longest
        
        return longest
                
            
            
            #print(strs[i])
        
    """
