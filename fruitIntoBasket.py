# Typical but quintessential sliding window algo problem
# Commonly asked in Google OA

# Author: Byeongho Hwang

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        count = 0
        lp = 0
        basket = dict()
        
        for rp in range(len(fruits)):
            fruit_rp = fruits[rp]
            if fruit_rp not in basket:
                basket[fruit_rp] = 1
            else:
                basket[fruit_rp] += 1
            

            while len(basket) > 2:
                fruit_lp = fruits[lp]
                basket[fruit_lp] -= 1
                if basket[fruit_lp] == 0:
                    basket.pop(fruit_lp)
                lp += 1
                
            count = max(count, sum(basket.values()))
            
        return count
        
