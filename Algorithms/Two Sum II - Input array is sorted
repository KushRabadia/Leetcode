class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index,value in enumerate(numbers):
            remain = target - value
            if remain in nums_dict:
                return [nums_dict[remain]+1,index+1]
            nums_dict[value] = index
         
        return []
