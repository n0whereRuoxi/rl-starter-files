import gym
import gym_minigrid.envs as envs

def make_env(num_vertical_crossings, num_horizontal_crossings, seed=None):
    env = envs.CrossingEnv(size=9, num_vertical_crossings=num_vertical_crossings, num_horizontal_crossings=num_horizontal_crossings, seed=seed)
    # env = envs.SimpleCrossingS9N3Env()
    print(env.mission)
    print(env)
    return env
