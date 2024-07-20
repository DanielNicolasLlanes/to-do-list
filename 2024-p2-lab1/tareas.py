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
        self.pendientes = 0


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
            nuevo_nodo.siguiente = actual.siguiente #el siguiente del nuevo nodo pasa a ser el siguiente del nodo actual
            actual.siguiente = nuevo_nodo #el siguiente nodo del actual pasa a ser el nuevo nodo

        self.pendientes +=1
        print("Tarea agregada con éxito.") #muestra un mensaje al usuario de que la tarea se agrego exitosamente

    def buscar_tarea_descripcion(self,texto)->bool: #crea el método buscar
        pass

    def completar_tarea(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.tarea.id == id:
                actual.tarea.completada = True
                self.pendientes -= 1
                return True
            else:
                actual = actual.siguiente
        

    #elimina tarea por id   
    def eliminar_tarea(self, id): #elimina la tarea por Id
        actual = self.cabeza #crea la variable que inicie en el primer elemento
        previo = None #crea variable con valor none
        while actual is not None: #crea un bucle para recorrer la lista 
            if actual.tarea.id == id: #pregunta si el id de la tarea de actual es igual a id pasado por parametro
                if previo is None: #si lo anterior es cierto, vuelve a preguntar si la variable previo es none
                    if actual.tarea.completada == False: #si la tarea a eliminar estaba pendiente
                        self.pendiente -= 1 #resta 1 al atributo 
                    self.cabeza = actual.siguiente #actualiza la cabeza a su valor siguiente
                else: #si previo no es none 
                    previo.siguiente = actual.siguiente #el siguiente del previo pasa a ser el siguiente del actual y el nodo actual se pierde
                    if actual.tarea.completada == False: ##si la tarea a eliminar estaba pendiente
                        self.pendiente -= 1 #resta 1 al atributo 
                print(f"Tarea eliminada: {actual.tarea.descripcion}") #imprime en pantalla que la tarea se eliminó y muestra la descripcion de la tarea
                return #corta la función en ese instante
            previo = actual #si el id de la tarea actual no coincide con el ingresado por parametro, previo vale el nodo actual
            actual = actual.siguiente #actual pasa a valer el siguiente nodo
        print(f"Tarea con ID {id} no encontrada.") #si el id no coincidio con ninguna tarea, muestra un mensaje de que la tarea no fue encontrada


    #muestra todas las tareas
    def mostrar_tareas(self): #se define método mostrar tareas sin parámetros
        actual = self.cabeza #crea una variable actual asignando el nodo cabeza
        while actual is not None: #crea un bucle que se ejecuta mientras actual no sea none
            estado = "Completada" if actual.tarea.completada else "Pendiente" #muestra "completada" o "pendiente" según el atributo completada
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}") #imprime la tarea con todos sus atributos
            actual = actual.siguiente #actualiza la variable con el siguiente nodo


    def mostrar_tareas_pendientes(self):
        pass
        

    def mostrar_tareas_descripcion(self,text)->None:
        pass


    # F unciones estadisticas:
    def contar_tareas_pendientes(self)->int:
        pass


    def contar_tareas_pendientes_cte(self)->int:
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
            if lista_tareas.completar_tarea(id_tarea):
                print ("Tarea Completada")
            else:
                print ("Tarea no encontrada")
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
