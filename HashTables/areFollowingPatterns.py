# HashTables
# codefights
# by Oz

def areFollowingPatterns(strings, patterns):
    result={}
    
    for i in range(len(strings)):
        if patterns[i] not in result :
            if strings[i] in result.values():
                return False
            result[patterns[i]]=strings[i]
        else:
            print strings[i],result[patterns[i]]
            if strings[i] != result[patterns[i]]:
                return False
            
            
    return True

        
