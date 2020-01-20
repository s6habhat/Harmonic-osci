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

	if not filename.exists() or filename.is_dir():
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


	fig, ax = plt.subplots(figsize=(6,6))
	cs = ax.imshow(datas, extent=[min(header_min), max(header_max), max(distances), min(distances)], norm=LogNorm())

	cbar = fig.colorbar(cs)
	cbar.ax.minorticks_off()

	plt.plot([+d / 2 for d in distances], distances, color='black', label='Classical Minima')
	plt.plot([-d / 2 for d in distances], distances, color='black')

	x0,x1 = ax.get_xlim()
	y0,y1 = ax.get_ylim()
	ax.set_aspect(abs(x1-x0)/abs(y1-y0))

	plt.xlabel('position')
	plt.ylabel('minima distance')

	plt.legend()

	out_filename = root_path / 'imgs' / relative_path
	out_filename.parent.mkdir(exist_ok=True)

	plt.savefig(out_filename.with_suffix(".png"))
	plt.savefig(out_filename.with_suffix(".pdf"))