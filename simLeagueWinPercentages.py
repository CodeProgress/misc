import random

def win_percentage(numWins, numLosses):
    denom = float(numWins+numLosses)
    if denom == 0: return "Invalid"
    return numWins/denom

def update_team_records(team1, team2):
    """updates records as if team1 wins"""
    team1[0] += 1
    team2[1] += 1
    

def play_season(numTeams):
    """If a season consists of every team playing every other team once
    returns a list of all team records"""
    teams = [[0,0] for x in range(numTeams)]

    for i in range(numTeams):
        for j in range(i+1, numTeams):
            if random.random() < .5:
                update_team_records(teams[i], teams[j])
            else:
                update_team_records(teams[j], teams[i])
    return teams

def is_over_500(team):
    return win_percentage(*team) > .500

def percent_with_winning_season(teams):
    return sum(1. for x in teams if is_over_500(x))/len(teams)

def best_worst_win_percentage(numTeams, numSeasons):
    """returns a tuple (best, worst) of team winning percentages over numSeasons
    """
    best = 0
    worst = 1
    for i in range(numSeasons):
        teamRecords = play_season(numTeams)
        winPercentages = [win_percentage(*x) for x in teamRecords]
        bestTeam = max(winPercentages)
        worstTeam = min(winPercentages)
        if bestTeam > best:
            best = bestTeam
        if worstTeam < worst:
            worst = worstTeam
    return best, worst



numTeams = 32
example  = play_season(numTeams)

#assert that the season is zero sum
assert abs(sum(win_percentage(*x) for x in example) - numTeams/2.) < 10e-10


print "{} percent of the league had a winning record.".format(
            percent_with_winning_season(play_season(numTeams))*100)

best, worst = best_worst_win_percentage(numTeams, 1000)      
print "The best team's winning percentage was {}".format(best)
print "The worst team's winning percentage was {}".format(worst)
