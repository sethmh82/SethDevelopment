N = 100000

# tree nodes connection 
edges = [[]for i in range(N)]

# stores the index of node in DFS 
mp = {}

# stores the index of node in 
# original node 
a = []

# Function to call DFS and count nodes 
# levels that subtree 
def dfs(levels, child, parent):
	# stores the DFS of tree 
	a.append(child) 
	# hieght of subtree 
	levels[child] = 1
	# iterate for children 
	for edge in edges[child]:
		# if not equal to parent 
		# so that it does not traverse back 
		if (it != parent):
			# call DFS for subtree 
			dfs(levels, edge, child) 
			# add the height 
			levels[child] += levels[edge] 
            
            
            
            
			
# Function to return the DFS of subtree of node 
def printDFSofSubtree(node, under):
	
	# index of node in the original DFS 
	ind = mp[node] 
	
	# height of subtree of node 
	height = under[node]
	
	print("The DFS of subtree", node, ":", end=" ")
     print("")
	
	# print the DFS of subtree 
	for i in range(ind,ind + under[node]):
		print(a[i], end=" ") 
	print()
	
# Function to add edges to a tree 
def addEdge(x, y):
	v[x].append(y) 
	v[y].append(x) 

# Marks the index of node in original DFS 
def markIndexDfs():
	
	size = len(a)
	
	# marks the index 
	for i in range(size):
		mp[a[i]] = i 
	
# Driver Code 

n = 7

# add edges of a tree 
addEdge(1, 2) 
addEdge(1, 3) 
addEdge(2, 4) 
addEdge(2, 5) 
addEdge(4, 6) 
addEdge(4, 7) 

# array to store the height of subtree 
# of every node in a tree 
under = [0]*(n + 1)

# Call the function DFS to generate the DFS 
dfs(under, 1, 0) 

# Function call to mark the index of node 
markIndexDfs() 

# Query 1 
printDFSofSubtree(2, under)

# Query 2 
printDFSofSubtree(4, under)

# This code is contributed by SHUBHAMSINGH10
