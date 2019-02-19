import os
import csv

class Parser(object):
	def parse(path):
		lines = []
		with open(path, "r") as file :
			for line in file:
				txt = line.rstrip().split(" ")[::-1]
				val = txt.pop()
				div = {
					"val" : val,
					"next" : txt
				}
				lines.append(div)

		return lines
