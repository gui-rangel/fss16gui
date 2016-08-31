import rows, syms, nums
import sys

class Table:

	def __init__(self,csv):
		self.csv = csv
		self.rows = []
		headings = rows.csv(csv).next()
		self.cols = [syms.Sym(headings[0]),nums.Num(headings[1]),nums.Num(headings[2]),syms.Sym(headings[3]),nums.Num(headings[4])]


	def add_rows(self, csv):
		headings = rows.csv(csv).next()
		for num,row in enumerate(rows.csv(csv)):
			if num is not 0:
				self.rows.append(row)
				for count,item in enumerate(row):
					self.cols[count].add(item)


table = Table(sys.argv[1])
table.add_rows(sys.argv[1])
for col in table.cols:
	col.show()