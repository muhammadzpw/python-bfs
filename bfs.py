from pprint import pprint
import sys
from collections import deque

class Adjacent:
	def __init__(self,node,weight):
		self.node = node
		self.weight = weight
		
class Node:
	def __init__(self, name, adjacent=None):
		self.name = name
		self.adjacent = adjacent
	
	def add_adjacent(self, a, weight):
		if self.adjacent == None:
			self.adjacent = {}
		self.adjacent[a.name] = Adjacent(a,weight)



def load_graph(file):
	graph = {}
	with open(file) as f:
		data = f.read()
		data = data.split("\n")
		n = int(data[0])
		# read all node
		for i in range(1, n*2 + 1, 2):
			graph[data[i]] = Node(data[i])
		# read all adjacent
		for i in range(1, n*2 + 1, 2):
			adjacents = data[i+1].split("\t")
			for adj in adjacents:
				adj = adj.split("|")
				graph[data[i]].add_adjacent(graph[adj[0]], int(adj[1]))
	return graph

def bfs(graph, start, goal):
	queue = deque([(start,None)])
	expanding_order = []
	path_solution = []
	path_cost = 0
	parent = {}
	found = False
	visited = set()
	i=0
	while not found:
		current = queue.popleft()
		visited.add(current[0])
		expanding_order.append(current)
		if current[0] == goal:
			found = True
		else :
			# expand node
			for k,v in graph[current[0]].adjacent.items():
				if k not in visited:
					queue.append((k,current[0]))
		# verbose
		print("Iterasi "+ str(i))
		i+=1
		print("Current : " + current[0])
		print(queue)
		print()

	# path solution
	curr = expanding_order[-1]
	path_solution.append(curr)
	for x in reversed(expanding_order):
		if x[0] == curr[1]:
			curr = x
			path_solution.append(curr)

	# path cost
	for x in path_solution:
		if x[1] in graph:
			path_cost += graph[x[1]].adjacent[x[0]].weight
			# print(graph[x[1]].adjacent[x[0]].weight)
	return expanding_order, path_solution, path_cost

def main():
	graph = load_graph("graph-romania.txt");
	if len(sys.argv) == 2:
		start = sys.argv[1]
		goal = "Bucharest"
	elif len(sys.argv) == 3:
		start = sys.argv[1]
		goal = sys.argv[2]
	else :
		start = "Arad"
		goal = "Bucharest"

	expanding_order, path_solution, path_cost = bfs(graph, start, goal)

	# print(expanding_order, path_solution, path_cost)
	print("\nExpanding Order : ")
	for x in expanding_order:
		print(x)
	print("\nPath Solution : ")
	for x in reversed(path_solution):
		print(x)
	print("\nPath Cost : ")
	print(path_cost)
if __name__ == '__main__':
	main()