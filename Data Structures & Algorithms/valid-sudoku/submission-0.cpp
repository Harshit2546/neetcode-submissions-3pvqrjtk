class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Use 2D arrays to track seen digits: [index][digit]
        // Example: usedRows[2][5] means digit '5' was seen in row 2
        bool usedRows[9][9] = {false};
        bool usedCols[9][9] = {false};
        bool usedBoxes[9][9] = {false};

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int num = board[r][c] - '1'; // Convert '1'-'9' to index 0-8
                
                // Calculate box index: 0 to 8
                // This formula maps (row, col) to one of the nine 3x3 squares
                int boxIdx = (r / 3) * 3 + (c / 3);

                // Check if we've seen this digit in the current row, column, or box
                if (usedRows[r][num] || usedCols[c][num] || usedBoxes[boxIdx][num]) {
                    return false;
                }

                // Mark the digit as seen
                usedRows[r][num] = true;
                usedCols[c][num] = true;
                usedBoxes[boxIdx][num] = true;
            }
        }

        return true;
    }
};
