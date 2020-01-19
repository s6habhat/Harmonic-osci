from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import sys
from tools import getRootDirectory
import csv

if len(sys.argv) >= 2:
	dirs = sys.argv[1:]
else:
	exit(-1)

root_path = getRootDirectory()

for subdir in dirs:
	filename = root_path / subdir
	relative_path = filename.relative_to(root_path / 'data')

	if not filename.exists():
		continue
	with filename.open('r') as csvfile:
		reader = csv.reader(csvfile)
		distances = []
		datas = []
		for i, row in enumerate(reader):
			if i == 0:
				header_min = [float(v) for v in row[1:]]
			elif i == 1:
				header_max = [float(v) for v in row[1:]]
			else:
				distance = float(row[0])
				data = [int(v) for v in row[1:]]
				distances.append(distance)
				datas.append(data)