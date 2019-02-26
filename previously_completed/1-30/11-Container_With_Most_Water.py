class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                now_contain = min(height[i], height[j]) * (j - 1)
                if now_contain > max_area:
                    max_area = now_contain

        return max_area
    
    def quick_sort(self, nums, low, high, indexs):
        if high <= low:
            return
        i, j = low, high
        pivot = nums[low]
        while i < j:
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
            indexs[j] = i + 1

            while i < j and nums[j] > pivot:
                j -= 1
            nums[i] = nums[j]
            indexs[i] = j + 1

        nums[i] = pivot
        indexs[i] = low + 1

        self.quick_sort(nums, low, i-1, indexs)
        self.quick_sort(nums, i+1, high, indexs)

    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # index = [x for x in range(1, len(height) + 1)]
        # self.quick_sort(height, 0, len(height) - 1, index)

        i, j = 0, len(height)-1
        maxarea = 0
        maxarea_i, maxarea_j = 0, 0
        while i < j:
            nowarea = (j-i) * min(height[i], height[j])
            if nowarea > maxarea:
                maxarea = nowarea
                maxarea_i = i
                maxarea_j = j
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1


        # max_area = 0
        # for i in range(0, len(height)):
        #     for j in range(i+1, len(height)):
        #         now_contain = min(height[i], height[j]) * (j - 1)
        #         if now_contain > max_area:
        #             max_area = now_contain
        #
        return maxarea,[maxarea_i,maxarea_j]


if __name__ == '__main__':
    soul = Solution()
    list = [1,34,5,4,31,2,12,1,21,1,2,12,1,21,3,4,5,5,4]
    # indexs = [x for x in range(1, len(list) + 1)]
    # soul.quick_sort(list, 0, len(list)-1, indexs)
    # print(list, indexs)
    print(soul.maxArea1(list))