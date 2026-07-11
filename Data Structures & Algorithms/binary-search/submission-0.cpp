class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size();
        int mid, mid_val;

        int i = 0;

        while (l<r) {
            mid = l+(r-l) / 2;
            mid_val = nums[mid];
            if (mid_val==target) return mid;
            if (r-l == 1) return -1;
            if (target < mid_val) r = mid;
            else l = mid;
            i++;
            std::cout << "l: " << l << ", mid: "<<mid <<", r: "<<r<<"\n";
            if (i>10) break;
        }

        return -1;
    }
};
