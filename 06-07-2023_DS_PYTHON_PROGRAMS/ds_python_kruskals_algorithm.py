def kruskals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight,dest=edge
            edge_list.append((weight,source,dest))
    edge_list.sort()
    print("edges",edge_list)

    
    parents={}
    for vertex in graph:
        parents[vertex]=vertex
    mst=[]
    
    def find_parent(vertex):
        if parents[vertex]!=vertex:
            parents[vertex]=find_parent(parents[vertex])            
        return parents[vertex]
    
    for edge in edge_list:
        weight,source,dest=edge
        if find_parent(source)!=find_parent(dest):
            mst.append(edge)
            parents[find_parent(source)]=find_parent(dest)
    print("parents",parents)
    print("minimum spanning tree",mst)
    return mst
    
graph={
    'A':[(10,'F'),(28,'B')],
    'B':[(14,'G'),(16,'C')],
    'C':[(16,'B'),(12,'D')],
    'D':[(18,'G'),(12,'C'),(22,'E')],
    'E':[(25,'F'),(24,'G'),(22,'D')],
    'F':[(10,'A'),(25,'E')],
    'G':[(14,'B'),(24,'E'),(18,'D')]
     }
mst=kruskals(graph)