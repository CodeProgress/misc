import random

def win_percentage(numWins, numLosses):
    denom = float(numWins+numLosses)
    if denom == 0: return "Invalid"
    return numWins/denom

def update_team_records(team1, team2):
    """updates records as if team1 wins"""
    team1[0] += 1
    team2[1] += 1
    

def play_season(teams):
    index = len(teams)
    for i in range(index):
        for j in range(i+1, index):
            if random.random() < .5:
                update_team_records(teams[i], teams[j])
            else:
                update_team_records(teams[j], teams[i])

            
teams = [[0,0] for x in range(32)]

play_season(teams)

print teams
