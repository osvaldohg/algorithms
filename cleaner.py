import os
import shutil

print "cleanning"

excludelist=["exclude.txt","excludef1","excludef2"]

paths="C:\Users\ohuertag\Documents\oz_docs\python\git\\test1"

files=os.listdir(paths)

#print files
for file in files:
    if file not in excludelist:
        print "file to delete",file
        complete=os.path.join(paths,file)
        if os.path.isfile(complete):
            os.remove(complete)
        else:
            shutil.rmtree(complete)
        
        


