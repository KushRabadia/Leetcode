class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        ans = []
        
        for num in range(1, n+1):
            ans_string = ""
            
            if num % 3 == 0 and num % 5 == 0:
                ans_string += "FizzBuzz"
            elif num % 5 == 0:
                ans_string += "Buzz"
            elif num % 3 == 0:
                ans_string += "Fizz"
            else:
                ans_string += str(num)
                
            ans.append(ans_string)
        
        return ans
