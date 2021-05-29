import math
import random
from tqdm import tqdm
from matplotlib import pyplot as plt

points = [('A', [76, 203]), ('B', [165, 75]), ('C', [366, 159]), ('D', [342, 307]),

          ('E', [201, 402]), ('F', [353, 97]), ('G', [489, 310]), ('H', [390, 380]),

          ('I', [501, 302]), ('J', [389, 510]), ('K', [509, 350]), ('L', [410, 160]),

          ('M', [380, 110])]


def draw_road(individual):
    x = []
    y = []
    for p in individual:
        x.append(map_dict[p][0])
        y.append(map_dict[p][1])
        plt.text(x=map_dict[p][0], y=map_dict[p][1], s=p)

    plt.plot(x, y)
    plt.show()


map_dict = dict(points)
travel_dict = dict(points[1:])
root_city = points[0]
dist_memory = {}


def initialize_population(size=100):
    population = []
    for _ in range(size):
        individual = list(travel_dict.keys())
        random.shuffle(individual)
        individual.append('A')
        individual.insert(0, 'A')
        population.append(individual)
    return population


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def calc_cost(individual):
    individual_tuple = tuple(individual)
    if individual_tuple not in dist_memory:
        cost = 0
        for idx in range(len(individual) - 1):
            cost += distance(a=map_dict[individual[idx]], b=map_dict[individual[idx + 1]])
        dist_memory[individual_tuple] = cost
    else:
        cost = dist_memory[individual_tuple]
    return cost


def selection(population):
    costs = []
    for individual in population:
        costs.append(calc_cost(individual=individual))

    max_costs = max(costs)
    weights = [max_costs - c for c in costs]

    sum_weights = sum(weights)
    weights = [w / sum_weights for w in weights]
    selected = random.choices(population=population, weights=weights, k=1)[0]
    return selected


def crossover(parent1, parent2):
    idx1 = random.randint(1, len(parent1) - 3)
    idx2 = random.randint(idx1 + 1, len(parent2) - 2)

    child = ['x'] * len(parent1)
    child[0] = root_city[0]
    child[-1] = root_city[0]

    child[idx1:idx2] = parent1[idx1:idx2]
    for idx in range(len(child)):
        if child[idx] == 'x':
            for p2 in parent2[1: -1]:
                if p2 not in child:
                    child[idx] = p2
                    break
    return child


def mutation(individual):
    p1 = random.randint(1, len(individual) - 2)
    p2 = random.randint(1, len(individual) - 2)

    mutant = individual.copy()
    temp = mutant[p1]
    mutant[p1] = mutant[p2]
    mutant[p2] = temp
    return mutant


def ga(size=100, epochs=100, mutation_threshold=0.5, crossover_threshold=0.5):
    population = initialize_population(size=size)
    global_best = {'individual': None, 'cost': 10e10}
    for e in tqdm(range(epochs)):
        individual_selected = selection(population=population)
        if calc_cost(individual_selected) <= global_best['cost']:
            global_best['cost'] = calc_cost(individual_selected)
            global_best['individual'] = individual_selected

        new_population = []
        for _ in range(size):
            parent1 = selection(population=population)
            parent2 = selection(population=population)

            if random.random() < crossover_threshold:
                child = crossover(parent1=parent1, parent2=parent2)
            else:
                child = random.choice([parent1, parent2])
            if random.random() < mutation_threshold:
                child = mutation(individual=child)

            new_population.append(child)
        population = new_population

    return global_best


if __name__ == '__main__':
    best_individual = ga(size=100, epochs=100)
    print(f'đường đi ngắn nhất có thể chọn là : {best_individual}')
    draw_road(best_individual['individual'])
