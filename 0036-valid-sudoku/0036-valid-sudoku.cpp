class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int bit = 1 << (board[r][c] - '1');   // digit 1-9 -> bit 0-8
                int b = (r / 3) * 3 + c / 3;          // which 3x3 box

                if ((rows[r] & bit) || (cols[c] & bit) || (boxes[b] & bit))
                    return false;                     // digit already seen

                rows[r]  |= bit;
                cols[c]  |= bit;
                boxes[b] |= bit;
            }
        }
        return true;
    }
};