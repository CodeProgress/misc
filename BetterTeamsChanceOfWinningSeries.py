import pylab
import random


outcomes = []
for s_length in range(1, 101, 2):
    a = .6
    series_length = s_length
    num_trials = 1000
    
    num_series_wins = 0
    for trial in range(num_trials):
        counter = 0
        for game in xrange(series_length):
            if random.random() < a:
                counter += 1
        
            if counter >= (series_length/2)+1:
                num_series_wins += 1
                break
    
    outcomes.append(num_series_wins/float(num_trials))
    
pylab.plot(range(1, 101, 2), outcomes)
pylab.show()
