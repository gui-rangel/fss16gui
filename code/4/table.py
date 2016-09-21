import rows, syms, nums
import sys

class Table:

	def __init__(self):
		self.rows = []
		self.cols = []

	def add_rows(self, csv):
		for row in rows.csv(csv):
			if self.cols == []:
				self.cols = [syms.Sym(row[0]),nums.Num(row[1]),nums.Num(row[2]),syms.Sym(row[3]),nums.Num(row[4])]
			else:
				self.rows.append(row)
				for count,item in enumerate(row):
					self.cols[count].add(item,count)
	
	def distance(self,r1,r2):
		f,d,n = 2, 0, 10**-32
		for col in (self.cols[0:-1]):
			x, y  = r1[col.pos], r2[col.pos]
			n    += 1
			inc   = col.dist(x,y)**f
			d    += inc
		return d

	def closest_row(self,row_x):
		closest,low = None,10e32
		for row in self.rows:
			if row != row_x:
				dist = self.distance(row,row_x)
				if dist<low:
					low = dist
					closest = row
		return closest

	def furthest_row(self,row_x):
		furthest,high = None,-10e32
		for row in self.rows:
			if row != row_x:
				dist = self.distance(row,row_x)
				if dist>high:
					high = dist
					furthest = row
		return furthest

	def closest_furthest(self, row_x):
		closest = table.closest_row(row_x)
		furthest = table.furthest_row(row_x)
		print 'Row - {};  Closest - {}; Furthest - {}'.format(row_x,closest,furthest)


if __name__ == "__main__":
	table = Table()
	table.add_rows(sys.argv[1])
	table.closest_furthest(table.rows[0])
	table.closest_furthest(table.rows[1])

