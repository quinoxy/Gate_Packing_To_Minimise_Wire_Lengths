# Gate_Packing_To_Minimise_Wire_Lengths
According to the problem statement:

In order to calculate the wire length for all the connections of the form say (wire g1.p1 gi.pj), we will estimate a minimum fitting bounding box which will consist of the coordinates {g1.p1} union {gi.pj | we have connections of the form (wire g1.p1 gi.pj)}

Then calculate the semi perimeter of the rectangle. It will be wire length for all the connections of the form (wire g1.p1 g2.p1).

Total wire length will be then sum of wire lengths for all k such that we have connections of the form (wire gk.pk gi.pj).

We have created 2 solutions to the problem statement. One is implemented directly if you run the current main file. As for the other, uncomment the line packing,ll,bb=aadi_solution(862) in the main file and comment the lines packing= EnhancedGreedyGatePacking()(863) and packing.greedy_multiple()(866) and run the file. In case you want a visual representation of how the graphs are placed, uncomment the packing.draw()(869) line.
After running, the file outputs the total wire length calculated for the iteration.

For testing, input into the input file gates in the format given in the Problem Statement file.
