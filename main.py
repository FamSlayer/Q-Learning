import sys, QLearning



def main():

    #BEGIN = sys.currentTimeMillis();
 
    obj = QLearning.QLearning()

    obj.run();
    obj.printResult();
    obj.showPolicy();

    #END = System.currentTimeMillis();
    print "Time: " + (END - BEGIN) / 1000.0 + " sec."

main()
