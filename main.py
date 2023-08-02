
#Создаем граф
graph = {}
#Добавляем узел "start"
graph["start"] = {}
#Добавляем соседние узлы с весами
graph["start"]["a"] = 6
graph["start"]["b"] = 2


#Просмотр веса ребра по двум узлам
print(graph["start"]["a"])
#Просмотр всех соседних узлов
print(graph["start"].keys())
#Просмотр всех соседних узлов и с весами
print(graph["start"].items())


#Добавляем остальные узлы с соседями
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}