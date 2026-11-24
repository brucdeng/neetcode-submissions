class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0, 10:0, 20:0}
        for bill in bills:
            amt = bill -5
            dic[bill] +=1
            while amt > 0:
                if dic[20] >0 and amt >= 20:
                    amt -=20
                    dic[20] -=1
                elif dic[10] >0 and amt >=10:
                    amt -=10
                    dic[10]-=1
                elif dic[5] > 0 and amt >= 5:
                    amt -=5 
                    dic[5]-=1
                else:
                    return False
        return True