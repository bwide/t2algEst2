import sys

path = sys.argv[1]

def pprint(dict):
    for key in dict:
        print(key + ": " + str(dict[key]))

def read_nodes_dict(file):
    number_of_nodes = int( file.readline() )
    nodes = {}
    
    for i in range(0, number_of_nodes):
        line = file.readline().split(' ')
        node, cost = line
        nodes[node] = int( cost )

    return nodes

def read_graph_dict(file, nodes):
    number_of_arrows = int( file.readline() )
    graph = dict.fromkeys( nodes.keys(), [] )
    
    for i in range(0, number_of_arrows):
        line = file.readline().strip('\n').split(' ')

        node_in, node_out, count = line
        
        graph[node_in] = graph[node_in] + [(node_out, int(count))]
    return graph

def read_file(file):
    ans1 = read_nodes_dict(file)
    return ans1, read_graph_dict(file, ans1)

def find_leaf_nodes_in(graph):
    return [ node for node in graph if not graph[node] ]

def find_first_node_in(graph): # check if node is referenced in any <__> list
    for key in graph:
        ans = True
        for i in graph:
            nodes = [ x for x,y in graph[i] ]
            if key not in nodes: continue
            else: ans = False; break
        if ans: return key 
    return None

def calculate_cost(node):

    global calls
    calls += 1

    cost = costs[node]

    if node in totalCosts: return totalCosts[node]

    if not graph[node]:  #leaf
        totalCosts[node] = cost
        return cost

    for adjacent, repetitions in graph[node]:
        cost += repetitions * calculate_cost(adjacent)
    
    totalCosts[node] = cost
    return cost

sys.setrecursionlimit(28953)

with open(path) as file:
    costs, graph = read_file(file)
    
    first_node = find_first_node_in(graph)

    totalCosts = {}
    calls = 0

    ans = calculate_cost(first_node)

    print("total calls: " + str(calls))
    print("total cost: " + str(ans))

