class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        def get_index(left, prefix):
            right = len(products) - 1
            while left <= right:
                mid = left + (right - left) // 2

                x = False
                if len(products[mid]) <= len(prefix):
                    x = prefix <= products[mid]
                else:
                    x = prefix <= products[mid][:len(prefix)]
                
                if x:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left


        res = []
        left = 0
        for i in range(1, len(searchWord) + 1):
            curr = searchWord[:i]
            left = get_index(left, curr)

            temp = []
            for i in range(left, min(len(products), left + 3)):
                if products[i][:len(curr)] == curr:
                    temp.append(products[i])
                else:
                    break

            res.append(temp)
        
        return res