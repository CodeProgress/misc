
import pylab

def probability_of_shared_birthday_in_group(numPeopleInGroup):
    if numPeopleInGroup >= 366: return 1
    if numPeopleInGroup <= 1:   return 0
    
    probabilityOfNotSharingBirthay = 1.
    for i in range(366, 366-numPeopleInGroup, -1):
        probabilityOfNotSharingBirthay *= i/366.
        
    return 1 - probabilityOfNotSharingBirthay
    
daysInAYear = 365
daysInAYearList = range(1, daysInAYear + 1)
probabilities = [probability_of_shared_birthday_in_group(x) for x in daysInAYearList]

pylab.plot(daysInAYearList, probabilities)
pylab.xlabel("Number of People")
pylab.ylabel("Probability of Shared Birthday")
pylab.show()
