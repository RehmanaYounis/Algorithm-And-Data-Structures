class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int l = 0;
        int maxP=0;
        int curP=0;
        
        for( int r=1;r<prices.size();r++ )
        {
            
            curP= prices[r]-prices[l];
            maxP=max(curP, maxP);
            if (prices[l]>prices[r])
            {
                l=r;
            }
            
        }
        
        return maxP;
        
    }
};