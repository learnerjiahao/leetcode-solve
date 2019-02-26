class Solution:
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # first sort candidates from small to large
        candidates.sort()

        def helper(candidates, target):

            if len(candidates) <= 0:
                return []

            if target < candidates[0]:
                return []

            if target == candidates[0]:
                return [[candidates[0]]]

            ret1 = helper(candidates, target-candidates[0])
            ret2 = helper(candidates[1:], target-candidates[0])

            for ret in ret2:
                if ret in ret1:
                    ret1.remove(ret)

            ret3 = helper(candidates[1:], target)

            ret_list = ([([candidates[0]] + ret) for ret in ret1]) + \
                   [([candidates[0]] + ret) for ret in ret2] + \
                   ret3

            # print(candidates, target, ret_list)

            return ret_list

        return helper(candidates, target)


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_lists = []

        def backtrace(candidates, ret_list, remain):

            if remain == 0:
                ret_lists.append(ret_list)
                return
            if remain < 0:
                return

            for i, candidate in enumerate(candidates):
                now_len = len(ret_list)
                ret_list.append(candidate)
                backtrace(candidates[i:], ret_list, remain - candidate)
                ret_list = ret_list[:now_len]


        # first sort candidates from small to large
        candidates.sort()
        backtrace(candidates, [], target)
        return ret_lists





if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    # print(sol.combinationSum([2,3,5], 8))
    num1 = [1,2,3]
    num2 = [1,2,3]
    print(num1 == num2)

    # print([([3] + ])









