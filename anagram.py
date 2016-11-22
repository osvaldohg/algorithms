print "decoding"

#poultry outwits ants
PHRASE="poultryoutwitsants"
#pastils turnout towy


#poultryoutwitsants
#ailnooprssttttuuwy

source_list=[]
source_dict={}
filter_words=[]


def load_dict_source(inputFile):
    source=open(inputFile,"r")
    for line in source:
        source_list.append(line.strip())
        
def fill_dict(word):
    dict={}
    for letter in word:
        if letter not in dict:
            dict[letter]=1
        else:
            dict[letter]=dict[letter]+1
    
    return dict
#main
load_dict_source("wordlist2.txt")
#print source_list
print len(source_list)
source_dict=fill_dict(PHRASE)
print source_dict.keys()

for word in source_list:
    tmpDict=fill_dict(word)
    for letter in tmpDict.keys():
        if letter in source_dict.keys():
            if tmpDict[letter]<=source_dict[letter]:
                filter_words.append(word)
        else:
            break
            
print len(filter_words)
#we are doing good enough

len_dict={}
for word in filter_words:
    if len(word) not in len_dict:
        len_dict[len(word)]=[word]
    else:
        len_dict[len(word)].append(word)
    
print len_dict.keys()








