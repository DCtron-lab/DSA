class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        ans = ""
        d = ["Trillion", "Billion", "Million", "Thousand", ""]
        
        x = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety", 100:"Hundred", 0:""} 
        
        while num > 0:
            newans = ""
            newnum = num%1000
            num = num//1000
            units = newnum%10
            newnum //=10
            tens = newnum%10
            newnum //=10
            Hundreds = newnum
            if Hundreds != 0:
                newans = x[Hundreds]+ " Hundred"
            if tens == 1:                
                newans+=" "+ x[10+units]
            else:
                newans += " "+x[10*tens]+ " "+x[units]
            
            if newans.strip()=="":
                d.pop()
                continue
            ans = newans +" " + d.pop() + " " + ans
        return " ".join([x for x in ans.split(" ")if x != ""])