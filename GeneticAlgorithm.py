# This genetic algorithm makes use of biological and evolutional mechanisms to find a unique solution to a
# particular problem, carried out on gene- and chromosome-like data structures. The mechanisms mimic biological
# mechanisms such as genetic crossover, genetic mutation, fitness, and some limited population dynamics.
# This idea comes from Mat Buckland of AI-Junkie, who kindly wrote a tutorial on genetic algorithms:
# http://www.ai-junkie.com/ga/intro/gat1.html

import math
import random


def main():
    # Generating a Population:

    # A dictionary used to rep a population of chromosomes (list of binary string chromosomes).
    population = {}

    # A Boolean to track whether the target solution has been found.
    target_found = False

    # Initialize variable for the starting population size and the chromosome length. The length must
    # be divisible by four for the algorithm to work correctly, since encoded genes are each 4 bits long.
    starting_population_size = 10000
    chromosome_size = 80

    # Establish the target value.
    target = 27

    # A variable for tracking the total fitness of the starting population for use in roulette wheel selection later.
    total_fitness = .0

    # A variable to hold the partial summation of fitnesses evaluated for roulette wheel selection.
    partial_sum = .0

    # Variables for roulette wheel selections.
    parent0 = {}
    parent1 = {}

    # Create the starting populations:
    population00 = []
    population01 = []

    for i in range(starting_population_size, 0, -1):

        # Create the next chromosome in the population.
        next_chromosome = {}
        next_chromosome_name = []
        for j in range(chromosome_size):
            random_bit = str(random.getrandbits(1))
            next_chromosome_name.append(random_bit)
        next_chromosome = {'name': next_chromosome_name}

        # Evaluate the chromosome.
        evaluate(next_chromosome, target)

        # Check to see if the chromosome matches the target.
        if next_chromosome['evaluation'] == target:
            print("The chromosome that succeeded: " + str(next_chromosome_name))
            target_found = True

        # Otherwise, find the chromosome's fitness and add the chromosome to the starting population.
        else:
            fitness(next_chromosome, target)
            population00.append(next_chromosome)

            # Add this chromosome's fitness to the total fitness of the starting population for roulette wheel
            # selection later.
            total_fitness += next_chromosome['fitness']

    # Add the starting population to the
    population = {'population00': population00}

    # Create the next population:

    # Select two members of the starting population based on fitness and using roulette wheel selection.
    for i in range(starting_population_size):

        # Generate a random number between 0 and our total fitness as the random point on our roulette wheel to
        # for parent0.
        random.seed()
        random_fitness = random.uniform(0, total_fitness)

        # Add up the fitnesses of each chromosome until the partial sum is greater than the random fitness.
        for i in population00:
            # While the partial sum is less than the random fitness, continue adding up fitnesses.
            if partial_sum < random_fitness:
                partial_sum += i['fitness']
            # Otherwise, the chromosome has been found.
            else:
                parent0 = i
                break

        # Generate a random number between 0 and our total fitness as the random point on our roulette wheel to
        # stop for parent1.
        random_fitness = random.uniform(0, total_fitness)

        # Add up the fitnesses of each chromosome until the partial sum is greater than the random fitness.
        for i in population00:
            # While the partial sum is less than the random fitness, continue adding up fitnesses.
            if partial_sum < random_fitness:
                partial_sum += i['fitness']
            # Otherwise, the chromosome has been found.
            else:
                parent1 = i
                break

        # Crossover bits from each of the chosen chromosomes.
        # Good crossover rate: .7
        crossover_rate = .7

        # Determine whether crossover is occurring.
        crossover_occurring = False
        random_crossover = random.random()
        if random_crossover <= crossover_rate:
            crossover_occurring = True

        # If crossover is occurring, choose a random bit along the length and swap all bits after that point.
        if crossover_occurring:

            random_bit_to_flip_after = random.randint(0, chromosome_size)
            parent0s_new_bits = []
            parent1s_new_bits = []

            # Take parent0's bits after the flip point and save them for parent1.
            # TODO: update with range to eliminate if statement
            for index in parent0['name']:
                if index >= random_bit_to_flip_after:
                    parent1s_new_bits.append(parent0['name'][int(index)])

            # Take parent1's bits after the flip point and save them for parent0.
            # TODO: update with range to eliminate if statement
            for index in parent1['name']:
                if index >= random_bit_to_flip_after:
                    parent0s_new_bits.append(parent1['name'][int(index)])

            # Update values for saved bits for parent0.
            next_key_index = random_bit_to_flip_after
            for val in parent0s_new_bits:
                parent0['name'][next_key_index] = val
                next_key_index += 1

            # Update values for saved bits for parent1.
            next_key_index = random_bit_to_flip_after
            for val in parent1s_new_bits:
                parent1['name'][next_key_index] = val
                next_key_index += 1

        # Step through the chosen chromosomes' bits and flip for mutations.

        # Good mutation rate: .001
        mutation_rate = .001

        mutation_occurring = False
        random_mutation = random.random()
        if random_mutation <= mutation_rate:
            mutation_occurring = True

        # for i in parent0['name']:

        # random.seed()
        # mutationAttempt = random.random()

        # if mutationAttempt ... :
        # if name[i] == 0:
        # name[i] = 1
        # else:
        # name[i] = 0

        # Add the chromosomes to the new population.
        # population01.append(parent0)
        # population01.append(parent1)


