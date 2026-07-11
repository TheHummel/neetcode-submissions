class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int k = s1.length();
        int m = s2.length();
        if (k>m) return false;

        vector<int> target(26);
        vector<int> curr(26);

        for (int i=0; i<k; ++i) {
            target[s1.at(i)-'a']++;
            curr[s2.at(i)-'a']++;
        }

        if (target == curr) return true;

        int idxR, idxL;
        for (int j=k; j<m; ++j) {
            idxR = s2.at(j)-'a';
            idxL = s2.at(j-k)-'a';

            curr[idxR]++;

            curr[idxL]--;

            if (target == curr) return true;
        }

        return false;

        /*unordered_map<char, int> curr = {};
        unordered_map<char, int> target = {};


        int needed = 0;
        for (char c:s1) {
            if (target.find(c) == target.end()) {
                target.insert({c, 1});
                ++needed;
            } else {
                target[c] = target[c] + 1;
            }
        }

        int curr_needed = needed;

        int l = -1;
        char l_char;

        int i = 0;

        for (char c:s2) {
            if (target.find(c) != target.end()) {
                if (l == -1) {
                    l = i;
                }
                if (curr.find(c) == curr.end()) {
                    curr.insert({c, 1});
                } else {
                    if (curr[c] == target[c]) {
                        // move l to right
                        while (curr[c] == target[c]) {
                            l_char = s2.at(l);
                            if (curr[l_char] == target[l_char]) ++curr_needed;
                            curr[l_char] = curr[l_char] - 1;
                            ++l;
                        }
                    }
                    curr[c] = curr[c] + 1;
                }
                if (curr[c] == target[c]) {
                    --curr_needed;
                    
                }
                if (curr_needed <= 0) return true;
            } else {
                curr = {};
                curr_needed = needed;
                l = -1;
            }

            ++i;
        }

        return false;*/
    }
};
