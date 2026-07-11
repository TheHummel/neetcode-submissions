class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;

        for (const auto& token:tokens) {
            if(token=="+" || token=="-" || token=="*" || token=="/") {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                if (token=="+") stack.push_back(a+b);
                if (token=="-") stack.push_back(a-b);
                if (token=="*") stack.push_back(a*b);
                if (token=="/") stack.push_back(a/b);
            } else {
                stack.push_back(std::stoi(token));
            }
        }

        return stack.back();
    }
};
