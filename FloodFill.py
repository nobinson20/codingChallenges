class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image

        sn = image[sr][sc]
        image[sr][sc] = newColor

        # 1) go up
        if sr > 0 and image[sr - 1][sc] == sn:
            # print ("go up from", sr, sc)
            Solution.floodFill(self, image, sr - 1, sc, newColor)

        # 2) go down
        if sr < len(image) - 1 and image[sr + 1][sc] == sn:
            # print ("go down from", sr, sc)
            Solution.floodFill(self, image, sr + 1, sc, newColor)

        # 3) go left
        if sc > 0 and image[sr][sc - 1] == sn:
            # print ("go left from", sr, sc)
            Solution.floodFill(self, image, sr, sc - 1, newColor)

        # 4) go right
        if sc < len(image[0]) - 1 and image[sr][sc + 1] == sn:
            # print ("go right from", sr, sc)
            Solution.floodFill(self, image, sr, sc + 1, newColor)

        return image





