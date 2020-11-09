#!/bin/sh
for i in {1..3}
do
  for j in $(seq 1 $i)
  do
    echo 0_${i}_0_${j}
    sbatch -n 1 -N 1 --share -t 0:05:00 ./0_${i}_0_${j}.sh
    echo 0_${i}_1_${j}
    sbatch -n 1 -N 1 --share -t 0:05:00 ./0_${i}_1_${j}.sh
    echo 1_${i}_1_${j}
    sbatch -n 1 -N 1 --share -t 0:05:00 ./1_${i}_1_${j}.sh
  done
done
