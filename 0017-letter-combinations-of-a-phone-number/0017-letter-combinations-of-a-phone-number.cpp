class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> mp = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res;
        string cur;

        function<void(int)> dfs = [&](int i) {
            if (i == digits.size()) {
                res.push_back(cur);
                return;
            }
            for (char c : mp[digits[i] - '0']) {
                cur.push_back(c);   // choose
                dfs(i + 1);         // explore
                cur.pop_back();     // undo
            }
        };

        dfs(0);
        return res;
    }
};