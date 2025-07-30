#
# @lc app=leetcode id=729 lang=python3
# @lcpr version=30202
#
# [729] My Calendar I
#
# https://leetcode.com/problems/my-calendar-i/description/
#
# algorithms
# Medium (58.18%)
# Likes:    4748
# Dislikes: 131
# Total Accepted:    432.2K
# Total Submissions: 742.9K
# Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a double booking.
# 
# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).
# 
# The event can be represented as a pair of integers startTime and endTime that
# represents a booking on the half-open interval [startTime, endTime), the
# range of real numbers x such that startTime <= x < endTime.
# 
# Implement the MyCalendar class:
# 
# 
# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be
# added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.
# 
# 
# 
# Example 1:
# 
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
# 
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time
# 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the
# first event takes every time less than 20, but not including 20.
# 
# 
# Constraints:
# 
# 
# 0 <= start < end <= 10^9
# At most 1000 calls will be made to book.
# 
# 
#

# @lc code=start
from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.res = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.res) == 0:
            self.res.append((startTime,endTime))
            return True
        pos = bisect_left([x[0] for x in self.res],startTime)
        if pos == 0 and endTime <= self.res[0][0]:
            self.res.insert(pos,(startTime,endTime))
            return True
        elif pos == len(self.res) and startTime >= self.res[-1][1]:
            self.res.append((startTime,endTime))
            return True
        else:
            if 0 < pos < len(self.res) and self.res[pos][0] >= endTime and self.res[pos-1][1] <= startTime:
                self.res.insert(pos,(startTime,endTime))
                return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# @lc code=end



