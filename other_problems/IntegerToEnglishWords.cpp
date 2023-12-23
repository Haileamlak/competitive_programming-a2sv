
class Solution
{
public:
    string numberToWords(int num)
    {
        if (num < 0 || num > pow(2, 31) - 1)
            exit(1);
        string res = "";
        string x = to_string(num);
        bool added = false;

        for (size_t i = 1, j = 1; i <= x.size(); i++)
        {
            if (j == 2 && !added  )
            {
                res = "Thousand " + res;
                added = true;
            }

            else if (j == 3 && added)
            {
                if (res.substr(0, 8) == "Thousand")
                    res = res.substr(9);
                res = "Million " + res;
                added = false;
            }
            else if (j == 4 && !added)
            {
                if (res.substr(0, 7) == "Million")
                    res = res.substr(8);
                res = "Billion " + res;
                added = true;
            }
            switch (i % 3)
            {
            case 1:
                if (x.size() != i && x[x.size() - i - 1] == '1')
                    ;
                else
                {
                    if (x.size() == 1 && x[x.size() - i] == '0')
                        return "Zero";
                    if (x[x.size() - i] == '1')
                        res = "One " + res;
                    else if (x[x.size() - i] == '2')
                        res = "Two " + res;
                    else if (x[x.size() - i] == '3')
                        res = "Three " + res;
                    else if (x[x.size() - i] == '4')
                        res = "Four " + res;
                    else if (x[x.size() - i] == '5')
                        res = "Five " + res;
                    else if (x[x.size() - i] == '6')
                        res = "Six " + res;
                    else if (x[x.size() - i] == '7')
                        res = "Seven " + res;
                    else if (x[x.size() - i] == '8')
                        res = "Eight " + res;
                    else if (x[x.size() - i] == '9')
                        res = "Nine " + res;
                }
                break;
            case 2:
                if (x[x.size() - i] == '1')
                {
                    if (x[x.size() - i + 1] == '0')
                        res = "Ten " + res;
                    else if (x[x.size() - i + 1] == '1')
                        res = "Eleven " + res;
                    else if (x[x.size() - i + 1] == '2')
                        res = "Twelve " + res;
                    else if (x[x.size() - i + 1] == '3')
                        res = "Thirteen " + res;
                    else if (x[x.size() - i + 1] == '4')
                        res = "Fourteen " + res;
                    else if (x[x.size() - i + 1] == '5')
                        res = "Fifteen " + res;
                    else if (x[x.size() - i + 1] == '6')
                        res = "Sixteen " + res;
                    else if (x[x.size() - i + 1] == '7')
                        res = "Seventeen " + res;
                    else if (x[x.size() - i + 1] == '8')
                        res = "Eighteen " + res;
                    else if (x[x.size() - i + 1] == '9')
                        res = "Nineteen " + res;
                }
                else if (x[x.size() - i] == '2')
                    res = "Twenty " + res;
                else if (x[x.size() - i] == '3')
                    res = "Thirty " + res;
                else if (x[x.size() - i] == '4')
                    res = "Forty " + res;
                else if (x[x.size() - i] == '5')
                    res = "Fifty " + res;
                else if (x[x.size() - i] == '6')
                    res = "Sixty " + res;
                else if (x[x.size() - i] == '7')
                    res = "Seventy " + res;
                else if (x[x.size() - i] == '8')
                    res = "Eighty " + res;
                else if (x[x.size() - i] == '9')
                    res = "Ninety " + res;
                break;
            case 0:
                if (x[x.size() - i] == '1')
                    res = "One Hundred " + res;
                else if (x[x.size() - i] == '2')
                    res = "Two Hundred " + res;
                else if (x[x.size() - i] == '3')
                    res = "Three Hundred " + res;
                else if (x[x.size() - i] == '4')
                    res = "Four Hundred " + res;
                else if (x[x.size() - i] == '5')
                    res = "Five Hundred " + res;
                else if (x[x.size() - i] == '6')
                    res = "Six Hundred " + res;
                else if (x[x.size() - i] == '7')
                    res = "Seven Hundred " + res;
                else if (x[x.size() - i] == '8')
                    res = "Eight Hundred " + res;
                else if (x[x.size() - i] == '9')
                    res = "Nine Hundred " + res;
                break;
            default:
                break;
            }
            if (i % 3 == 0)
            {
                j++;
            }
        }
        if (res.size() > 0 && res[res.size() - 1] == ' ')
            res = res.substr(0, res.size() - 1);
        return res;
    }
};
