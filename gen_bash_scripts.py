for i in range(7):
    for j in range(i+1):
        for d1, d2 in [(0,0), (0,1), (1,1)]:
            with open('{}_{}_{}_{}.sh'.format(d1, i+1, d2, j+1), 'w+') as f:
                f.write('#!/bin/sh\n')
                f.write('python3 -m scripts.train.py --algo ppo --save-interval 10 --lr 0.001 --procs 8 --spec {} {} {} {}'.format(d1, i+1, d2, j+1))
