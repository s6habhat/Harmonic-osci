from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import sys
from tools import getRootDirectory
import csv
import numpy as np

if len(sys.argv) >= 2:
	dirs = sys.argv[1:]
else:
	exit(-1)

root_path = getRootDirectory()

for subdir_pattern in dirs:
	for subdir in root_path.glob(subdir_pattern):
		filename = root_path / subdir
		relative_path = filename.relative_to(root_path / 'data')

		if not filename.exists():
			continue
		with filename.open('r') as csvfile:
			reader = csv.reader(csvfile)
			positions = []
			for i, row in enumerate(reader):
				if i == 0:
					header_min = row[:]
				else:
					num = int(row[0])
					position = float(row[1])
					positions.append(position)
		print("\n\nComputing file %s:" %relative_path)
		positions = np.array(positions)
		print(positions)