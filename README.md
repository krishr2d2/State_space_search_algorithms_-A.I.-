# State_space_search_algorithms_-A.I.-
Assignment-1(AI@iiits)
The current repository includes state-space search algorithms : Breadth-First search(BFS), Bidirectional search(bds), Depth-first search(dfs) and Uniform-cost search(ucs) applied on the 8-puzzle problem.

1. assign_1_bfs :
	Each 'Node' class consists of :
									a list that holds the 8-puzzle configuration.
									an integer that gives the current space(represented by 0) position.
									a reference node that stores the reference to its parent.
									methods :
												swap --> to swap two elements in the list.
												left --> to move the space left
												right --> to move the space right
												up -----> to move the space top
												down ---> to move the space down
												printconfig ---> to print the 8-puzzle configuration
	
	The bfs function implements the bfs algorithm provided with the input : an empty queue, start node, end config...
	The exhaust_Set is the closed list that maintains the explored Nodes in the tree...
	Queue-order :
				[up,right,down,left]
	
	Input : space seperated integer string (saved as the start list) through terminal.
	output : if there is a solution, the path to the solution is printed using backtracking.
	
2. assign_1_dfs :
	All the code is similar to that of bfs except that the popping order from the list is backwards(stacck implementation..).
	Stack-Order :
				[up,right,down,left]
				
	Input : space seperated integer string (saved as the start list) through terminal.
	Output : the path to the solution is printed using backtracking.
	
3. assign_1_bds :
	Most of the code is similar to that of the rest except that we are maintaining two exhaust_Sets : one for backward search and one for forward search.
	Other than that there are also two extra lists to store the explored nodes so that the path-printing would be easy using backtracking.
	Queue-1 order :
				[up,down,right,left]
	Queue-2 order :
				[up,down,right,left]
				
	Input : space seperated integer string (saved as the start list) through terminal.
	Output : the path to the goal node is printed using backtracking.
	
4. assign_1_ucs :
	All the code is same as that of bfs, dfs except that there is another parameter called 'cost' assosciated with each node.
	For every swap, this cost is updated depending on the tile being swapped.
	In the queue being used, the nodes are pushed in an order such that the minimum cost node is pushed first.
	Queue-order :
				depends on the cost order on every iteration...
			
	Input : space seperated integer string (saved as the start list) through terminal.
	Output : the path to the goal node is printed using backpropagation.
