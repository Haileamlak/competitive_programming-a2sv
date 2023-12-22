class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            left = 0
            right = n - 1
            while left <= right:
                image[i][left], image[i][right] = 1 - image[i][right], 1 - image[i][left]
                
                left += 1
                right -= 1

        return image