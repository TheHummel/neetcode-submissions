class Solution {
public:
    uint32_t reverseBits(uint32_t n) {

        int reverseSum = 0;
        int counter = 31;
        while(counter >= 0){
           if(n % 2 == 0){ // even
                n /= 2;
                std::cout << "Even. " <<counter<<std::endl;
                

           }else{ // uneven
               n = (n - 1) / 2;
               reverseSum += std::pow(2,counter); 
               std::cout<< "Uneven: "<<counter<<std::endl;
               
           }
            counter--;

        }
        std::cout << "Final" << reverseSum << std::endl;
        return reverseSum;

    }
};
