class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();

        vector<unordered_set<char>> rows(n);
        vector<unordered_set<char>> cols(n);

        unordered_map<int, unordered_set<char>> squares;

        for (int i=0;i<n; ++i) {
            for (int j=0; j<n; ++j) {
                char num = board[i][j];
                if (num == '.') continue; 
                auto& row = rows[i];
                auto& col = cols[j];
                if (row.find(num) != row.end() || col.find(num) != col.end()) {
                    return false;
                }
                row.insert(num);
                col.insert(num);

                int square = (i / 3) * 3 + (j / 3);
                if (squares[square].find(num) != squares[square].end()) {
                return false;}

                squares[square].insert(num);

            }
        }

        return true;
    }
};
