class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size()-1;

        while(i<j) {
            char a = std::tolower(s[i]);
            char b = std::tolower(s[j]);
            if (!std::isalnum(a)) {
                i++;
                continue;
            }
            if (!std::isalnum(b)) {
                j--;
                continue;
            }
            if (a!=b) return false;
            i++;
            j--;
        }
        return true;
    }
};
