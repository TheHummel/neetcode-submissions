class Solution {
public:
    int maxArea(vector<int>& heights) {
        vector<int>::iterator p1 = heights.begin();
        vector<int>::iterator p2 = heights.end() - 1;

        int max = 0;
        int curr;

        while(p1 < p2) {
            curr = (p2-p1) * std::min(*p1, *p2);
            std::cout << *p1 << " " << *p2 << " " << curr <<"\n";
            if(*p1<*p2) ++p1;
            else --p2;

            max = std::max(max, curr);
        } 

        return max;

    }
};
