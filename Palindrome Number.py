"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
#String Method
class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        s = a[::-1]

        if a == s:
            print("True")
        else:
            print("False")
 #note: string method may give you the answer but will not work in this case          
            
            
            

#Integer method
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False  
        div = 1
        while x >= 10 * div:  
            div *= 10
        while div > 1:  
            right = x % 10
            left = x // div  
            if left != right:
                return False
            x = (x % div) // 10  
            div //= 100  
        return True