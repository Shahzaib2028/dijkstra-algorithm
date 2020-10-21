class Dij:
    def __init__(self,vertex):
        self.vertex = vertex
        self.array = [[0 for i in range(self.vertex)] for j in range(self.vertex)]

    def AddDirectedEdges(self, src, destination, cost):
        if src == destination:
            print("Same source and destination")
        else:
            self.array[src][destination] = cost

    def GetDirectedNeighbours(self, source):
        a = []
        for i in range(len(self.array[source])):
            if self.array[source][i] > 0:
                a.append(i)
        return a

    def Print(self):
        for i in self.array:
            for j in i:
                print(j,end=' ')
            print()

    def rasta(self,source):
        dict = {}
        for i in range(len(self.array)):
            temp = {}
            z = self.GetDirectedNeighbours(i)
            for j in z:
                temp[j]  = self.array[i][j]
            dict[i] = temp


        start = source
        goal = len(self.array) - 1
        shortest_path = {}
        predecessor ={}
        infinity = 999999
        path = []
        unseenNodes = dict

        for i in unseenNodes:
            shortest_path[i] = infinity
        shortest_path[start] = 0


        while unseenNodes:
            minNode = None
            for i in unseenNodes:
                if minNode == None:
                    minNode = i
                elif shortest_path[i] < shortest_path[minNode]:
                    minNode = i

            for child , weight in dict[minNode].items():
                if shortest_path[minNode] + weight < shortest_path[child]:
                    shortest_path[child] = shortest_path[minNode] + weight
                    predecessor[child] = minNode
            unseenNodes.pop(minNode)


        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except:
                print('path not found')
                break

        path.insert(0,start)
        if shortest_path[goal] != infinity:
            print('shortest distance is ' , str(shortest_path[goal]))
            print('path is ' , str(path))




g = Dij(6)
g.AddDirectedEdges(0, 3, 5)
g.AddDirectedEdges(0, 1, 9)
g.AddDirectedEdges(1, 2, 15)
g.AddDirectedEdges(1, 4, 7)
g.AddDirectedEdges(2, 3, 5)
g.AddDirectedEdges(2, 4, 2)
g.AddDirectedEdges(3, 4, 4)
g.AddDirectedEdges(3, 5, 6)
g.AddDirectedEdges(4, 5, 1)
g.AddDirectedEdges(4, 2, 9)
g.Print()
g.rasta(1)

