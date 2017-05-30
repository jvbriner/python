# class taken from http://alexhwoods.com/dijkstra/
import collections
import math
 
class Graph:
    ''' graph class inspired by https://gist.github.com/econchick/4666413
    '''
	
    def __init__(self):
        self.vertices = set()
 
        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}
 
    def add_vertex(self, value):
        self.vertices.add(value)
 
    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: 
            return  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance
 
    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string

def dijkstra(graph, start):
    # initializations
    S = set()
 
    # print("Dijkstra from start", start, flush=True)
    # print(graph, flush=True)
    # delta represents the length shortest distance paths from start -> v, for v in delta. 
    # We initialize it so that every vertex has a path of infinity (this line will break if you run python 2)
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)
 
    # then we set the path length of the start vertex to 0
    delta[start] = 0
 
    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(delta.keys()) - S), key=delta.get)
 
        # print('delta ', delta, flush=True)
        # print('previous ', previous, flush=True)
        # print('v ', v, flush=True)
        
        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v,neighbor]
 
            # is the new path from neighbor through 
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path
 
                # set the previous vertex of neighbor to v
                previous[neighbor] = v
        
        S.add(v)	
    return (delta, previous)
 
def shortest_path(graph, start, end):
    '''Uses dijkstra function in order to output the shortest path from start to end
    '''
    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path

def problem():
    G = Graph()
    [nNodes, nEdges] = list(map(int, input().split()))

    for i in range(1,nNodes+1):
        G.add_vertex(i)

    for i in range(nEdges):
        [u, v] = list(map(int, input().split()))
        G.add_edge(u, v, 6)
        G.add_edge(v, u, 6)

    startx = int(input())
    delta, previous = dijkstra(G, startx)
    # print(delta)
    distances=[]
    for i in range(1, nNodes+1):
        if i != startx:
            distances.append(delta[i] if not math.isinf(delta[i]) else -1)
    print(*distances)
    
numProblems = int(input())
for i in range(numProblems):
    problem()
