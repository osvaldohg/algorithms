import sys
sys.setrecursionlimit(64000000)

#print "DFS"

explored={}
graph={}
fgraph={}
func={}
t=0
count=0
lista=[]

def dfs(graph,start):
    global func
    global t
    global count
    count+=1
    explored[start]=True
    
    if start in graph:
        for node in graph[start]:
            if not explored[node]:
                dfs(graph,node)
    
    t+=1
    func[start]=t

def dfs_loop(graph,size,counting):
    global explored
    global count

    for i in range (size,0,-1):
        if not explored[i]:
            count=0
            dfs(graph,i)
            if counting:
                #print "leader "+str(i)+" size "+str(count)
                if count not in lista:
                    lista.append(count)

def graph_reader(inFile,a,b,graph,size):
    global explored
    buffer=open(inFile,"r")
    
    for line in buffer:
        values=line.split()
        if int(values[a]) in graph:
            graph[int(values[a])].append(int(values[b]))
        else:
            graph[int(values[a])]=[int(values[b])]

    explored={k:False for k in range(0,size+1)}

def graph_reader_order(inFile,graph,size):
    global explored
    buffer=open(inFile,"r")

    for line in buffer:
        values=line.split()
        a=func[(int(values[0]))]
        b=func[(int(values[1]))]

        if a in graph:
            graph[a].append(b)
        else:
            graph[a]=[b]

    explored={k:False for k in range(1,size+1)}

#main
#exFILE="graph4.txt"
exFILE="scc1.txt"
gSIZE=875714
#gSIZE=8
graph_reader(exFILE,1,0,graph,gSIZE)
dfs_loop(graph,gSIZE,False)
graph_reader_order(exFILE,fgraph,gSIZE)
#print func
#print graph
dfs_loop(fgraph,gSIZE,True)
print sorted(lista,reverse=True)
