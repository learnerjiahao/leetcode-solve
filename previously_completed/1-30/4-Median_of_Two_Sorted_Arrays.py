class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        half_len = (m + n) // 2

        if n == 0:
            raise ValueError   # the size of bigger list should be larger than 0

        imin, imax = 0, m

        while imin <= imax:

            media = (imax - imin) // 2

            if media == 0:
                return

            if media < m and nums1[media] > nums2[half_len - (media + 1)]:
                imax = medi - 1
                medi = (imax - imin + 1) // 2

            if nums2[half_len - (media + 1) - 1] < nums1[media + 1]:
                imin = medi + 1
                medi = (imax - imin + 1) // 2



            # if max(mleft, nleft) <= min(mright, nright):
            #     if (m + n) % 2 != 0:
            #         return min(mright, nright)
            #     else:
            #         return (max(mleft, nleft) + min(mright, nright)) / 2


if __name__ == '__main__':
    soul = Solution()
    print(soul.findMedianSortedArrays1([1,3], [2]))