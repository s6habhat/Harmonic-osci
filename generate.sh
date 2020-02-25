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

# evolution of a step state
if [ ! -f data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv"
    $PYTHON src/harmonic_oscillator.py -m 0.25 -i 100 -N 100 --step
else
    echo "Not generating file data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv"
fi
$PYTHON src/create_plots_track.py data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv -i 1 10 20 40 80 100
$PYTHON src/create_plots_track_shifted.py data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv -i 1 10 20 40 80 100
$PYTHON src/create_plots_track_shifted.py data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv -i 1 5 10 15 20 25
$PYTHON src/create_plots_track_shifted.py data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv -i 1 2 3 4 5 6 7 8 9 10
$PYTHON src/create_plots_track_shifted.py data/harmonic_oscillator_track/N100i100initstepm0.2500step.csv -i 1 3 5 7 9 11 13 15

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

# classical limit harmonic oscillator
if [ ! -f data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-5.00-5.00-0.10-N1000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-5.00-5.00-0.10-N1000.csv"
    $PYTHON src/harmonic_oscillator_classical_limit.py -N 1000
else
    echo "Not generating file data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-5.00-5.00-0.10-N1000.csv"
fi
$PYTHON src/create_plots_classical_limit.py data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-5.00-5.00-0.10-N1000.csv

echo


if [ ! -f data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-3.00-3.00-0.05-N1000.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-3.00-3.00-0.05-N1000.csv"
    $PYTHON src/harmonic_oscillator_classical_limit.py -N 1000 -b " -3:3:0.05"
else
    echo "Not generating file data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-3.00-3.00-0.05-N1000.csv"
fi
$PYTHON src/create_plots_classical_limit.py data/harmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-3.00-3.00-0.05-N1000.csv

echo

# classical limit anharmonic oscillator
if [ ! -f data/anharmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-10.00-10.00-0.10-N100.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-10.00-10.00-0.10-N100.csv"
    $PYTHON src/anharmonic_oscillator_classical_limit.py -N 100 -b " -10:10:0.1" -init -5 -ir 2 -i 1000
else
    echo "Not generating file data/anharmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-10.00-10.00-0.10-N100.csv"
fi
$PYTHON src/create_plots_classical_limit.py data/anharmonic_oscillator_classical_limit/h0.00-2.00-0.0100_-10.00-10.00-0.10-N100.csv

echo

# lambda parameter anharmonic oscillator
if [ ! -f data/anharmonic_oscillator_lambda_parameter/d0.00-10.00-0.10s-5.00-5.00-0.10-N1000-i100.csv ] || [ "${1}" = "-f" ] || [ "${1}" = "--force" ]; then
    echo "Generating file data/anharmonic_oscillator_lambda_parameter/d0.00-10.00-0.10s-5.00-5.00-0.10-N1000-i100.csv"
    $PYTHON src/anharmonic_oscillator_lambda_parameter.py -init 0 -ir 10 -i 100 -N 1000
else
    echo "Not generating file data/anharmonic_oscillator_lambda_parameter/d0.00-10.00-0.10s-5.00-5.00-0.10-N1000-i100.csv"
fi
$PYTHON src/create_plots_lambda_parameter.py data/anharmonic_oscillator_lambda_parameter/d0.00-10.00-0.10s-5.00-5.00-0.10-N1000-i100.csv

echo