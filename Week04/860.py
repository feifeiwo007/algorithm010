class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_index=0
        ten_index=0
        for i in bills:
            if i==5 :
                five_index +=1
            elif i== 10 and five_index>0 :
                five_index -=1
                ten_index  +=1
            elif i==20 and five_index>0 and ten_index>0:
                five_index -=1
                ten_index -=1
            elif i==20 and five_index>=3 :
                five_index -=3
            else:
                return False
        
        return True