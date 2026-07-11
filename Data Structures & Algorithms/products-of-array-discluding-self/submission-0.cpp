class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zero_idx = -1;
        int n = nums.size();

        vector<int> res(n);

        int total = 1;
        for (int i=0;i<n;++i) {
            int num = nums[i];
            if (num==0) {
                if (zero_idx >= 0) return res;
                zero_idx = i;
            } else {
                total *= num;
            }
        }
        if (zero_idx >= 0) {
            res[zero_idx] = total;
            return res;
        }

        for (int i=0;i<n;++i) {
            res[i] = total / nums[i];
        }

        return res;
    }
};
