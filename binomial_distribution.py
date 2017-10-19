import numpy as np
import pandas as pd

def bernoulli_trial(probability_of_yes):
    random_number = np.random.rand(1)[0]
    return probability_of_yes > random_number

def flip_a_fair_coin():
    return bernoulli_trial(0.5)


### This is an example of a binomial trial
flips = 1000
# 1000 True and Falses
coin_flip_binomial_trial = np.array([flip_a_fair_coin() for _ in range(flips)])
# Just for fun let's look at the precentage of heads
should_be_close_to_fifty_precent = (coin_flip_binomial_trial).sum() / flips
print(np.abs(should_be_close_to_fifty_precent - 0.5))

### Let's generalize a binomial trial
### a binomial trial is just a series of bernoulli_trials
def binomial_trial(n, p):
    return np.array([bernoulli_trial(p) for _ in range(n)])



### let's run a bunch of binomial trials to simulate the binomal distribution
bunch_of_binomial_trials = np.array([binomial_trial(1000, 0.5) for _ in range(5000)])
bunch_of_binomial_trials.shape # (5000, 1000)
# 5000 examples of flipping a coin 1000 times


binomial_dist = pd.DataFrame(bunch_of_binomial_trials.sum(1)) # Count the number of Yes (True) in each trial of 1000 flips
min = binomial_dist.min()
max = binomial_dist.max()
pd.DataFrame.hist(binomial_dist, bins=np.arange(min, max)) # This histogram has a similar shape to a binomial distribution




