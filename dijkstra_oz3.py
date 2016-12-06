print "dijkstra"
#graph={'a':{'b':7,'c':9,'f':14},'b':{'c':10,'d':15},'c':{'d':11}}
graph=dict()

def graph_reader(inFile,graph,size):
    global explored
    buffer=open(inFile,"r")
    
    for line in buffer:
        values=line.split()
        
        tmp={}
        for i in range (1,len(values)):
            w=values[i].split(",")
            tmp[int(w[0])]=int(w[1])
            
        graph[int(values[0])]=tmp
   
#node,weight
def dijsktra(graph,start):
    v=graph.keys()
    x=[]
    a={}
    
    x.append(start)
    a[start]=0
    
    while x!= v:
        min=[]
        for node in x:  #x=[a]
            lst=graph[node].keys()
            
            if len(lst)>0:
                #min[lst[0]]=graph[node][lst[0]]
                min.append(lst[0])
                min.append(graph[node][lst[0]])
            for edge in graph[node]:
                
                if (graph[node][edge]+ a[node]) < min[1]:
                    min[0]=edge
                    min[1]=graph[node][edge]+a[node]
        
        x.append(min[0])
        a[min[0]]=min[1]
        print x
                
                
    print a        
            
                
    
    
    
    #print a
    #ex=[7,37,59,82,99,115,133,165,188,197]
    #for e in ex:
    #    print a[e],
  

#graph_reader("dijkstraData.txt",graph,200)
graph_reader("test_data2.txt",graph,6)
#print graph[6]
#dijsktra(graph,1)
print graph.keys()



            
