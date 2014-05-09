import random
import pylab

def record_to_win_percentage(wins, losses):
    """If win is worth 10, draw worth 4, loss worth 1
    loss worth 1 because even winless teams have a chance to win in the future"""
    best = (wins + losses)*10.
    if best == 0: return 0.
    score = wins * 10. + losses
    return score/best

def norm_percentages(percent1, percent2):
    """returns percent1, percent2, normed"""
    total = percent1 + percent2
    return (percent1/total, percent2/total)

def does_better_team_win(betterTeamWinPercentage, numGames):
    """returns the number of wins for team1 and team2 in a numGames long series
    betterTeamWinPercentage: float between .5 and 1.0
    numGames: Odd int
    """
    assert numGames % 2 != 0
    assert .5 <= betterTeamWinPercentage <= 1.0
    
    team1wins = 0
    team2wins = 0
    for i in range(numGames):
        if random.random() < betterTeamWinPercentage:
            team1wins += 1
        else:
            team2wins += 1
    return team1wins > team2wins

def sim_confidence_level(betterTeamWinPercentage, numGames, numSeries = 100):
    count = 0.
    for i in range(numSeries):
        if does_better_team_win(betterTeamWinPercentage, numGames):
            count += 1.
    
    return count/numSeries
  
def sim_confidence_levels(betterTeamWinPercentage, numGames, numSeries = 100):
    games = []
    count = 0.
    for i in range(1, numSeries + 1):
        if does_better_team_win(betterTeamWinPercentage, numGames):
            count += 1.
        games.append(count/i)
    
    return games

def sim_trials(prob):
    count = 1
    while random.random() > prob:
        count += 1
    return count

def avg_num_trials_needed(prob, numSims = 10000):
    numTrials = 0.
    for i in range(numSims):
        numTrials += sim_trials(prob)
    return numTrials/numSims


print sim_trials(.01)

print avg_num_trials_needed(.1)
    
### Example

team1 = (30, 20)
team2 = (25, 25)

team1 = record_to_win_percentage(*team1)
team2 = record_to_win_percentage(*team2)

team1, team2 = norm_percentages(team1, team2)

print sim_confidence_level(max(team1, team2), 5)
print sim_confidence_level(max(team1, team2), 7)
print sim_confidence_level(max(team1, team2), 101)

betterTeamWinPercent = .55
numSeries = 100

pylab.plot(sim_confidence_levels(betterTeamWinPercent, 7, numSeries))
pylab.plot([betterTeamWinPercent for i in range(numSeries)])

pylab.show()

