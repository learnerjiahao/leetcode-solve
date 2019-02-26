class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        minest_ch, return_ch = "z", "z"
        flag = False
        for ch in letters:
            if ch > target and ch <= return_ch:
                flag = True
                return_ch = ch
            if ch < minest_ch:
                minest_ch = ch

        if not flag:
            return minest_ch
        else:
            return return_ch



if __name__ == "__main__":
    sol = Solution()
    sol.nextGreatestLetter(["c","f","j"], "a")

