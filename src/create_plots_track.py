from matplotlib import pyplot as plt
from tools import getRootDirectory
import csv
import sys

if len(sys.argv) >= 2:
	dirs = sys.argv[1:]
else:
	exit(-1)

root_path = getRootDirectory()

for subdir_pattern in dirs:
	for subdir in root_path.glob(subdir_pattern):
		filename = root_path / subdir
		relative_path = filename.relative_to(root_path / 'data')

		if not filename.exists() or filename.is_dir():
			continue

		nums = []
		distances = []

		with filename.open('r') as csvfile:
			reader = csv.reader(csvfile)
			for i, row in enumerate(reader):
				if i == 0:
					pass
				else:
					num = int(row[0])
					distance = float(row[1])
					nums.append(num)
					distances.append(distance)

		print("\n\nComputing file %s:" %relative_path)

		plt.figure()
		plt.errorbar(distances, nums)
		plt.xlabel('Position')
		plt.ylabel('Number')

		out_filename = root_path / 'imgs' / relative_path
		out_filename.parent.mkdir(exist_ok=True)

		plt.savefig(out_filename.with_suffix(".png"))
		plt.savefig(out_filename.with_suffix(".pdf"))