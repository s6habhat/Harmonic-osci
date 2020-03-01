from matplotlib import pyplot as plt
import matplotlib
from tools import getRootDirectory, getColorIterator, autoCorrelationNormalized
import csv
import numpy as np
import scipy.optimize as op

import argparse
from glob import glob

import itertools
flatten = itertools.chain.from_iterable

color_iterator = getColorIterator()

def linear(x, *p):
	a, b = p
	return a * x + b

parser = argparse.ArgumentParser(description='Calculate the autorelation function.')
parser.add_argument('filenames', nargs='*')
parser.add_argument('-i', '--iterations', nargs='+')
parser.add_argument('-f', '--fit', action='store_true')
args = parser.parse_args()

filenames = list(flatten([glob(arg) for arg in args.filenames]))

root_path = getRootDirectory()

for file in filenames:
	full_path = (root_path / file)
	if not full_path.exists() or full_path.is_dir():
		continue

	relative_path = full_path.relative_to(root_path / 'data')

	print('[Autocorrelation Metropolis] Computing file %s ... ' %relative_path, end='')

	data = {}

	with full_path.open('r') as csvfile:
		reader = csv.reader(csvfile)
		for i, row in enumerate(reader):
			if i == 0:
				numbers = np.array([int(r) for r in row[1:]])
				pass
			else:
				num = int(row[0])
				positions = np.array([float(r) for r in row[1:]])
				data[num] = positions

	plt.figure()
	min_ = 100
	max_ = -100

	metropolis_iterations = np.array(sorted(data.keys()))

	data = np.array([data[num] for num in metropolis_iterations])
	#print(data.dtype, data.shape)

	color_plot, color_fit = next(color_iterator)['color']
	ydata_sum = np.zeros(len(metropolis_iterations))
	xdata = metropolis_iterations
	#for i in range(iteration, iteration + 10):
	for i in range(data.shape[1]):
		positions = data[:,i]
		ydata = autoCorrelationNormalized(positions, xdata)

		ydata_sum += ydata

	ydata_mean = ydata_sum / data.shape[1]
	#print(ydata_mean)
	plt.errorbar(xdata, ydata_mean, label='Autocorrelation function', fmt='.', color=color_plot)
	if args.fit:
		try:
			parameters, parameters_error = op.curve_fit(linear, bins_mid, hits, p0=[1, 1])
			parameters_error = np.sqrt(np.diag(parameters_error))
			xdata_fit = np.linspace(min(bins), max(bins), 1000)
			ydata_fit = gauss(xdata_fit, *parameters)
			plt.plot(xdata_fit, ydata_fit, color=color_fit)
		except:
			pass

	plt.xlabel('Metropolis iteration')
	plt.ylabel('$\Gamma(t)$')
	plt.yscale('log')
	plt.legend()

	#plt.xlim(0, 1)

	out_filename = root_path / 'imgs' / relative_path
	out_filename.parent.mkdir(parents=True, exist_ok=True)

	out_filename = out_filename.with_suffix('')
	out_filename = '%s_autocorrelation_metropolis_' %(out_filename)

	plt.savefig(out_filename + '.png')
	print('done')
	#plt.savefig(out_filename + '.pdf')