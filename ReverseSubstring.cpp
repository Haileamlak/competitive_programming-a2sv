
class Solution
{
public:
string reverseParentheses(string str)
{
    stack<int> st;
    int size = str.size();
    for (int i = 0; i < size; i++)
    {
        if (str[i] == '(')
        {
            st.push(i);
        }
        else if (str[i] == ')')
        {
            reverse(str.begin() + st.top() + 1,
                    str.begin() + i);
            st.pop();
        }
    }

    string res = "";
    for (int i = 0; i < size; i++)
    {
        if (str[i] != ')' && str[i] != '(')
            res += (str[i]);
    }
    return res;
}
};
