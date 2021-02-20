class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 = [x for x in s if x.isdigit()]
        stack2 = [x for x in s if x.isalpha()]
        if len(stack1) < len(stack2): stack1, stack2 = stack2, stack1
        if abs(len(stack1) - len(stack2)) > 1:
            return ''
        else:
            stack2 += [''] # fill shorter array with ''
            return ''.join([x + y for x, y in zip(stack1, stack2)])
