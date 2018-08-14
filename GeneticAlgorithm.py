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

    # A dictionary used to rep a population of chromosomes (list of binary string chromosomes).
    instanceOfGeneticAlgorithm = {}

    # A Boolean to track whether the target solution has been found.
    targetFound = False

    # Initialize variable for the starting population size and the chromosome length. The length must
    # be divisible by four for the algorithm to work correctly, since encoded genes are each 4 bits long.
    startingPopulationSize = 10000
    chromosomeSize = 80

    # Establish the target value.
    target = 27

    # Create the starting population using the startingPopulationSize.
    for i in range(startingPopulationSize, 0, -1):

        # Create the next chromosome in the population.
        nextChromosome = {}
        nextChromosomeName = []
        for j in range(chromosomeSize):
            randomBit = str(random.getrandbits(1))
            nextChromosomeName.append(randomBit)
        nextChromosome = {'name': nextChromosomeName}

        # Evaluate the chromosome.
        evaluate(nextChromosome, target)

        # Check to see if the chromosome matches the target.
        if(nextChromosome['evaluate'] == target):
            targetFound = True
        # Otherwise, add the chromosome to the starting population.
        #else:
         #   instanceOfGeneticAlgorithm['']

def evaluate(chromosome, target):

    # Define the variables needed to calculate the evaluation of the chromosome.
    chromosomeName = chromosome['name']
    chromosomeGenes = []
    evalution = 0
    nextOperator = 0
    nextValue = 0

    # Parse the chromosome 4 bits at a time into genes.
    for i in range(0, len(chromosomeName) - 4, 4):

        newGene = ''

        # Decode the bits for a gene and add the gene to the list of genes.
        for j in range(4):
            newGene += str(chromosomeName[i + j])

        chromosomeGenes.append(newGene)

    # Evaluate the genes to determine the chromosome's collective evaluation.
    #for i in chromosomeGenes:

        #value =

        # Decode the genes into their equivalent mathematical values.
        #if i == '0000'



# This allows a python file to be used as an executable (main will run) or as a library (main will not).
if __name__ == "__main__":
    main()