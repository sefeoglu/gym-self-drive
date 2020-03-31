import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw, show
import time

def display_rewards(rewards):
    rewards = np.array(rewards)
    x = np.linspace(0, len(rewards)-1, len(rewards)).repeat(rewards.shape[1])

    mean = np.mean(rewards, axis=1)
    mx = np.max(rewards, axis=1)
    mn = np.min(rewards, axis=1)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(x, rewards.flatten(), s=8)
    ax.plot(mean, c='g', label='Averages')
    ax.plot(mn, c='r', label='Minimum')
    ax.plot(mx, c='y', label='Maximums')

    plt.legend(loc='upper left')

    plt.xlabel('Generations', fontsize=10)
    plt.xticks(np.arange(min(x), max(x)+1, 10))

    plt.ylabel('Reward', fontsize=10)

    show(block=False)
    plt.pause(60)
    plt.close(fig)

if __name__ == '__main__':
    while True:
        rewards = list(np.load('./results/rewards4-2.npy'))
        display_rewards(rewards)