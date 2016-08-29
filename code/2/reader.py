import rows, syms, nums
import sys

class Table:

	def __init__(self,csv):
		self.csv = csv
		self.rows = []
		self.cols = [syms.Sym(),nums.Num(),nums.Num(),syms.Sym(),nums.Num()]


	def add_rows(self, csv):
		headings = rows.csv(csv).next()
		for num,row in enumerate(rows.csv(csv)):
			if num is not 0:
				self.rows.append(row)
				for count,item in enumerate(row):
					self.cols[count].add(item)


table = Table(sys.argv[1])
table.add_rows(sys.argv[1])
# for col in table.cols:
#   col.show()