def intToRoman(num):
        
        sol = ""
        while(num):
            if(num >= 1000):
                num -= 1000
                sol += "M"
            elif(num >= 900):
                num -= 900
                sol += "CM"
            elif(num >= 500):
                num -= 500
                sol += "D"
            elif(num >= 400):
                num -= 400
                sol += "CD"
            elif(num >= 100):
                num -= 100
                sol += "C"
            elif(num >= 90):
                num -= 90
                sol += "XC"
            elif(num >= 50):
                num -= 50
                sol += "L"
            elif(num >= 40):
                num -= 40
                sol += "XL"
            elif(num >= 10):
                num -= 10
                sol += "X"
            elif(num >= 9):
                num -= 9
                sol += "IX"
            elif(num >= 5):
                num -= 5
                sol += "V"
            elif(num >= 4):
                num -= 4
                sol += "IV"
            elif(num >= 1):
                num -= 1
                sol += "I"
                
        return sol
