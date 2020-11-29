Implementation of Vogel Approximation Method for transportation problem and Hungarian Algorithm for assignment problem in Python 

Usage  

`bash run.sh`


Description of files :
1. src/Assignment_problem/hungarian.py - implementation of the hungarian algorithm
2. src/Assignment_problem/naive_algo.py - brute force solution of the Assignment problem
3. src/Assignment_problem/ap.py - Comparison of brute force solution and hungarian algorithm solution on a randomnly generated matrix
4. src/Transportation_problem/Vogel_approx_method.py - Implementation of the Vogel Approximation Method
5. src/Transportation_problem/Russel_approx_method.py - Implementation of the Russel Approximation Method
6. src/Transportation_problem/experimental_design.py - Generation of 640 random instances according to the experimental design
7. src/Transportation_problem/comparison.py - Obtaining the results of the 640 instances using all 4 algorithms and evaluating their performance using integrated ranks
8. main.py - Runs the hungarian algorithm on a randomly generated matrix and compares it with the brute force algorithm . Also runs the Vogel Approximation Method and the Russel Approximation method on a randomly generated cost matrix. 
