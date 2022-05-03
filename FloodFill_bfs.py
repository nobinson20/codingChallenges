class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param new_color: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, new_color):
        # Write your code here
        max_row, max_col, original_color = len(image), len(image[0]), image[sr][sc]
        q = [(sr, sc)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(q) > 0:
            pixel = q.pop()
            # firstly check if the pixel in the range
            if 0 <= pixel[0] < max_row and 0 <= pixel[1] < max_col and \
                    image[pixel[0]][pixel[1]] == original_color and image[pixel[0]][pixel[1]] != new_color:
                image[pixel[0]][pixel[1]] = new_color
                neighbors = [(pixel[0]+direc[0], pixel[1]+direc[1]) for direc in directions]
                q.extend(neighbors)
        return image