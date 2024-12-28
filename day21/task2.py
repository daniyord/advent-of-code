import networkx as nx
from shared import get_complexity

result = 0
file = open('input.txt', 'r')
for line in file:
    result += get_complexity(line.strip(), 25)

print(result)
