class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()) return "";
        vector<int> sizes;
        string encoding = "";

        for (const string& s:strs) {
            sizes.push_back(s.size());
        }

        for (int size:sizes) {
            encoding += to_string(size) + ';';
        }

        encoding += '#';

        for (const string& s:strs) {
            encoding += s;
        }

        return encoding;
    }

    vector<string> decode(string s) {
        if(s.empty()) return {};
        
        vector<int> sizes;
        vector<string> decodings;

        int i = 0;
        string curr;
        while (s.at(i) != '#') {
            curr = "";
            while(s[i]!=';') {
                curr += s[i];
                ++i;
            }
            sizes.push_back(stoi(curr));

            ++i;
        }
        ++i;

        for (int size:sizes) {
            decodings.push_back(s.substr(i, size));
            i += size;
        }
        
        return decodings;
    }
};
