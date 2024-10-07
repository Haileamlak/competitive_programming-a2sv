# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cp_domains: List[str]) -> List[str]:
        domain_visit = {}
        for cp_domain in cp_domains:
            cp, domain = cp_domain.split(" ")
            
            for i in range(len(domain) - 1, -1, -1):
                if domain[i] == '.':
                    domain_visit[domain[i + 1:]] = domain_visit.get(domain[i + 1:], 0) + int(cp)
            
            # for the whole domain
            domain_visit[domain] = domain_visit.get(domain, 0) + int(cp)
        
        result = []
        for domain, cp in domain_visit.items():
            result.append(str(cp) + " " + domain)
        
        return result