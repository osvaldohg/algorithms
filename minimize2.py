data=[]

fhandler=open("jobs.txt","r")

for line in fhandler:
    val=line.strip().split()
    diff=float(val[0])/int(val[1])
    row=[]
    row.append(int(val[0]))
    row.append(int(val[1]))
    two=[]
    two.append(diff)
    two.append(row)
    data.append(two)
    
ndata=sorted(data, reverse=True)

l=0
total=0

for i in ndata:
    total+= i[1][0]*(l+i[1][1])
    l+=i[1][1]
    
print total

#2 67311454237

    
    
    
