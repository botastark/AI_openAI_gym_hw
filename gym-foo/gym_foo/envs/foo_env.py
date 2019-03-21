import random
from gym import spaces

import gym
import numpy as np

class FooEnv(gym.Env):

    def __init__(self):
        self.env=np.zeros((9,9), dtype=int)
        #0 for empty spaces, 1 for a invaders for 9 by 9 space, there are 9 invaders
        for i in range(3):
            self.env[2*i+1][2]=1
            self.env[2*i+1][4]=1
            self.env[2*i+1][6]=1
            
        self.reward=0
        self.curr_score=0
        self.max_score = 180
        self.is_win = False
        
        #  what the agent can do: shoot, move right or left
        self.action_space = spaces.Discrete(3)
        self.agent_loc=4 #init loc is middle 4
        self.observation_space = spaces.Box(low=0, high=1, shape=(9, 9, 1), dtype=int)
        
        
    def step(self, action):
        
        if self.is_win:
            raise RuntimeError("Episode is done")
        self._take_action(action)
        reward = self._get_reward()
        ob = self._get_state()
        
        return ob, reward, self.is_win, {}
            
    def _take_action(self, action):
        """
        actions
        0 : fire
        1 : move left
        2 : move right
        """
        if action==1:
            if self.agent_loc>0: #move only when not at leftmost leftmost loc
                self.agent_loc-=1
                self.reward=0
        elif action==2:             
            if self.agent_loc<8: #move only when not at rightmost leftmost loc
                self.agent_loc+=1
                self.reward=0
        else:
            #print("FIRE")
            if self.env[5][self.agent_loc]==1:
                self.reward=10
                self.env[5][self.agent_loc]=0
            elif self.env[3][self.agent_loc]==1:
                self.reward=20
                self.env[3][self.agent_loc]=0
            elif self.env[1][self.agent_loc]==1:
                self.reward=30
                self.env[1][self.agent_loc]=0
            else:
                self.reward=0
                pass
            self.curr_score+=self.reward
#            if self.reward!=0:
#                print(self.env)
#            print("Current score is ", self.curr_score," ")
            
        if self.curr_score == self.max_score:
            self.is_win = True

    def _get_reward(self):
        return self.reward
    
    def _get_state(self):
        return self.env
    
    def seed(self, seed):
        random.seed(seed)
        np.random.seed
        
    def reset(self):
        """
        Reset the state of the environment and returns an initial observation.
        Returns
        -------
        observation (object): the initial observation of the space.
        """
        self.is_win = False
        for i in range(3):
            self.env[2*i+1][2]=1
            self.env[2*i+1][4]=1
            self.env[2*i+1][6]=1
        self.curr_score=0
        return self._get_state()
