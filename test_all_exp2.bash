#!/bin/sh
for s in {2..16}
do
  sbatch -n 1 -N 1 --share -t 0:05:00 ./1_0_${s}_exp2.sh
done