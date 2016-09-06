import random

# toss a fair coin n times.
# heads should come up around n/2 times
# Now take the subset of outcomes immediately following a heads outcome.
# How many are heads? (of this roughly n/2 element subset)


def is_heads(x):
    return x == 1

# Monte Carlo Simulation
num_flips = 100000
outcomes = [random.randint(0, 1) for _ in xrange(num_flips)]

sub_set_outcomes = []
num_events = 0.
for i in xrange(num_flips):
    if is_heads(outcomes[i]): 
        num_events += 1
        # (i+1)%num_flips to avoid IndexError and to wrap the last element to the first
        sub_set_outcomes.append(outcomes[(i+1)%num_flips])

print sum(sub_set_outcomes)/num_events, num_events/num_flips
