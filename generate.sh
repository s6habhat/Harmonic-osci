#!/bin/bash

PYTHON="/usr/bin/python3"

if [ "${1}" = "-h" ] || [ "${1}" = "--help" ]; then
    echo "usage: ${0} [-h] [-c] [-f]"
	echo
	echo "Create and plot the data"
	echo
	echo "optional arguments:"
	echo "  -h, --help		show this help message and exit"
	echo "  -c, --clean		clean data and image directories"
	echo "  -f, --force		force overwrite of data files"
    exit 1
fi

# cleanup
if [ "${1}" = "-c" ] || [ "${1}" = "--clean" ]; then
    rm -r data/* 2> /dev/null
    rm -r imgs/* 2> /dev/null
    exit 1
fi

# harmonic oscillator

# evolution of path from 5 to 0
if [ ! -f data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv"
    $PYTHON src/harmonic_oscillator.py -m 0.25 -init 5 -ir 1 -i 100 -N 100
else
    echo "Not generating file data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv"
fi
$PYTHON src/create_plots_track.py data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv -i 1 10 20 40 80 100
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv -i 1 10 20 40 80 100 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N100i100init5.0000m0.2500.csv -i 10 20 40 80 100 -f

echo

# evolution of path from 5 to 0
if [ ! -f data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv"
    $PYTHON src/harmonic_oscillator.py -m 0.25 -init 5 -ir 1 -i 100 -N 1000
else
    echo "Not generating file data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv"
fi
$PYTHON src/create_plots_track.py data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv -i 1 10 20 40 80 100
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv -i 1 10 20 40 80 100 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N1000i100init5.0000m0.2500.csv -i 10 20 40 80 100 -f

echo

# evolution of path from 5 to 0
if [ ! -f data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv"
    $PYTHON src/harmonic_oscillator.py -m 0.25 -init 5 -ir 1 -i 100 -N 10000
else
    echo "Not generating file data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv"
fi
$PYTHON src/create_plots_track.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 1 10 20 40 80 100
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 1 10 20 40 80 100 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 10 20 40 80 100 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 1 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 10 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 20 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 40 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 80 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N10000i100init5.0000m0.2500.csv -i 100 -f

echo

# evolution of path from 5 to 0 better
if [ ! -f data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv"
    $PYTHON src/harmonic_oscillator.py -m 0.25 -init 5 -ir 1 -i 1000 -N 1000
else
    echo "Not generating file data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv"
fi
$PYTHON src/create_plots_track.py data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv -i 1 10 20 40 80 100 1000
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv -i 1 10 20 40 80 100 1000 -f
$PYTHON src/create_plots_gauss.py data/harmonic_oscillator_track/N1000i1000init5.0000m0.2500.csv -i 10 20 40 80 100 1000 -f

echo


# anharmonic oscillator

if [ ! -f data/anharmonic_oscillator_track/N100i1000init0.0m0.2500l-0.0200d10.0000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_track/N100i1000init0.0m0.2500l-0.0200d10.0000.csv"
    $PYTHON src/anharmonic_oscillator.py -m 0.25 -init 0 -ir 10 -i 1000 -N 100
else
    echo "Not generating file data/anharmonic_oscillator_track/N100i1000init0.0m0.2500l-0.0200d10.0000.csv"
fi
$PYTHON src/create_plots_track.py data/anharmonic_oscillator_track/N100i1000init0.0m0.2500l-0.0200d10.0000.csv -i 1 10 20 40 80 100 1000
$PYTHON src/create_plots_track.py data/anharmonic_oscillator_track/N100i1000init0.0m0.2500l-0.0200d10.0000.csv -i 1 50 100 200 400 1000

echo

if [ ! -f data/anharmonic_oscillator_track/N1000i1000init0.0m0.2500l-0.0200d10.0000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_track/N1000i1000init0.0m0.2500l-0.0200d10.0000.csv"
    $PYTHON src/anharmonic_oscillator.py -m 0.25 -init 0 -ir 10 -i 1000 -N 1000
else
    echo "Not generating file data/anharmonic_oscillator_track/N1000i1000init0.0m0.2500l-0.0200d10.0000.csv"
fi
$PYTHON src/create_plots_track.py data/anharmonic_oscillator_track/N1000i1000init0.0m0.2500l-0.0200d10.0000.csv -i 1 10 20 40 80 100 1000

echo

if [ ! -f data/anharmonic_oscillator_track/N100i10000init0.0m0.2500l-0.0200d10.0000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_track/N100i10000init0.0m0.2500l-0.0200d10.0000.csv"
    $PYTHON src/anharmonic_oscillator.py -m 0.25 -init 0 -ir 10 -i 10000 -N 100
else
    echo "Not generating file data/anharmonic_oscillator_track/N100i10000init0.0m0.2500l-0.0200d10.0000.csv"
fi
$PYTHON src/create_plots_track.py data/anharmonic_oscillator_track/N100i10000init0.0m0.2500l-0.0200d10.0000.csv -i 100 1000 2000 3000 5000 10000

echo

if [ ! -f data/anharmonic_oscillator_track/N200i10000init0.0m0.2500l-0.0200d10.0000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_track/N200i10000init0.0m0.2500l-0.0200d10.0000.csv"
    $PYTHON src/anharmonic_oscillator.py -m 0.25 -init 0 -ir 10 -i 10000 -N 200
else
    echo "Not generating file data/anharmonic_oscillator_track/N200i10000init0.0m0.2500l-0.0200d10.0000.csv"
fi
$PYTHON src/create_plots_track.py data/anharmonic_oscillator_track/N200i10000init0.0m0.2500l-0.0200d10.0000.csv -i 100 1000 2000 3000 5000 10000

echo