import heapq

def prims(graph,start):
    parents={}
    weights={}
    queue=[]
    visited=set()
    for vertex in graph:
        weights[vertex]=9999999
    weights[start]=0
    heapq.heappush(queue,(0,start))
    while len(queue)!=0:
        cur_weight,cur_node=heapq.heappop(queue)
        if cur_node in visited:
            continue
        for weight,node in graph[cur_node]:
            if node not in visited and weight<weights[node]:
                weights[node]=weight
                parents[node]=cur_node
                heapq.heappush(queue,(weight,node))
            visited.add(cur_node)
    print("weights",weights)
    print("parents",parents)

graph={
    'A':[(10,'F'),(28,'B')],
    'B':[(14,'G'),(16,'C')],
    'C':[(16,'B'),(12,'D')],
    'D':[(18,'G'),(12,'C'),(22,'E')],
    'E':[(25,'F'),(24,'G'),(22,'D')],
    'F':[(10,'A'),(25,'E')],
    'G':[(14,'B'),(24,'E'),(18,'D')]
     }
mst=prims(graph,'A')
