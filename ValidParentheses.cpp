
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> coll;
        char temp;
        int size = s.size();
        if (size % 2 != 0)
            return false;
        for (int i = 0; i < size; i++)
        {
            if (s[i] == '(')
                coll.push(')');
            else if (s[i] == '{')
                coll.push('}');
            else if (s[i] == '[')
                coll.push(']');
            else if (s[i] == ')' || s[i] == ']' || s[i] == '}')
            {
                if (!coll.empty())
                {
                    temp = coll.top();
                    coll.pop();
                }
                else
                    return false;
                if (s[i] != temp)
                    return false;
            }
        }
        if (coll.empty())
            return true;
        return false;
    }
};
