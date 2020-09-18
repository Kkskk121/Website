def solution(src, dest):
    if src == dest:
        return 0
    if src < 0 or src > 63 or dest < 0 or dest > 63:
        return float('inf')
    return bfs(src, dest, 0)
    

class Node:
    
    def __init__(self, l, dist = 0):
        self.l = l
        self.dist = dist
        self.neighborSet = {l+10,l+6,l+17,l+15,l-6,l-10,l-17,l-15}

    def findNeighbors(self,l):
        if self.l <= 15:
            self.neighborSet.remove(l-17)
            self.neighborSet.remove(l-15)
        if self.l <= 7:
            self.neighborSet.remove(l-6)
            self.neighborSet.remove(l-10)
        if self.l >= 48:
            self.neighborSet.remove(l+15)
            self.neighborSet.remove(l+17)
        if self.l >= 56:
            self.neighborSet.remove(l+6)
            self.neighborSet.remove(l+10)
        
        if self.l % 8 == 1 or self.l % 8 == 0:
            if l-10 in self.neighborSet:
                self.neighborSet.remove(l-10)
            if l+6 in self.neighborSet:
                self.neighborSet.remove(l+6)
        if self.l % 8 == 0:
            if l-17 in self.neighborSet:
                self.neighborSet.remove(l-17)
            if l+15 in self.neighborSet:
                self.neighborSet.remove(l+15)
        if self.l % 8 == 6 or self.l % 8 == 7:
            if l-6 in self.neighborSet:
                self.neighborSet.remove(l-6)
            if l+10 in self.neighborSet:
                self.neighborSet.remove(l+10)
        if self.l % 8 == 7:
            if l-15 in self.neighborSet:
                self.neighborSet.remove(l-15)
            if l+17 in self.neighborSet:
                self.neighborSet.remove(l+17)

        return self.neighborSet
            

def bfs(src, dest, level):
    queue = []  #queue implmented as a list
    queue.append(Node(src))
    visited = set()
    visited.add(src)
    while len(queue) > 0:
        
        current = queue.pop(0)
        moves = current.dist
        if current.l == dest:
            return moves

        valid = []
        for n in current.findNeighbors(current.l):
            
            if (n >= 0 and n < 64) and (n not in visited): #if the node is on the chessboard
                queue.append(Node(n,moves+1))
                valid.append(n)
                visited.add(n)
        
    return float('inf')
        

src = input("What's the src: " )
dest = input("What's the destination: " )

for src in range(64):
    for dest in range(64):

        print(src, dest, " ", solution(src,dest))




# from collections import deque


# # queue node used in BFS
# class Node:
# 	# (x, y) represents chess board coordinates
# 	# dist represent its minimum distance from the source
# 	def __init__(self, x, y, dist=0):

# 		self.x = x
# 		self.y = y
# 		self.dist = dist

# 	# As we are using Node as a key in a dictionary,
# 	# we need to implement hashCode() and equals()
# 	def __hash__(self):

# 		return hash((self.x, self.y, self.dist))

# 	def __eq__(self, other):

# 		return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)


# # Below lists details all 8 possible movements for a knight
# row = [2, 2, -2, -2, 1, 1, -1, -1]
# col = [-1, 1, 1, -1, 2, -2, 2, -2]


# # Check if (x, y) is valid chess board coordinates
# # Note that a knight cannot go out of the chessboard
# def valid(x, y, N):
# 	return not (x < 0 or y < 0 or x >= N or y >= N)


# # Find minimum number of steps taken by the knight
# # from source to reach destination using BFS
# def BFS(src, dest, N):

# 	# set to check if matrix cell is visited before or not
# 	visited = set()

# 	# create a queue and enqueue first node
# 	q = deque()
# 	q.append(src)

# 	# loop till queue is empty
# 	while q:

# 		# pop front node from queue and process it
# 		node = q.popleft()

# 		x = node.x
# 		y = node.y
# 		dist = node.dist

# 		# if destination is reached, return distance
# 		if x == dest.x and y == dest.y:
# 			return dist

# 		# Skip if location is visited before
# 		if node not in visited:
# 			# mark current node as visited
# 			visited.add(node)

# 			# check for all 8 possible movements for a knight
# 			# and enqueue each valid movement into the queue
# 			for i in range(8):
# 				# Get the valid position of Knight from current position on
# 				# chessboard and enqueue it with +1 distance
# 				x1 = x + row[i]
# 				y1 = y + col[i]

# 				if valid(x1, y1, N):
# 					q.append(Node(x1, y1, dist + 1))

# 	# return INFINITY if path is not possible
# 	return float('inf')


# if __name__ == '__main__':


#     for i in range(8):
#         for j in range(8):
#             src = Node(i,j)
#             for k in range(8):
#                 dest = Node(j,k)
#                 print("Minimum steps for ",src.x,src.y,dest.x,dest.y," ", BFS(src, dest, 8))
                
                

# 	src = Node(0, 7)   # source coordinates
# 	dest = Node(7, 0)  # destination coordinates

	

            

