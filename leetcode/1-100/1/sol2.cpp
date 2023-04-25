class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> m;
        
        for(int i=0;i<nums.size();i++){
            int search = target - nums[i]; // search
            
            unordered_map<int, int>::iterator x = m.find(search);
            
            if(x != m.end()){
                // element found
                return vector<int> {i, m[search]};
            }
            m[nums[i]] = i; 
        }
        
        
        return vector<int> {0,0};
    }
};
