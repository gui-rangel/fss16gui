import rows, syms, nums
import sys

class Table:

	def __init__(self,csv):
		self.csv = csv
		self.rows = []
		headings = rows.csv(csv).next()
		self.cols = [syms.Sym(headings[0]),nums.Num(headings[1]),nums.Num(headings[2]),syms.Sym(headings[3]),nums.Num(headings[4])]

	def add_rows(self, csv):
		for num,row in enumerate(rows.csv(csv)):
			if num is not 0:
				self.rows.append(row)
				for count,item in enumerate(row):
					self.cols[count].add(item,count)
	
	def distance(self,r1,r2):
		# UNKNOWN = "?"
		f,d,n = 2, 0, 10**-32
		for num,col in enumerate(self.cols):
			if num is not len(self.cols)-1:
				x, y  = r1[col.pos], r2[col.pos]
				# if x is UNKNOWN and y is UNKNOWN:
				# 	continue
				# if x is UNKNOWN: x=col.my.furthest(y)
				# if y is UNKNOWN: y=col.my.furthest(x)
				n    += 1
				inc   = col.dist(x,y)**f
				d    += inc
		# return (d**(1/f)) / (n**(1/f))
		return d

	def closest_furthest(self, rowx):
		closest,furthest = None,None
		low,high = 10e32,-10e32
		for row in table.rows:
			if row is not rowx:
				dist = table.distance(row,rowx)
				if dist>high:
					high = dist
					furthest = row
				if dist<low:
					low = dist
					closest = row
		print 'Row - {};  Closest - {}; Furthest - {}'.format(rowx,closest,furthest)

if __name__ == "__main__":
	table = Table(sys.argv[1])
	table.add_rows(sys.argv[1])
	# table.closest_furthest(table.rows[0])
	# table.closest_furthest(table.rows[1])

