#181
#Создаем граф
graph = {}
graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 5

#Просмотр веса ребра по двум узлам
#print(graph["start"]["a"])
#Просмотр всех соседних узлов
#print(graph["start"].keys())
#Просмотр всех соседних узлов и с весами
#print(graph["start"].items())

#Добавляем остальные узлы с соседями
graph["a"] = {}
graph["a"]["b"] = 8
graph["a"]["c"] = 7

graph["b"] = {}
graph["b"]["c"] = 2
graph["b"]["d"] = 4

graph["c"] = {}
graph["c"]["fin"] = 1

graph["d"] = {}
graph["d"]["c"] = 6
graph["d"]["fin"] = 3

graph["fin"] = {}

print(graph.keys())
print(graph.values())

#Таблица стоимостей
infinity = float("inf") #бесконечность
costs = {}
costs["a"] = 2
costs["b"] = 5
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

#Таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["b"] = "a"
parents["c"] = "a"
parents["c"] = "b"
parents["c"] = "d"
parents["d"] = "b"
parents["fin"] = "c"
parents["fin"] = "d"
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