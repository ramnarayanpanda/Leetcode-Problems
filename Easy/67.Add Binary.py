# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        outPut = int(a, 2) + int(b, 2)
        return f"{outPut:b}"
    
    
 
# The hardway   
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        length = min(len(a), len(b))
        
        i, j = 0, 0
        lst = []
        a, b = a[::-1], b[::-1]
        carry = '0'
        
        while i<length and j<length:
            if a[i]=='1' and b[j]=='1':
                if carry=='0': 
                    lst.append('0')
                else: 
                    lst.append('1')
                carry = '1'
            
            elif (a[i]=='1' and b[j]=='0') or (a[i]=='0' and b[j]=='1'):
                if carry=='1':
                    lst.append('0')
                else:
                    lst.append('1')
                
            else:
                if carry=='1':
                    lst.append('1')
                    carry='0'
                else: 
                    lst.append('0')
                    
            i, j = i+1, j+1
                    
                    
                    
        while i<len(a):
            if a[i]=='1':
                if carry=='1':
                    lst.append('0')
                else:
                    lst.append('1')
                    
            elif a[i]=='0':
                if carry=='1':
                    lst.append('1')
                    carry='0'
                else:
                    lst.append('0')
            
            i+=1
            
            
                    
        while j<len(b):
            if b[j]=='1':
                if carry=='1':
                    lst.append('0')
                else:
                    lst.append('1')
                    
            elif b[j]=='0':
                if carry=='1':
                    lst.append('1')
                    carry='0'
                else:
                    lst.append('0')
                
            j+=1
            
        if carry=='1':
            lst.append('1')
            
        return ''.join(lst[::-1])
                
        