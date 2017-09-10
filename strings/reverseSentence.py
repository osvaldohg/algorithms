# from codefights wizeline assessment
# by oz

def reverseSentence(sentence):
    words=sentence.strip().split()
    res=""
    
    for i in range(len(words)-1,-1,-1):
        res+=words[i]
        res+=" "
        
    return res.strip()
    