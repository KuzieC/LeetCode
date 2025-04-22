/*
 * @lc app=leetcode id=875 lang=cpp
 * @lcpr version=30104
 *
 * [875] Koko Eating Bananas
 *
 * https://leetcode.com/problems/koko-eating-bananas/description/
 *
 * algorithms
 * Medium (48.93%)
 * Likes:    11875
 * Dislikes: 780
 * Total Accepted:    1M
 * Total Submissions: 2.1M
 * Testcase Example:  '[3,6,7,11]\n8'
 *
 * Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
 * piles[i] bananas. The guards have gone and will come back in h hours.
 * 
 * Koko can decide her bananas-per-hour eating speed of k. Each hour, she
 * chooses some pile of bananas and eats k bananas from that pile. If the pile
 * has less than k bananas, she eats all of them instead and will not eat any
 * more bananas during this hour.
 * 
 * Koko likes to eat slowly but still wants to finish eating all the bananas
 * before the guards return.
 * 
 * Return the minimum integer k such that she can eat all the bananas within h
 * hours.
 * 
 * 
 * Example 1:
 * 
 * Input: piles = [3,6,7,11], h = 8
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * Input: piles = [30,11,23,4,20], h = 5
 * Output: 30
 * 
 * 
 * Example 3:
 * 
 * Input: piles = [30,11,23,4,20], h = 6
 * Output: 23
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= piles.length <= 10^4
 * piles.length <= h <= 10^9
 * 1 <= piles[i] <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
public: 
    int time(vector<int> piles, int speed){
        int res = 0;
        for(size_t i = 0; i < piles.size(); i++){
            res += piles[i] / speed;
            if(piles[i] % speed > 0) res++;
        }   
        return res;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(),piles.end());
        while(left < right){
            int mid = left + (right-left)/2;
            int r = time(piles,mid);
            if(r > h){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        return right;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,6,7,11]\n8\n
// @lcpr case=end

// @lcpr case=start
// [30,11,23,4,20]\n5\n
// @lcpr case=end

// @lcpr case=start
// [30,11,23,4,20]\n6\n
// @lcpr case=end

 */

