class top:

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

class Bfs:
	def get_next(self, x1, y1, x2, y2, field):
		s, f = top(x1, y1), top(x2, y2)
		p = self.search(30, 30, s, f, field)
		path = self.bfs_paths(s, f, p)
		try:
			return path[-2]
		except IndexError:
			return (x1 + 1, y1)

	def search(self, N, M, start, finish, field):
	    used, queue = [[False] * N for i in range(M)], [start]
	    dx = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
	    p = [[None] * N for i in range(M)]
	    p[start.x][start.y] = start
	    while queue:
	        v = queue.pop(0)
	        for direction in dx:
	        	u = top(v.x + direction[0], v.y + direction[1])
		        if u == finish or u.x < N and u.x >=0 and u.y < N and u.y >= 0 and not used[u.x][u.y] and field.get_cell(u.x, u.y) is None:
		        	used[u.x][u.y] = True
		        	p[u.x][u.y] = v
		        	queue.append(u)
		        	if u == finish:
		        		return p
	    return p

	def bfs_paths(self, start, finish, p):
	 	x, y = finish.x, finish.y
	 	if p[x][y] is None:
	 		return []
	 	path = [(x, y)]
	 	while (x != start.x) or (y != start.y):
	 		v = p[x][y]
	 		x, y = v.x, v.y
	 		path += [(x, y)]
	 	return path
