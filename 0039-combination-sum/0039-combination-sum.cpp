class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, target, 0, cur, res);
        return res;
    }

private:
    void backtrack(vector<int>& c, int remain, int start,
                   vector<int>& cur, vector<vector<int>>& res) {
        if (remain == 0) {
            res.push_back(cur);
            return;
        }
        for (int i = start; i < c.size(); i++) {
            if (c[i] > remain) break;      // sorted, so the rest are too big
            cur.push_back(c[i]);
            backtrack(c, remain - c[i], i, cur, res);  // i, not i+1: reuse allowed
            cur.pop_back();                // undo the choice
        }
    }
};