class Solution {
public:
    vector<int> countBits(int n) {
        
        //
        vector<int> v(n+1);
        

        for (int i=0; i<=n; ++i) {
            int currentNumber = i;
            int ones = 0;
            while (currentNumber > 0){ 
                if(currentNumber % 2 == 0){
                    currentNumber /= 2;
                }else{
                    currentNumber = (currentNumber - 1) / 2;
                    ones++;
                }
            }
            v[i] = ones;
        }
                


         
        

        return v;
    }
};
