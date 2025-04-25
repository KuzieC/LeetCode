/*
 * @lc app=leetcode id=729 lang=cpp
 * @lcpr version=30200
 *
 * [729] My Calendar I
 *
 * https://leetcode.com/problems/my-calendar-i/description/
 *
 * algorithms
 * Medium (58.13%)
 * Likes:    4709
 * Dislikes: 129
 * Total Accepted:    421.8K
 * Total Submissions: 725.5K
 * Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
 *
 * You are implementing a program to use as your calendar. We can add a new
 * event if adding the event will not cause a double booking.
 * 
 * A double booking happens when two events have some non-empty intersection
 * (i.e., some moment is common to both events.).
 * 
 * The event can be represented as a pair of integers startTime and endTime
 * that represents a booking on the half-open interval [startTime, endTime),
 * the range of real numbers x such that startTime <= x < endTime.
 * 
 * Implement the MyCalendar class:
 * 
 * 
 * MyCalendar() Initializes the calendar object.
 * boolean book(int startTime, int endTime) Returns true if the event can be
 * added to the calendar successfully without causing a double booking.
 * Otherwise, return false and do not add the event to the calendar.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["MyCalendar", "book", "book", "book"]
 * [[], [10, 20], [15, 25], [20, 30]]
 * Output
 * [null, true, false, true]
 * 
 * Explanation
 * MyCalendar myCalendar = new MyCalendar();
 * myCalendar.book(10, 20); // return True
 * myCalendar.book(15, 25); // return False, It can not be booked because time
 * 15 is already booked by another event.
 * myCalendar.book(20, 30); // return True, The event can be booked, as the
 * first event takes every time less than 20, but not including 20.
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= start < end <= 10^9
 * At most 1000 calls will be made to book.
 * 
 * 
 */

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

using namespace std;

// @lc code=start
class MyCalendar {
public:
    map<int,int> mp;
    MyCalendar() {
        
    }
    
    bool book(int startTime, int endTime) {
        auto it = mp.lower_bound(startTime);
        if(it != mp.end() && it->first  < endTime) return false;

        it = mp.upper_bound(startTime);
        if(it != mp.begin() && (--it)->second > startTime) return false;
        mp[startTime] = endTime;
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}


