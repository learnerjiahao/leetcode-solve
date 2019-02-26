class Solution:
    def append_str(self, list1, list2):
        res = []
        for i in len(list1):
            for j in len(list2):
                res.append(list1[i]+list2[j])
        return res
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        map_digit2letter = {}
        map_digit2letter[2] = ['a','b','c']
        map_digit2letter[3] = ['d','e','f']
        map_digit2letter[4] = ['g','h','i']
        map_digit2letter[5] = ['j','k','l']
        map_digit2letter[6] = ['m','n','o']
        map_digit2letter[7] = ['p','q','r','s']
        map_digit2letter[8] = ['t','u','v']
        map_digit2letter[9] = ['w','x','y','z']

        res = map_digit2letter[digits[0]]
        for i in range(1, len(digits)):
            res = self.append_str(res, map_digit2letter[digits[i]])

        return res
