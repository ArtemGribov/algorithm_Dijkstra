#181
#Создаем граф
graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

#Просмотр веса ребра по двум узлам
#print(graph["start"]["a"])
#Просмотр всех соседних узлов
#print(graph["start"].keys())
#Просмотр всех соседних узлов и с весами
#print(graph["start"].items())

#Добавляем остальные узлы с соседями
graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

print(graph.keys())
print(graph.values())

#Таблица стоимостей
infinity = float("inf") #бесконечность
costs = {}
costs["a"] = 10
costs["b"] = 30
costs["c"] = infinity
costs["fin"] = infinity

#Таблица родителей
parents = {}
parents["a"] = "start"
parents["a"] = "c"
parents["b"] = "a"
parents["c"] = "a"
parents["c"] = "b"
parents["fin"] = "b"
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
print("Кратчайший путь до fin: ", costs.get("fin"))