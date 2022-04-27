# Library for INT_MAX
import sys

class Graph():
	#constructor
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	#printing the created mst
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][parent[i]])

	#function for returning index of minimum adjacent weight
	def minKey(self, key, mstSet):
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	#creating mst 
	def primMST(self):
		key = [sys.maxsize] * self.V
		parent = [None] * self.V
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1

		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True

			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u

		self.printMST(parent)



n=1
ver = int(input("Insert total no. of vertices : "))
g = Graph(ver)
flag = 0


#menu driven code
while(n):
    print("\n-----MENU-----\n 1. Exit\n 2. Insert graph\n 3. Create MST\n")
    n=int(input("Choose the number : "))
    if(n==1):
        n=0
        print("Programme ended!")
        break
    elif(n==2):
        tempGraph = []
        flag=1
        for i in range(ver):
            arr = list(map(int, sys.stdin.readline().strip().split()))
            tempGraph.append(arr)
        g.graph=tempGraph
    elif(n==3):
        if(flag):
            g.primMST();
            print("MST Created")
        else:
            print("Please insert the graph!!!")
    else:
        print("Please select correct number")








'''
g.graph = [ [0, 2, 11, 1, 0, 0],
			[2, 0, 0, 9, 10, 0],
			[11, 0, 0, 0, 0, 20],
			[1, 9, 0, 0, 3, 1],
			[0, 10, 0, 3, 0, 0],
			[0, 0, 20, 1, 0, 0]]
			
Total vertices	= 6
		
input for Insert graph = 
			0 2 11 1 0 0
			2 0 0 9 10 0
			11 0 0 0 0 20
			1 9 0 0 3 1
			0 10 0 3 0 0
			0 0 20 1 0 0
			
Output = 
			Edge 	Weight
			0 - 1 	 2
			0 - 2 	 11
			0 - 3 	 1
			3 - 4 	 3
			3 - 5 	 1


'''