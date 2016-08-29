import sys

def zeror(training, testing):

	def train(training):
		yes = 0
		no = 0
		with open(training, "r") as f:
			for line in f:
				if line.startswith("@") or line.startswith("\n"):
					continue
				else:
					data_list = line.split(",")
					if data_list[-1] == "yes\n":
						yes = yes + 1
					else:
						no = no + 1
		if yes > no:
			return "yes\n"
		else:
			return "no\n"

	def test(testing, pred):
		res = ""
		res = res + "=== Predictions on test data ===" + "\n"
		res = res + "inst#	actual	predicted	error_prediction" + "\n"
		num = 0
		with open(testing, "r") as f:
			for line in f:
				
				num = num + 1
				if line.startswith("@") or line.startswith("\n"):
					num = num -1
				else:
					data_list = line.split(",")
					if data_list[-1] == pred:
						res = res + str(num) + "	" + str(data_list[-1].split("\n")[0]) + "	" + pred[0:-1] + "		1" + "\n"
					else:
						res = res + str(num) + "	" + str(data_list[-1].split("\n")[0]) + "	" + pred[0:-1] + "		0" + "\n"
		res = res.replace("no","2:no")
		res = res.replace("yes","1:yes")
		return res

	pred = train(training)
	test = test(testing, pred)
	print test



training = sys.argv[1]
testing = sys.argv[2]
zeror(training, testing)