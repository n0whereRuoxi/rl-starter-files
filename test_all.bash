#!/bin/sh
for i in {1..4}
do
  for j in $(seq 1 $i)
  do
    sbatch -n 1 -N 1 --share -t 2:00:00 ./0_${i}_0_${j}.sh
    sbatch -n 1 -N 1 --share -t 2:00:00 ./0_${i}_1_${j}.sh
    sbatch -n 1 -N 1 --share -t 2:00:00 ./1_${i}_1_${j}.sh
  done
done
