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
                // row = rows[i];
                auto col = cols[j];
                if (rows[i].find(num) != rows[i].end() or cols[j].find(num) != cols[j].end()) {
                    std::cout << "A;" << i << " " << j << "\n";
                    return false;
                }
                rows[i].insert(num);
                cols[j].insert(num);

                int square = (i / 3) * 3 + (j / 3);
                if (squares[square].find(num) != squares[square].end()) {
                    std::cout << "B;" << i << " " << j << "\n";
                return false;}

                squares[square].insert(num);

            }
        }
        std::cout << "TEST";
        for (int c:cols[3]) std::cout << c << "\n";

        return true;
    }
};
