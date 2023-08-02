#175
#Создаем граф
graph = {}
#Добавляем узел "start"
graph["start"] = {}
#Добавляем соседние узлы с весами
graph["start"]["a"] = 6
graph["start"]["b"] = 2

#Просмотр веса ребра по двум узлам
#print(graph["start"]["a"])
#Просмотр всех соседних узлов
#print(graph["start"].keys())
#Просмотр всех соседних узлов и с весами
#print(graph["start"].items())

#Добавляем остальные узлы с соседями
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#Таблица стоимостей
infinity = float("inf") #бесконечность
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#Таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

#Массив для отслеживания всех уже обработанных узлов
processed = []

#Алгоритм Дейкстры
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#Проверка
print(costs)