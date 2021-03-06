import random
import pylab

totalCost = 0.
numTrials = 1000

outcomes = []

for j in range(51, 151):
    for i in xrange(numTrials):
        high = 150
        low  = 51
        cost    = 0
        correct = random.randint(low, high)
        #guess   = random.randint(low, high)
        guess   = j
        guesses = 0
        
        while guess != correct:
            if guess < correct:
                cost += 1
                low = guess + 1
            else:
                cost += 10
                high = guess - 1
            #diff strategies
            
            #guess average
            guess = (low + high) / 2
            
            #guess random
            #guess = random.randint(low, high)
            
            guesses += 1
            
            #print low, high, guess
        totalCost += cost
    
    outcomes.append(totalCost/numTrials)
    totalCost = 0.

lowest = [0, 99999, 0]
for k in range(len(outcomes)):
    index = k+51
    tcost = outcomes[k]
    print index, tcost
    if tcost < lowest[1]:
        lowest[0] = index
        lowest[1] = tcost
        lowest[2] = k

print "Lowest =", lowest

pylab.plot(range(51, 151), outcomes)
pylab.xlabel('Staring guess')
pylab.ylabel("Total cost")
pylab.show()

#Sample output for numTrials = 1000000:
#
#51 25.253573
#52 25.0347
#53 24.880493
#54 24.828799
#55 24.7889
#56 24.469373
#57 24.276644
#58 24.135452
#59 23.917172
#60 23.685744
#61 23.626037
#62 23.553659
#63 23.535269
#64 23.406374
#65 23.368233
#66 23.421201
#67 23.335025
#68 23.220754
#69 23.194963
#70 23.27698
#71 23.359838
#72 23.219895
#73 23.208097
#74 23.290168
#75 23.255458
#76 23.232858
#77 23.317861
#78 23.461017
#79 23.613868
#80 23.711097
#81 23.865567
#82 24.120946
#83 24.10538
#84 24.068052
#85 24.180796
#86 24.319754
#87 24.504142
#88 24.348897
#89 24.238797
#90 24.239322
#91 24.159731
#92 24.040579
#93 24.035127
#94 24.14885
#95 24.222277
#96 24.231813
#97 24.34043
#98 24.509513
#99 24.528938
#100 24.50198
#101 24.583668
#102 24.779618
#103 24.963136
#104 24.955212
#105 25.049323
#106 25.215642
#107 25.326429
#108 25.400188
#109 25.600166
#110 25.831207
#111 26.11452
#112 26.307525
#113 26.589655
#114 26.926391
#115 26.961172
#116 26.957176
#117 27.075024
#118 27.257705
#119 27.428447
#120 27.374804
#121 27.377441
#122 27.486393
#123 27.523993
#124 27.547146
#125 27.676578
#126 27.878091
#127 28.043565
#128 28.163019
#129 28.370672
#130 28.672423
#131 28.768148
#132 28.869492
#133 29.046792
#134 29.348407
#135 29.654999
#136 29.773706
#137 29.996873
#138 30.287283
#139 30.471461
#140 30.703115
#141 31.019886
#142 31.39712
#143 31.766711
#144 32.095175
#145 32.483657
#146 32.974234
#147 33.193383
#148 33.447491
#149 33.757834
#150 34.189122
#Lowest = [69, 23.194963, 18]
