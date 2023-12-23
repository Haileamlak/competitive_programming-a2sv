class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int32_t> token;
        int s = tokens.size();
        int32_t num1, num2;
        for (size_t i = 0; i < s; i++)
        {
            if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/")
            {
                num1 = token.top();
                token.pop();
                num2 = token.top();
                token.pop();
                if (tokens[i] == "+")
                    num2 += num1;
                else if (tokens[i] == "-")
                    num2 -= num1;
                else if (tokens[i] == "*")
                    num2 *= num1;
                else if (tokens[i] == "/")
                    num2 /= num1;
                token.push(num2);
            }
            else
                token.push(stoi(tokens[i]));
        }
        return token.top();
    }
};
