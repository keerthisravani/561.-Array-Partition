def arrayPairSum(nums):
        l=sorted(nums)
        result=0
        for i in range(0,len(l),2):
            seq=l[i:i+2]
            result+=min(seq)
        return result
            
s=[1,6,7,3]
print(arrayPairSum(s))