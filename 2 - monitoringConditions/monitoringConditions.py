import gym
from gym import spaces
from gym.utils import seeding

import numpy as np

MAXIMUM_RANGE = 342

def sumDiff(list):
    tmp_list = list.copy()    
    if(len(tmp_list) < 3):
        zeroFiller(tmp_list,3)
    diff_1 = tmp_list[0] - 0
    diff_2 = tmp_list[1] - tmp_list[0]
    diff_3 = tmp_list[2] - tmp_list[1]
    #clipping
    if(diff_1 < 0):
        diff_1 = 0
    if(diff_2 < 0):
        diff_2 = 0
    if(diff_3 < 0):
        diff_3 = 0 

    return (diff_1 + diff_2 + diff_3)

def zeroFiller(list,n):
    tmp_lst = list
    size = len(tmp_lst)
    for i in range(size,n):
        tmp_lst.append(0)        
    return tmp_lst

class monitoringConditions(gym.Env):

    def __init__(self, max_action = MAXIMUM_RANGE):
        self.action_space = spaces.Discrete(max_action+1)
        low = np.array([0,0], dtype=np.int32)
        high = np.array([7,MAXIMUM_RANGE], dtype=np.int32)
        self.observation_space = spaces.Box(low,high,dtype=np.int32)

        self.node = 0
        self.action_log = []

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.node = 0
        self.action_log = []
        return (0,0)
    
    def render(self):
        print("State: ",self.node,", Action Log: ",self.action_log)
        return 0

    def step(self, action):
        assert self.action_space.contains(action)
        tmp_state = -1
        tmp_reward = -1
        tmp_finished = False
        if(self.node == 0):
            self.action_log.append(action)
            self.node = 1
            tmp_state = (1,sumDiff(self.action_log))
            tmp_reward = 0.25
        elif(self.node == 1):
            if((self.action_log[0] == 0 or self.action_log[0] == MAXIMUM_RANGE) and (action == 0 or action == MAXIMUM_RANGE)):
                self.action_log.append(action)
                self.node = 2
                tmp_state = (2,sumDiff(self.action_log))
            else:
                self.action_log.append(action)
                self.node = 3
                tmp_state = (3,sumDiff(self.action_log))
            tmp_reward = 0.25
        elif(self.node == 2):
            self.action_log.append(action)
            if(sumDiff(self.action_log) == MAXIMUM_RANGE):
                tmp_state = (4,sumDiff(self.action_log))
                tmp_reward = 0.5
                tmp_finished = True
            else:
                tmp_state = (5,sumDiff(self.action_log))
                tmp_reward = -0.5
                tmp_finished = True 
        elif(self.node == 3):
            self.action_log.append(action)
            if(sumDiff(self.action_log) == MAXIMUM_RANGE):
                self.node = 6
                tmp_state = (6,sumDiff(self.action_log))
                tmp_reward = 0.5
                tmp_finished = True
            else:
                self.node = 7
                tmp_state = (7,sumDiff(self.action_log))
                tmp_reward = -0.5
                tmp_finished = True 
        return tmp_state,tmp_reward,tmp_finished,{str(self.action_log)}

