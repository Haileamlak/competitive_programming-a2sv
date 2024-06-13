# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {}
        names = {}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
    
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email in parent:
                curr_parent = find(first_email)
            else:
                curr_parent = first_email
                parent[first_email] = first_email
                names[curr_parent] = name
            
            for i in range(2, len(account)):
                email = account[i]
                if email in parent:
                    parent[find(email)] = curr_parent
                else:
                    parent[email] = curr_parent
        
        res = defaultdict(list)
        for email in parent:
            res[find(email)].append(email)

        answer = []
        for email, emails in res.items():
            answer.append([names[email]] + sorted(emails))
        
        return answer