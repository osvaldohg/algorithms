print "DFS"

explored={}
graph={}

def dfs(graph,start):
    print "Visiting ",start
    explored[start]=True
    for node in graph[start]:
        if not explored[node]:
            dfs(graph,node)


def graph_reader(inFile):
    global graph
    global explored
    buffer=open(inFile,"r")
    
    for line in buffer:
        values=line.split()
        #print values[1],values[0]
        if int(values[0]) in graph:
            graph[int(values[0])].append(int(values[1]))
        else:
            graph[int(values[0])]=[int(values[1])]

    #print graph
    explored={k:False for k in graph.keys()}

#main
graph_reader("test_graph.txt")
#print explored
print graph
dfs(graph,1)
