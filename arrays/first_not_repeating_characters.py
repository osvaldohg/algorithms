# Arrays
# from codefights
# by oz

def firstNotRepeatingCharacter(s):
    queue=[]
    letters=[0 for x in range(27)]
    
    for letter in s:
        if letters[ord(letter)-97]==0:
            letters[ord(letter)-97]+=1
            queue.append(letter)
        else:
            if letter in queue:
                queue.remove(letter)

    if len(queue)==0:
        return "_"
    else:
        return queue[0]
    
        