import heapq
def dijkstras(graph,source):
    distances={}
    for vertex in graph:
        distances[vertex]=float('inf')
    distances[source]=0
    
    heap=[]
    heapq.heappush(heap,(0,source))
    
    while len(heap)!=0:
        cur_wt,cur_ver=heapq.heappop(heap)
        if cur_wt > distances[cur_ver]:
            continue
        
        for edge in graph[cur_ver]:
            travel_weight,node=edge
            cost=cur_wt+travel_weight
            if cost < distances[node]:
                distances[node]=cost
                heapq.heappush(heap,(cost,node))
    print(distances)
graph={
    'A':[(2,'B'),(4,'D')],
    'B':[(7,'C'),(1,'D')],
    'C':[(16,'F')],
    'D':[(22,'E')],
    'E':[(2,'C'),(5,'F')],
    'F':[]
     }
ans=dijkstras(graph,'A')
print(ans)
