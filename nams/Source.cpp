#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "nams.h"
#include "hungarian.h"



/* 
very briefly, this how it should be done 
1. compute all the atom matrices for the base molecule all the ones in the filtered database and save them
2. for a given number of iterations do:
	2a. compute a random number of weights (from 0 to 2?) for each atom of the base mol - the are the atom exponents
	2b. apply the values as exponents to the self similarity matrices and the atom matrices
	2c. compute the J result for each
	2d. write down a line with a column for each molecule with the new similarity results
	2e. write down the atom exponents values in another file


*/

