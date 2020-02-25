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

for subdir_pattern in dirs:
	for subdir in root_path.glob(subdir_pattern):
		filename = root_path / subdir
		relative_path = filename.relative_to(root_path / 'data')

		if not filename.exists() or filename.is_dir():
			continue

		with filename.open('r') as csvfile:
			reader = csv.reader(csvfile)
			hbars = []
			datas = []
			for i, row in enumerate(reader):
				if i == 0:
					header_min = [float(v) for v in row[1:]]
				elif i == 1:
					header_max = [float(v) for v in row[1:]]
				else:
					hbar = float(row[0])
					data = [int(v) for v in row[1:]]
					hbars.append(hbar)
					datas.append(data)


		fig, ax = plt.subplots(figsize=(6,6))
		cs = ax.imshow(datas, extent=[min(header_min), max(header_max), max(hbars), min(hbars)], norm=LogNorm())

		cbar = fig.colorbar(cs)
		cbar.ax.minorticks_off()

		x0, x1 = ax.get_xlim()
		y0, y1 = ax.get_ylim()
		ax.set_aspect(abs(x1-x0)/abs(y1-y0))

		plt.xlabel('position')
		plt.ylabel('$\\hbar$')

		out_filename = root_path / 'imgs' / relative_path
		out_filename.parent.mkdir(parents=True, exist_ok=True)

		plt.savefig(out_filename.with_suffix(".png"))