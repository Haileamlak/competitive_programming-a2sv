class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        left = 0
        for i in range(1, len(searchWord) + 1):
            curr = searchWord[:i]
            left = bisect_left(products, curr, left)

            temp = []
            for i in range(left, min(len(products), left + 3)):
                if products[i][:len(curr)] == curr:
                    temp.append(products[i])
                else:
                    break

            res.append(temp)
        
        return res