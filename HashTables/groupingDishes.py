# HashTables
# codefights
# by Oz

def groupingDishes(dishes):
    group={}
    
    for i in range(len(dishes)):
        for j in range(1,len(dishes[i])):
            val=dishes[i][0]
            key=dishes[i][j]
            if key in group:
                group[key].append(val)
            else:
                group[key]=[val]

    res=[]
    i=0
    for key in group.keys():
        if len(group[key])>1:
            res.append([key])
            s=sorted(group[key])
            for val in s:
                res[i].append(val)
                
            i+=1
                
    return sorted(res)