import math
from heapq import heappush, heappop

'''
    connected node
    1-2
    2-3
    2-5
    2-4
    3-4
    3-6
    5-6
    it will be store in pair g
    
    1 and 6 are exit node
'''
g1 = [0,1,1,2,3]
g2 = [3,2,3,4,4]


INF = math.inf
final_path = []

def cost_cal(cost_1, cost_2):
    return (cost_1 + cost_2) / 2


def calc_path(par, tar):
    path = []
    while par[tar] != -1:
        path.append(tar)
        tar = par[tar]

    path.append(tar)
    return path


def path(arr, source_node):
    global final_path
    source_node = int(source_node)
    print(arr)

    rows, cols = (7, 7)
    par = []
    cost = []  ##path ka cost
    roads = []  ##adjec matrix
    for i in range(rows):
        col = []
        road = []
        for j in range(cols):
            if i == j:
                col.append(0)
            else:
                col.append(INF)
            road.append(0)
        roads.append(road)
        cost.append(col)

    for x in range(len(g1)):
        t_cost = cost_cal(arr[g1[x]], arr[g2[x]])
        cost[g1[x]][g2[x]] = t_cost
        cost[g2[x]][g1[x]] = t_cost
        roads[g1[x]][g2[x]] = 1
        roads[g2[x]][g2[x]] = 1

    cost_to_reach = []
    for x in range(7):
        cost_to_reach.append(INF)
        par.append(-1)
    cost_to_reach[source_node] = 0

    ##priority queue (pair)##first { element cost of reach that node , node}

    h = []
    for x in range(7):
        if x:
            print(x)
            heappush(h, (cost_to_reach[x], x))
            print((cost_to_reach[x], x))

    cnt = 0
    while len(h):
        node_cost, node = heappop(h)
        print(node_cost, node, cnt+1)

        for neighbour in range(7):
            if neighbour and roads[node][neighbour]:
                if cost_to_reach[neighbour] > cost_to_reach[node] + cost[node][neighbour]:
                    cost_to_reach[neighbour] = cost_to_reach[node] + cost[node][neighbour]
                    par[neighbour] = node

        cnt += 1

    if cost_to_reach[1] > cost_to_reach[6]:
        final_path = calc_path(par, 6)
    else:
        final_path = calc_path(par, 1)

    final_path.reverse()
    return final_path