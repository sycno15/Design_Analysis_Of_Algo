#taking 2 demo graphs:
graph1 = [
          [0,1,1,0,1,1],
          [1,0,1,0,0,0],
          [1,1,0,1,0,0],
          [0,0,1,0,1,0],
          [1,0,0,1,0,1],
          [1,0,0,0,1,0]
          ]
graph2 = [
          [0,1,1,1,1],
          [1,0,1,1,1],
          [1,1,0,1,1],
          [1,1,1,0,1],
          [1,1,1,1,0]
         ]
#to check if following node could be colored

def checkNext(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i]==1 and color[i]==c:
            return False
    return True

def graph_coloring_recur(graph, m, color, v):
    
    # If all vertices are assigned a color, return True
    if v == len(graph):
        return True

    # Try assigning all colors (1 to m)
    for c in range(1,m+1):
        if checkNext(v, graph, color, c):
            color[v] = c
            if graph_coloring_recur(graph, m, color, v + 1):
                return True
            # Backtrack
            color[v] = 0
    return False


def graph_coloring(graph, m):
    color = [0] * len(graph)

    if not graph_coloring_recur(graph, m, color, 0):
        print("No solution exists with", m, "colors.")
        return False

    print("Color assigned to each vertex:")
    for v in range(len(graph)):
        print(f"Vertex {v + 1} ---> Color {color[v]}")
    return True

#assuming the minimum colors requred are 3
min=3
print("For Graph 1:")
graph_coloring(graph1,min)
print("For Graph 2:")
graph_coloring(graph2,min)