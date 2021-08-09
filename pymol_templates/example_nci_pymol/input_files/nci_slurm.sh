#!/bin/bash
#SBATCH -J $1
#SBATCH -p shas
#SBATCH --qos normal
#SBATCH -t 00:59:59
#SBATCH -N 1

# setting environment for NCI program
export NCIPLOT_HOME='/projects/rpaton@colostate.edu/nciplot-3.0'

$NCIPLOT_HOME/nciplot $1.nci $1.out


