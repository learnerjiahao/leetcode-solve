class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> bool:
        # method 1, backtracking
        s, m = divmod(sum(nums), k)
        if m != 0: return False
        nums.sort()
        if nums[-1] > s: return False

        def backtracking_method(groups):
            if not nums: return True
            now_num = nums.pop()
            for i, group in enumerate(groups):
                if group + now_num <= s:
                    groups[i] += now_num
                    if backtracking_method(groups): return True
                    groups[i] -= now_num
                # if group == 0: break

            nums.append(now_num)
            return False

        return backtracking_method([0] * k)

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4))