
import random
import pylab
import math

LN_TWO = math.log(2)

def num_trials_until_fifty_percent_chance_of_duplicate(num_buckets):
    if num_buckets <= 1:
        return 0

    trial_count = 0
    num_remaining_buckets = float(num_buckets)
    probabilityOfNotSharingBirthay = 1.
    while probabilityOfNotSharingBirthay > .5:
        trial_count += 1
        num_remaining_buckets -= 1
        probabilityOfNotSharingBirthay *= (num_remaining_buckets/num_buckets)

    return trial_count


def num_rand_trials_until_duplicate(num_buckets, num_trials=10):
    if num_buckets <= 1:
        return 0
    if num_trials <= 0:
        return 0

    num_picks = 0
    for i in range(num_trials):
        seen = set()
        val = random.randint(1, num_buckets)
        while val not in seen:
            num_picks += 1
            seen.add(val)
            val = random.randint(1, num_buckets)
    return num_picks / float(num_trials)


def analytic_approx(num_buckets):
    return .5 + ((.25+2*LN_TWO*num_buckets)**.5)


num_trials = 366
pylab.scatter(range(1, num_trials),
              [num_rand_trials_until_duplicate(x) for x in range(1, num_trials)],
              label="Random Trials")

pylab.scatter(range(1, num_trials),
              [num_trials_until_fifty_percent_chance_of_duplicate(x) for x in range(1, num_trials)],
              label="Whole Number Trials until Passed 50%",
              alpha=.3)

pylab.scatter(range(1, num_trials), [x**.5 for x in range(1, num_trials)],
              label="Sqrt(x)",
              alpha=.2)

pylab.scatter(range(1, num_trials), [analytic_approx(x) for x in range(1, num_trials)],
              label=".5 + ((.25+2*LN_TWO*num_buckets)**.5)",
              alpha=.3)

pylab.legend()
pylab.xlabel("Number of Buckets")
pylab.ylabel("Number of Trials for 50% Chance of Duplicate")
pylab.title("Approximating the Birthday Paradox")

pylab.show()
