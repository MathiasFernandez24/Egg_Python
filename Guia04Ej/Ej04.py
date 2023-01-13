tareas = set()
while True:
    tarea = input("Ingrese tarea: ")
    if (tarea == ""):
        print("PROGRAMA FINALIZADO")
        break
    tareas.add(tarea)

    print("set -> ", tareas)

    array = list(tareas)
    array.sort()
    print("array -> ", array)
