class Solution:

    def isSubsequenceForFollowUp(self, s: 'str', t: 'str') -> 'bool':
        # preprocess t
        idx = {}
        iidx = {}
        ids = []
        for i, ch in enumerate(t):
            if ch not in idx:
                idx[ch] = [i]
            else:
                idx[ch].append(i)
        
        prev = 0
        for ch in s:
            if ch not in idx: 
                return False
            # 在idx[ch]中找到第一个大于等于prev的id, 使用二叉搜索速度更快
            for tid in idx[ch]:
                if tid >= prev:
                    prev = tid + 1
                    break
            else:
                return False
        return True

    """
    Given a string s and a string t, check if s is subsequence of t.
    """
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        """
        two pointer greedy method
        """
        si, ti = 0, 0 

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        return si == len(s)