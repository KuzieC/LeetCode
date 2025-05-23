#
# @lc app=leetcode id=127 lang=python3
# @lcpr version=20005
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (41.52%)
# Likes:    12506
# Dislikes: 1910
# Total Accepted:    1.3M
# Total Submissions: 3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
# 
# 
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
# 
# 
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
# 
# 
# Example 1:
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
# 
# 
# Example 2:
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        wordlis = set(wordList)
        def check(aa:str ,bb:str ):
            dif = sum(a != b for a,b in zip(aa,bb))
            return dif == 1
        q = []
        q.append(beginWord)
        vis = set()
        while len(q) > 0:
            res+=1
            for i in range(len(q)):
                curr = q.pop(0)
                if curr == endWord:
                    return res
                for j in range(len(curr)):
                    curr = list(curr)
                    ori = curr[j]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        curr[j] = c
                        if "".join(curr) in wordlis and "".join(curr) not in vis:
                            vis.add("".join(curr))
                            q.append("".join(curr))
                    curr[j] = ori
        return 0
                        
            
            
# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

