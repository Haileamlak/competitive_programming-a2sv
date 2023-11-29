
string sortSentence(string s)
{
    stringstream ss {s};
    string temp = "",result="";
    vector<string> res(9);
    int c = 0;
    while (ss>>temp)
    {
        int index = temp.back() - '0';
        temp.pop_back();
        res[index - 1] = temp;
        c++;
    }
    for (size_t i = 0; i < c; i++)
    {
        result += res[i] + " ";
    }
    result.pop_back();
    return result;
}