def evaluate(chromosome, target):
    # Define the variables needed to calculate the evaluation of the chromosome.
    chromosome_name = chromosome['name']
    chromosome_genes = []
    chromosome_usable_genes = []
    operator_next = False

    # Parse the chromosome 4 bits at a time into genes.
    for i in range(0, len(chromosome_name) - 4, 4):

        new_gene = ''

        # Decode the bits for a gene and add the gene to the list of genes.
        for j in range(4):
            new_gene += str(chromosome_name[i + j])

        chromosome_genes.append(new_gene)

    # Evaluate the genes to determine the chromosome's collective evaluation.
    for i in chromosome_genes:

        # Decode the genes into their usable equivalent mathematical values. The pattern followed will
        # be: number -> operator -> number -> operator -> ... -> number.

        # If the next value we need is a number, determine which number, if any, the gene decodes to.
        if operator_next == False:
            if i == '0000':
                chromosome_usable_genes.append(0)
                operator_next = True
                continue
            elif i == '0001':
                chromosome_usable_genes.append(1)
                operator_next = True
                continue
            elif i == '0010':
                chromosome_usable_genes.append(2)
                operator_next = True
                continue
            elif i == '0011':
                chromosome_usable_genes.append(3)
                operator_next = True
                continue
            elif i == '0100':
                chromosome_usable_genes.append(4)
                operator_next = True
                continue
            elif i == '0101':
                chromosome_usable_genes.append(5)
                operator_next = True
                continue
            elif i == '0110':
                chromosome_usable_genes.append(6)
                operator_next = True
                continue
            elif i == '0111':
                chromosome_usable_genes.append(7)
                operator_next = True
                continue
            elif i == '1000':
                chromosome_usable_genes.append(8)
                operator_next = True
                continue
            elif i == '1001':
                chromosome_usable_genes.append(9)
                operator_next = True
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
                chromosome_usable_genes.append('+')
                operator_next = False
                continue
            elif i == '1011':
                chromosome_usable_genes.append('-')
                operator_next = False
                continue
            elif i == '1100':
                chromosome_usable_genes.append('*')
                operator_next = False
                continue
            elif i == '1101':
                chromosome_usable_genes.append('/')
                operator_next = False
                continue
            elif i == '1110':
                continue
            elif i == '1111':
                continue

    # Determine the evaluated total of the usable genes.

    # Set the evaluation to the first usable gene, a number.
    evaluation = float(chromosome_usable_genes[0])

    # Since the usable genes follow the number -> operator -> number pattern, if the index is odd,
    # the value is an operator (string).
    for i in range(1, len(chromosome_usable_genes) - 1, 2):

        # Store the next operator and the next value.
        next_operator = chromosome_usable_genes[i]
        next_value = chromosome_usable_genes[(i + 1)]

        # Based on the operator, perform the corresponding calculation.
        if next_operator == '+':
            evaluation = evaluation + next_value
        if next_operator == '-':
            evaluation = evaluation - next_value
        if next_operator == '*':
            evaluation = evaluation * next_value
        if next_operator == '/':
            # Ensure no division by zero.
            if next_value != 0:
                evaluation = evaluation / next_value
            # Otherwise the loop advances to the next operator to see if there is a viable pairing to evaluate.

    # Store the final evaluation as a float back in the chromosome's dictionary.
    chromosome['evaluation'] = float(evaluation)


def fitness(chromosome, target):
    evaluation = chromosome['evaluation']

    # If the target and the evaluation are the same, a successful solution has been found.
    if target - evaluation == 0:
        return chromosome

    # Otherwise, calculate the chromosome's fitness and store it back in the chromosome's dictionary.
    found_fitness = 1 / (target - evaluation)
    chromosome['fitness'] = float(found_fitness)


# This allows a python file to be used as an executable (main will run) or as a library (main will not).
if __name__ == "__main__":
    main()
