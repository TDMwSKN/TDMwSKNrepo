import gym
import argparse
import numpy as np
from monitoringConditions import *

# noinspection PyTypeChecker
def open_file_and_save(file_path, data):
    """
    :param file_path: type==string
    :param data:
    """
    try:
        with open(file_path, 'wb') as f_handle:
            np.savetxt(f_handle, data, fmt='%s')
    except FileNotFoundError:
        with open(file_path, 'wb') as f_handle:
            np.savetxt(f_handle, data, fmt='%s')

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--iteration', default=20, type=int)
    return parser.parse_args()

def main(args):
    env = monitoringConditions()
    env.seed(0)
    ob_space = env.observation_space
    obs = env.reset()
    observations = []
    actions = []

    for episode in range(args.iteration):
        step = 0

        env.reset()

        while True:
            if(step == 0): 
                action = 70
            if(step == 1): #Rounded Down from 96.66667
                action = 96
            if(step == 2): #Rounded Down from 342.020202
                action = 342

            observations.append(obs)
            actions.append(action)

            next_obs, reward, done, info = env.step(action)
            step += 1

            if done == True:
                print(step)
                obs = env.reset()
                break
            else:
                obs = next_obs

    observations = np.reshape(observations, newshape=[-1] + list(ob_space.shape))
    actions = np.array(actions).astype(dtype=np.int32)

    open_file_and_save('trajectory/observations.csv', observations)
    open_file_and_save('trajectory/actions.csv', actions)

if __name__ == "__main__":
    args = argparser()
    main(args)