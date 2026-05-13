from ast import List




def plusOne(digits: List[int]) -> List[int]:

        for i in reversed(range(len(digits))):
           if digits[i] == 9:
                digits[i] = 0
           else:
                digits[i] += 1
                break
        else:
            digits.insert(0,1)
                
        return digits
            

val = plusOne([9,9,9])
print(val)



val = plusOne([1,2,3])
print(val)
