class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        // All digits were 9 (e.g. [9,9,9] -> [1,0,0,0])
        digits.insert(digits.begin(), 1);
        return digits;
    }
};