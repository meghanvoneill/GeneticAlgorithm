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
        if(nextChromosome['evaluation'] == target):
            targetFound = True
        # Otherwise, add the chromosome to the starting population.
        #else:
         #   instanceOfGeneticAlgorithm['']

def evaluate(chromosome, target):

    # Define the variables needed to calculate the evaluation of the chromosome.
    chromosomeName = chromosome['name']
    chromosomeGenes = []
    chromosomeUsableGenes = []
    evaluation = .0
    operatorNext = False
    nextOperator = ''
    nextValue = 0

    # Parse the chromosome 4 bits at a time into genes.
    for i in range(0, len(chromosomeName) - 4, 4):

        newGene = ''

        # Decode the bits for a gene and add the gene to the list of genes.
        for j in range(4):
            newGene += str(chromosomeName[i + j])

        chromosomeGenes.append(newGene)

    # Evaluate the genes to determine the chromosome's collective evaluation.
    for i in chromosomeGenes:

        # Decode the genes into their usable equivalent mathematical values. The pattern followed will
        # be: number -> operator -> number -> operator -> ... -> number.

        # If the next value we need is a number, determine which number, if any, the gene decodes to.
        if nextOperator == False:
            if i == '0000':
                chromosomeUsableGenes.append(0)
                nextOperator = True
                continue
            elif i == '0001':
                chromosomeUsableGenes.append(1)
                nextOperator = True
                continue
            elif i == '0010':
                chromosomeUsableGenes.append(2)
                nextOperator = True
                continue
            elif i == '0011':
                chromosomeUsableGenes.append(3)
                nextOperator = True
                continue
            elif i == '0100':
                chromosomeUsableGenes.append(4)
                nextOperator = True
                continue
            elif i == '0101':
                chromosomeUsableGenes.append(5)
                nextOperator = True
                continue
            elif i == '0110':
                chromosomeUsableGenes.append(6)
                nextOperator = True
                continue
            elif i == '0111':
                chromosomeUsableGenes.append(7)
                nextOperator = True
                continue
            elif i == '1000':
                chromosomeUsableGenes.append(8)
                nextOperator = True
                continue
            elif i == '1001':
                chromosomeUsableGenes.append(9)
                nextOperator = True
                continue
            elif i == '1010':
                continue
            elif i == '1011':
                continue
            elif i == '1100':
                continue
            elif i == '1101':
                continue
            elif i == '1110':
                continue
            elif i == '1111':
                continue
        # Otherwise, the next value we need is an operator. so determine which operator, if any, the gene decodes to.
        else:
            if i == '0000':
                continue
            elif i == '0001':
                continue
            elif i == '0010':
                continue
            elif i == '0011':
                continue
            elif i == '0100':
                continue
            elif i == '0101':
                continue
            elif i == '0110':
                continue
            elif i == '0111':
                continue
            elif i == '1000':
                continue
            elif i == '1001':
                continue
            elif i == '1010':
                chromosomeUsableGenes.append('+')
                nextOperator = False
                continue
            elif i == '1011':
                chromosomeUsableGenes.append('-')
                nextOperator = False
                continue
            elif i == '1100':
                chromosomeUsableGenes.append('*')
                nextOperator = False
                continue
            elif i == '1101':
                chromosomeUsableGenes.append('/')
                nextOperator = False
                continue
            elif i == '1110':
                continue
            elif i == '1111':
                continue

    # Determine the evaluated total of the usable genes.
    #for i in chromosomeUsableGenes:


    chromosome['evaluation'] = float(evaluation)

# This allows a python file to be used as an executable (main will run) or as a library (main will not).
if __name__ == "__main__":
    main()