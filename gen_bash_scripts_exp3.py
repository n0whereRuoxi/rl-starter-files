for size in range(2,17):
    with open('{}_{}_{}_exp3.sh'.format(1,0,size), 'w+') as f:
        f.write('#!/bin/sh\n')
        f.write('python3 -m scripts.train.py --algo ppo --save-interval 10 --lr 0.001 --procs 8 --spec {} {} {}'.format(1,0,size))
