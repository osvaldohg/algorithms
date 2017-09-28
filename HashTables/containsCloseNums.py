# HashTables
# codefights
# by Oz

def containsCloseNums(nums, k):
    result={}
    
    for i in range(len(nums)):
        if nums[i] not in result:
            result[nums[i]]=[i]
        else:
            result[nums[i]].append(i)
            if len(result[nums[i]])>=2:
                if abs(result[nums[i]][0]-result[nums[i]][1])<=k:
                    return True
                else:
                    result[nums[i]].pop(0)
    #print result
    
    
    return False