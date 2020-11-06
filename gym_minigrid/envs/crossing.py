from gym_minigrid.minigrid import *
from gym_minigrid.register import register

import itertools as itt


class CrossingEnv(MiniGridEnv):
    """
    Environment with wall or lava obstacles, sparse reward.
    """

    def __init__(self, size=9, num_vertical_crossings=0, num_horizontal_crossings=0, num_crossings=0, obstacle_type=Wall, seed=None):
        self.num_crossings = num_crossings
        self.num_vertical_crossings = num_vertical_crossings
        self.num_horizontal_crossings = num_horizontal_crossings
        self.obstacle_type = obstacle_type
        self.task_feature = [0,0,0,0,1,0,0,0]
        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=False,
            seed=seed
        )

    def _gen_grid(self, width, height):
        assert width % 2 == 1 and height % 2 == 1  # odd size

        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place the agent in the top-left corner
        self.agent_pos = (1, 1)
        self.agent_dir = 0
 
        # Place a goal square in the bottom-right corner
        self.put_obj(Goal(), width - 2, height - 2)

        # Place obstacles (lava or walls)
        v, h = object(), object()  # singleton `vertical` and `horizontal` objects

        if self.num_crossings:
            # print('num_crossings: ', self.num_crossings)
            # Lava rivers or walls specified by direction and position in grid
            rivers = [(v, i) for i in range(2, height - 2, 2)]
            rivers += [(h, j) for j in range(2, width - 2, 2)]
            self.np_random.shuffle(rivers)
            rivers = rivers[:self.num_crossings]  # sample random rivers
        else:
            # Lava rivers or walls specified by direction and position in grid
            v_rivers = [(v, i) for i in range(2, height - 2, 2)]
            h_rivers = [(h, j) for j in range(2, width - 2, 2)]
            self.np_random.shuffle(v_rivers)
            self.np_random.shuffle(h_rivers)
            rivers = v_rivers[:self.num_vertical_crossings] + h_rivers[:self.num_horizontal_crossings]  # sample random rivers

        rivers_v = sorted([pos for direction, pos in rivers if direction is v])
        rivers_h = sorted([pos for direction, pos in rivers if direction is h])
        self.num_vertical_crossings = len(rivers_v)
        self.num_horizontal_crossings = len(rivers_h)
        obstacle_pos = itt.chain(
            itt.product(range(1, width - 1), rivers_h),
            itt.product(rivers_v, range(1, height - 1)),
        )
        for i, j in obstacle_pos:
            self.put_obj(self.obstacle_type(), i, j)

        # Sample path to goal
        path = [h] * len(rivers_v) + [v] * len(rivers_h)
        self.np_random.shuffle(path)

        # Create openings
        limits_v = [0] + rivers_v + [height - 1]
        limits_h = [0] + rivers_h + [width - 1]
        room_i, room_j = 0, 0
        # pos = [2,5,6]
        # wall_index = 0
        # print(self.num_vertical_crossings,self.num_horizontal_crossings)
        for direction in path:
            if direction is h:
                i = limits_v[room_i + 1]
                # if self.num_vertical_crossings == 3:
                    # print(range(limits_h[room_j] + 1, limits_h[room_j + 1]),pos[wall_index])
                j = self.np_random.choice(range(limits_h[room_j] + 1, limits_h[room_j + 1]))
                # j = range(limits_h[room_j] + 1, limits_h[room_j + 1])[pos[wall_index]]
                    # wall_index += 1
                # else:
                #     j = range(limits_h[room_j] + 1, limits_h[room_j + 1])[4]

                room_i += 1
            elif direction is v:
                # if self.num_vertical_crossings == 3:
                # i = range(limits_v[room_i] + 1, limits_v[room_i + 1])[3]
                # else:
                i = self.np_random.choice(range(limits_v[room_i] + 1, limits_v[room_i + 1]))
                j = limits_h[room_j + 1]
                room_j += 1
            else:
                assert False
            self.grid.set(i, j, None)

        self.mission = (
            # "avoid the lava and get to the green goal square"
            # if self.obstacle_type == Lava
            # else "find the opening and get to the green goal square"
            'cross {} vertical walls and {} horizontal walls'.format(self.num_vertical_crossings, self.num_horizontal_crossings)
        )

class LavaCrossingEnv(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=1)

class LavaCrossingS9N2Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=2)

class LavaCrossingS9N3Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=3)

class LavaCrossingS11N5Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=11, num_crossings=5)

register(
    id='MiniGrid-LavaCrossingS9N1-v0',
    entry_point='gym_minigrid.envs:LavaCrossingEnv'
)

register(
    id='MiniGrid-LavaCrossingS9N2-v0',
    entry_point='gym_minigrid.envs:LavaCrossingS9N2Env'
)

register(
    id='MiniGrid-LavaCrossingS9N3-v0',
    entry_point='gym_minigrid.envs:LavaCrossingS9N3Env'
)

register(
    id='MiniGrid-LavaCrossingS11N5-v0',
    entry_point='gym_minigrid.envs:LavaCrossingS11N5Env'
)

class SimpleCrossingEnv(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_vertical_crossings=1, obstacle_type=Wall)
    def info(self):
        print(self.__class__)

class SimpleCrossingS9N1Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=1, obstacle_type=Wall)

class SimpleCrossingS9N2Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=2, obstacle_type=Wall)

class SimpleCrossingS9N3Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=9, num_crossings=3, obstacle_type=Wall)

class SimpleCrossingS11N5Env(CrossingEnv):
    def __init__(self):
        super().__init__(size=11, num_crossings=5, obstacle_type=Wall)

register(
    id='MiniGrid-SimpleCrossingS9N1-v0',
    entry_point='gym_minigrid.envs:SimpleCrossingEnv'
)

register(
    id='MiniGrid-SimpleCrossingS9N2-v0',
    entry_point='gym_minigrid.envs:SimpleCrossingS9N2Env'
)

register(
    id='MiniGrid-SimpleCrossingS9N3-v0',
    entry_point='gym_minigrid.envs:SimpleCrossingS9N3Env'
)

register(
    id='MiniGrid-SimpleCrossingS11N5-v0',
    entry_point='gym_minigrid.envs:SimpleCrossingS11N5Env'
)
