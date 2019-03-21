#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import gym
import gym_foo

env = gym.make('foo-v0')
#print(env.observation_space)
#print(env.action_space)

env.seed(0)
env.reset()
env.step(0)

for i_episode in range(50):
    observation = env.reset()
    for t in range(400):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        #print(observation)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
