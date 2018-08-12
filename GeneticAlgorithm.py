# This genetic algorithm makes use of biological and evolutional mechanisms to find a unique solution to a
# particular problem, carried out on gene- and chromosome-like data structures. The mechanisms mimic biological
# mechanisms such as genetic crossover, genetic mutation, fitness, and some limited population dynamics.
# This idea comes from Mat Buckland of AI-Junkie, who kindly wrote a tutorial on genetic algorithms.

import math
import random

def main():

    # Generating a Population:
    # Initialization for the random number generator used to create our starting population bit strings.
    random.seed()

    # A list used to rep a chromosome (list of binary string genes).


    # A dictionary used to rep a population of chromosomes (list of binary string chromosomes).


    # Initialize variable for the starting population size and the chromosome length. The length must
    # be divisible by four for the algorithm to work correctly, since encoded genes are each 4 bits long.
    startingPopulationSize = 10000
    chromosomeSize = 80

    for i in range(startingPopulationSize, 0, -1):
        nextChromosome = ''
        for j in range(chromosomeSize):
            randomBit = str(random.getrandbits(1))
            nextChromosome += randomBit


# This allows a python file to be used as an executable (main will run) or as a library (main will not).
if __name__ == "__main__":
    main()