# For reference see:
# https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
# http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
# http://www.med.mcgill.ca/epidemiology/hanley/tmp/proportion/wilson_jasa_1927.pdf

import sys
import math

# Gather our code in a main() function
def main():
#    print 'Hello there', sys.argv[1]



    five = int(input('How many 5 star ratings?  '))
    four =  int(input('How many 4 star ratings?  '))
    three = int(input('How many 3 star ratings?  '))
    two = int(input('How many 2 star ratings?  '))
    one = int(input('How many 1 star ratings?  '))

    N_k = [one, two, three, four, five]
    S_k = [1,2,3,4,5]

    K = len(S_k)
    N = sum(N_k) #one + two + three + four + five
    z = 1.65


    total = 0
    for i in range(0,5):
        total += S_k[i] * (N_k[i]+1) / (N+K)

    print("base: ", total)

    total_squared = 0
    for i in range(0,5):
        total_squared += S_k[i] ** 2 * (N_k[i]+1) / (N+K)


    credibility = 2 * z *math.sqrt( (total_squared - total ** 2 )/ (N+K+1) )
    print("Credibility: ", credibility)


    print('Adjusted: ', total - credibility)


    print('')
    print('Adjusted/Credibility: ', total - credibility , '/' , credibility)
#        total = total +
#        total += S_k(i) * ()
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
