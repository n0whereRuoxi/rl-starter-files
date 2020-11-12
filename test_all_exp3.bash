#!/bin/sh
for i in {1..19}
do
for s in {2..16}
do
  sbatch -n 1 -N 1 --share -t 0:15:00 ./1_0_${s}_exp3.sh
done
done
