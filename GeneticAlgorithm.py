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

    # Create the starting population:
    population00 = []

    while targetFound == False:
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
                print("The chromosome that succeeded: " + str(nextChromosomeName))
                targetFound = True
            # Otherwise, add the chromosome to the starting population.
            else:
                population00.append(nextChromosome)

     # Add the starting population to the
    instanceOfGeneticAlgorithm = {'population00': population00}

    # Create the next population:

        # Select two members of the starting population based on fitness and using roulette wheel selection.

        # Crossover bits from each of the chosen chromosomes.

            # Good crossover rate: .7

        # Step through the chosen chromosomes' bits and flip for mutations.

            # Good mutation rate: .001



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
        if operatorNext == False:
            if i == '0000':
                chromosomeUsableGenes.append(0)
                operatorNext = True
                continue
            elif i == '0001':
                chromosomeUsableGenes.append(1)
                operatorNext = True
                continue
            elif i == '0010':
                chromosomeUsableGenes.append(2)
                operatorNext = True
                continue
            elif i == '0011':
                chromosomeUsableGenes.append(3)
                operatorNext = True
                continue
            elif i == '0100':
                chromosomeUsableGenes.append(4)
                operatorNext = True
                continue
            elif i == '0101':
                chromosomeUsableGenes.append(5)
                operatorNext = True
                continue
            elif i == '0110':
                chromosomeUsableGenes.append(6)
                operatorNext = True
                continue
            elif i == '0111':
                chromosomeUsableGenes.append(7)
                operatorNext = True
                continue
            elif i == '1000':
                chromosomeUsableGenes.append(8)
                operatorNext = True
                continue
            elif i == '1001':
                chromosomeUsableGenes.append(9)
                operatorNext = True
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
                operatorNext = False
                continue
            elif i == '1011':
                chromosomeUsableGenes.append('-')
                operatorNext = False
                continue
            elif i == '1100':
                chromosomeUsableGenes.append('*')
                operatorNext = False
                continue
            elif i == '1101':
                chromosomeUsableGenes.append('/')
                operatorNext = False
                continue
            elif i == '1110':
                continue
            elif i == '1111':
                continue

    # Determine the evaluated total of the usable genes.

    # Set the evaluation to the first usable gene, a number.
    evaluation = float(chromosomeUsableGenes[0])

    # Since the usable genes follow the number -> operator -> number pattern, if the index is odd,
    # the value is an operator (string).
    for i in range(1, len(chromosomeUsableGenes) - 1, 2):

        # Store the next operator and the next value.
        nextOperator = chromosomeUsableGenes[i]
        nextValue = chromosomeUsableGenes[(i + 1)]

        # Based on the operator, perform the corresponding calculation.
        if nextOperator == '+':
            evaluation = evaluation + nextValue
        if nextOperator == '-':
            evaluation = evaluation - nextValue
        if nextOperator == '*':
            evaluation = evaluation * nextValue
        if nextOperator == '/':
            # Ensure no division by zero.
            if nextValue != 0:
                evaluation = evaluation / nextValue
            # Otherwise the loop advances to the next operator to see if there is a viable pairing to evaluate.

    # Store the final evaluation as a float back in the chromosome's dictionary.
    chromosome['evaluation'] = float(evaluation)

def fitness(chromosome, target):

    evaluation = chromosome['evaluation']

    # If the target and the evaluation are the same, a successful solution has been found.
    if target - evaluation == 0:
        return chromosome

    # Otherwise, calculate the chromosome's fitness and store it back in the chromosome's dictionary.
    foundFitness = 1 / (target - evaluation)
    chromosome['fitness'] = float(foundFitness)



# This allows a python file to be used as an executable (main will run) or as a library (main will not).
if __name__ == "__main__":
    main()