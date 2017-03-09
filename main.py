import time, QLearning, Map

def main():

    map1 = Map.Map(1)
    map1.printMap()

    map2 = Map.Map(2)
    map2.printMap()

    map3 = Map.Map(3)
    map3.printMap()
    
    #BEGIN = sys.currentTimeMillis();
    BEGIN = time.time()
 
##    obj = QLearning.QLearning()
##    obj.run(100);
##    obj.printResult();
##    obj.showPolicy();

    #END = System.currentTimeMillis();
    END = time.time()
    
    print "Time: " + str( END - BEGIN ) + " sec."

main()
