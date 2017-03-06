import random, sys

class QLearning():

    #final DecimalFormat df = new DecimalFormat("#.##");
 
    ## path finding
    alpha = 0.1;
    gamma = 0.9;

    ## states A,B,C,D,E,F
    ## e.g. from A we can go to B or D
    ## from C we can only go to C 
    ## C is goal state, reward 100 when B->C or F->C
    ## 
    ## _______
    ## |A|B|C|
    ## |_____|
    ## |D|E|F|
    ## |_____|
    ##
    stateA = 0
    stateB = 1
    stateC = 2
    stateD = 3
    stateE = 4
    stateF = 5

    statesCount = 6
    states = [stateA,stateB,stateC,stateD,stateE,stateF]
 
    ## http://en.wikipedia.org/wiki/Q-learning
    ## http://people.revoledu.com/kardi/tutorial/ReinforcementLearning/Q-Learning.html
 
    ## Q(s,a)= Q(s,a) + alpha * (R(s,a) + gamma * Max(next state, all actions) - Q(s,a))
 
    ## int[][] R = new int[statesCount][statesCount]; ## reward lookup
    ## double[][] Q = new double[statesCount][statesCount]; ## Q learning
    R = []
    Q = []
    
    ## Just going to initialize all these values?
    for x in range(statesCount):
        l = []
        for y in range(statesCount):
            l.append(0)
        R.append(l)
        Q.append(l)
    
 
    actionsFromA = [ stateB, stateD ]
    actionsFromB = [ stateA, stateC, stateE ]
    actionsFromC = [ stateC ]
    actionsFromD = [ stateA, stateE ]
    actionsFromE = [ stateB, stateD, stateF ]
    actionsFromF = [ stateC, stateE ]
    actions = [ actionsFromA, actionsFromB, actionsFromC,
                actionsFromD, actionsFromE, actionsFromF ]
 
    stateNames = [ "A", "B", "C", "D", "E", "F" ]
    
    def __init__(self):
        self.R[self.stateB][self.stateC] = 100
        self.R[self.stateF][self.stateC] = 100


    def run(self):
##        1. Set parameter , and environment reward matrix R 
##        2. Initialize matrix Q as zero matrix 
##        3. For each episode: Select random initial state
##            Do while not reach goal state o
##                Select one among all possible actions for the current state o 
##                Using this possible action, consider to go to the next state o 
##                Get maximum Q value of this next state based on all possible actions o 
##                Compute o Set the next state as the current state
        pass
        

    def policy(self, state):
        actionsFromState = actions[state]
        maxValue = int.MIN_VALUE
        

    def Q(self, s, a):
        return Q[s][a]

    def setQ(self, s, a, val):
        Q[s][a] = val

    def R(self, s, a):
        return self.R[s,a]

    def printResult(self):
        print "Print result" 
        for i in range(len(Q[i])):
            print "out from " + stateNames[i] + ":  "
            for j in range(len(Q[i])):
                print df.format(Q[i][j]) + " "
            print

    def showPolicy(self):
        print "\nshowPolicy"
        for i in range(len(states)):
            from_ = states[i]
            to_ = policy(from_)
            print "from "+stateNames[from_]+" goto "+stateNames[to_]

   
