class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_map = {};

        for (int i=0;i<nums.size(); ++i) {
            nums_map[nums[i]] = i;
        }

        for (int i=0;i<nums.size(); ++i) {
            int pot = target - nums[i];
            if (nums_map.find(pot) != nums_map.end() && nums_map[pot]!=i) {
                return vector<int>{min(nums_map[pot], i), max(nums_map[pot], i)};
            }
        }


    }
};
