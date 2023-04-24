#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        new = []
        s_dic = {}

        for i in range(len(s)):
            new.append(s[i])
            if s[i+1] in new:
                return s_dic[new[1]]
        return -1

# @lc code=end

