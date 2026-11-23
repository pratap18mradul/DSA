class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();

        // 1. Find the pivot: rightmost i where nums[i] < nums[i+1]
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;

        // 2. If a pivot exists, swap it with the rightmost element larger than it
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) j--;
            swap(nums[i], nums[j]);
        }

        // 3. Reverse the suffix after the pivot (whole array if no pivot)
        reverse(nums.begin() + i + 1, nums.end());
    }
};