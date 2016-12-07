print "dijkstra"
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
    n=0
    while len(x) <len(v):
        #[node,weight]
        min=[None,None]
        for node in x:  #x=[a]
            #print"looping on x",x
            for edge in graph[node]: #graph.keys()
                #print"looping on",node,graph[node]
                #print "this is edge",edge
                                
                if edge not in x:
                    if min[1]==None:
                        min[0]=edge
                        min[1]=a[node]+graph[node][edge]
                    
                    #print "checking edge",edge
                    #print graph[node][edge]+a[node], min[1]
                    if (graph[node][edge]+ a[node]) < min[1]:
                        min[0]=edge
                        min[1]=graph[node][edge]+a[node]
                        
        if min[0]!=None:
            x.append(min[0])
            a[min[0]]=min[1]
        min=[None,None]
        #print "x=",x
                  
    #a[] are the final distances from start       
    #print a
    #for the homework
    ex=[7,37,59,82,99,115,133,165,188,197]
    for e in ex:
        print a[e],
  

graph_reader("dijkstraData.txt",graph,200)
#graph_reader("test_data2.txt",graph,6)
#graph_reader("test_data.txt",graph,4)
dijsktra(graph,1)



            


            
