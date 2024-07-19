import csv #importa modulo csv para trabajar con el archivo tareas.csv en este código
import os ##importa modulo os para trabajar con el sistema operativo en este código

class Tarea: #crea una clase Tarea con los siguientes atributos
    def __init__(self, id, descripcion, prioridad, categoria="General"): #se le pasan los parámetros al constructor ()
        self.id = id #este atributo sirve para identificar cada Tarea 
        self.descripcion = descripcion #este atributo sirve para describir que se hace en cada tarea
        self.prioridad = prioridad #sirve para darle un grado de importancia a cada tarea de mayor a menor
        self.completada = False #cada objeto tendra un atributo "completada = False" que no se ingresará como parámetro
        self.categoria = categoria #atributo que si el usuario no ingresa ningun valor, se asigna por defecto como "General" 

class Nodo: #se crea la clase nodo que se usa para las listas enlazadas definidas por:
    def __init__(self, tarea): #se pasa por parámetro un objeto de la clase tarea
        self.tarea = tarea #este atributo sirve para asignarse el objeto tarea que se ingresó como parámetro
        self.siguiente = None #se asigna a cada nodo creado para enlazar el siguiente. Apuntará a None en el caso de que no haya mas nodos

class ListaEnlazada: #se crea la clase ListaEnlazada que contendrá objetos tipo Nodo
    def __init__(self): #se inicializa la clase sin pasar nada como parámetro
        self.cabeza = None #se inicia el atributo en la cabeza de la lista como None ya que en un principio la lista esta vacia (sin nodos)
        self.id_actual = 1 #se crea un contador para identificar cada nodo que luego será asignado como identificador de cada tarea

    #este método devuelve un booleano que nos dirá si la lista esta vacía 
    def esta_vacia(self): #se define el método sin parámetros que ingresar
        return self.cabeza is None #devuelve un valor booleano True si la condición es cierta

    #este método se crea para agregar una tarea en la lista, envuelve la tarea en un nodo, le asigna un valor unico de Id y por último la ordena por prioridad 
    def agregar_tarea(self, descripcion, prioridad, categoria): #define el método con los parámetros descripción, prioridad y categoria
        tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) #crea un objeto de clase Tarea y le asigna como ID el valor definido en self.id_actual y los demás valores pasados como parámetro
        nuevo_nodo = Nodo(tarea) #envuelve el objeto tarea creado dentro de un nodo y lo asigna a una variable  
        self.id_actual += 1 #incrementa el id en uno para la siguiente tarea
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: #usa el condicional para preguntar si la lista esta vacia o si la prioridad de la nueva tarea es mayor a la prioridad del primer elemento de la lista  
            nuevo_nodo.siguiente = self.cabeza #si la condición se cumple, el nuevo nodo en el valor de siguiente apunta a la cabeza de la lista (cabeza queda siguiente al nuevo nodo)
            self.cabeza = nuevo_nodo #cabeza pasa a ser el nuevo nodo
        else: #si no se cumplió la condición en el if, se recorre la lista para encontrar el lugar de la prioridad de la tarea
            actual = self.cabeza #self.cabeza es el actual nodo que se tomará para recorrer la lista 
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: #mientras el nodo siguiente al actual no sea none y mientras la prioridad del siguiente al actual sea mayor o igual a la prioridad de la nueva tarea que queremos agregar
                actual = actual.siguiente #actual pasa a valer el siguiente nodo de la lista
            #cuando salga del bucle del while agrega el elemento a la lista    
            nuevo_nodo.siguiente = actual.siguiente #el siguiente del nuevo nodo es el siguiente del nodo actual
            actual.siguiente = nuevo_nodo #el siguiente del nodo actual es el nuevo nodo

        print("Tarea agregada con éxito.")

    def buscar_tarea_descripcion(self,texto)->true:
        pass

    def completar_tarea(self, id):
        pass

    def eliminar_tarea(self, id):
        actual = self.cabeza
        previo = None
        while actual is not None:
            if actual.tarea.id == id:
                if previo is None:
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                print(f"Tarea eliminada: {actual.tarea.descripcion}")
                return
            previo = actual
            actual = actual.siguiente
        print(f"Tarea con ID {id} no encontrada.")

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual is not None:
            estado = "Completada" if actual.tarea.completada else "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}")
            actual = actual.siguiente

    def mostrar_tareas_pendientes(self):
        pass
        
    def mostrar_tareas_descripcion(self,text)->None:
        pass
    # F unciones estadisticas:
    def contar_tareas_pendientes(self)->int:
        pass
    def mostrar_estadisticas(self)->None:
        pass
        
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado.")
            return
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                id, descripcion, prioridad, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4] == 'True'
                tarea = Tarea(id, descripcion, prioridad, categoria)
                tarea.completada = completada
                self.agregar_tarea_existente(tarea)
            print(f"Tareas cargadas desde {archivo} con éxito.")

    def agregar_tarea_existente(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        if tarea.id >= self.id_actual:
            self.id_actual = tarea.id + 1

def menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Mostrar tareas pendientes")
    print("6. Guardar tareas en archivo CSV")
    print("7. Cargar tareas desde archivo CSV")
    print("8. Salir")

def main():
    lista_tareas = ListaEnlazada()
    archivo_csv = 'tareas.csv'

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): "))
            categoria = input("Ingrese la categoría de la tarea: ")
            lista_tareas.agregar_tarea(descripcion, prioridad, categoria)
        elif opcion == "2":
            id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
            lista_tareas.completar_tarea(id_tarea)
        elif opcion == "3":
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(id_tarea)
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
        elif opcion == "5":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "6":
            lista_tareas.guardar_en_csv(archivo_csv)
        elif opcion == "7":
            lista_tareas.cargar_desde_csv(archivo_csv)
        elif opcion == "8":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
