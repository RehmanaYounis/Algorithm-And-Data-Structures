class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set <int> hashSet;
        for (int n :nums){
            if (hashSet.count(n)>0){
                return true;
            }
            hashSet.insert(n);
        }
        return false;
    }
};