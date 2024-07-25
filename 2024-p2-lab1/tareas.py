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
        self.pendientes = 0 #se crea un atributo contador inicializado en 0 que usaremos para contar tareas pendientes
        self.tamano = 0 #se crea un atributo contador de tamaño que usaremos para ir contando las tareas que se van agregando  


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

        self.pendientes +=1 #se incrementa pendientes en 1 cada vez que se agrega una tarea
        self.tamano += 1 #se incrementa en 1 tamano para ir contando las tareas que se van agregando

        print("Tarea agregada con éxito.") #muestra un mensaje al usuario de que la tarea se agrego exitosamente


    #este método se crea para buscar una tarea por coincidencia con la descripción de la misma tarea con la descripción solicitada
    def buscar_tarea_descripcion(self,texto)->bool: #se define nombre del método con el parámetro a buscar en la descripción de cada tarea 
        tarea_actual = self.cabeza #se inicializa la variable que va a recorrer la lista a la cabeza
        encontrada = False #se crea una variable inicializada en False que sera la que va a retornar si se encontro o  no la tarea con esa descripción
        while tarea_actual is not None: #se condiciona el recorrido de la variable en la lista. Mientras sea dfirente a None ingresa al ciclo
            if tarea_actual.tarea.descripcion == texto: #si la descripción de la tarea que tiene la variable tarea_actual es igual al texto ingresado por parámetro
                encontrada = True #si lo anterior es cierto, la variable encontrada cambia a True
                break #si encontrada cambia a True entonces el ciclo while se rompe y retorna un valor booleano
            else: #si la descripción de la tarea no coincide con el parámetro ingresa por el else
                tarea_actual = tarea_actual.siguiente #actualiza el nodo al siguiente
        return encontrada #retorna el valor de encontrada 
             

    #este método busca una tarea por id ingresado como parámetro, cambia el valor de completada a True, actualiza el atributo de pendientes y retorna True. En defecto actualiza el nodo al siguiente 
    def completar_tarea(self, id): #define el nombre de método y el valor del parámetro para realizar la búsqueda
        actual = self.cabeza #crea una variable para inicializar el recorrido en cabeza
        while actual != None: #crea un ciclo condicional mientras el nodo sea distinto a None
            if actual.tarea.id == id: #crea el condicional si el id de la tarea del nodo actual es igual al id ingresado por parámetro 
                actual.tarea.completada = True #se cambia el valor del nodo actual en el atributo completada a True 
                self.pendientes -= 1 #se actualiza en valor del atributo pendientes
                return True #retorna True si ingreso por la validación del If como True
            else: #sino ingresa al if, salta de la línea 69 a la 73 e ingresa a ejecutar el else
                actual = actual.siguiente #actualiza el nodo al siguiente
        

    #elimina tarea por id   
    def eliminar_tarea(self, id): #elimina la tarea por Id
        actual = self.cabeza #crea la variable que inicie en el primer elemento
        previo = None #crea variable con valor none
        while actual is not None: #crea un bucle para recorrer la lista 
            if actual.tarea.id == id: #pregunta si el id de la tarea de actual es igual a id pasado por parametro
                if previo is None: #si lo anterior es cierto, vuelve a preguntar si la variable previo es none
                    if actual.tarea.completada == False: #si la tarea a eliminar estaba pendiente
                        self.pendiente -= 1 #resta 1 al atributo 
                        self.tamano -= 1
                    self.cabeza = actual.siguiente #actualiza la cabeza a su valor siguiente
                else: #si previo no es none 
                    previo.siguiente = actual.siguiente #el siguiente del previo pasa a ser el siguiente del actual y el nodo actual se pierde
                    if actual.tarea.completada == False: ##si la tarea a eliminar estaba pendiente
                        self.pendiente -= 1 #resta 1 al atributo 
                        self.tamano -= 1
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


    #muestra por pantalla las tareas que no estan completadas con la totalidad de sus atributos
    def mostrar_tareas_pendientes(self): #define el nombre del método sin parámetros
        tarea_actual = self.cabeza #crea la variable y la inicializa en la cabeza de la lista
        while tarea_actual is not None: #crea un ciclo condicional para ejecutar mientras tarea actual sea distinto de None
            if tarea_actual.tarea.completada is False: #si el atributo completada de la tarea del nodo actual es False
                print(tarea_actual.tarea) #muestra por pantalla la tarea con sus atributos
            tarea_actual = tarea_actual.siguiente #actualiza el nodo al siguiente
        

    #muestra por pantalla las tareas que se que tienen el valor ingresado en un parámetro
    def mostrar_tareas_descripcion(self,text)->None: #define el nombre de la función y que se ingrese un parámetro
        tarea_actual = self.cabeza #crea la variable inicializada en la cabeza de la lista
        while tarea_actual is not None: #crea un ciclo condicional para ejecutar mientras tarea actual sea distinto de None
            if tarea_actual.tarea.descripcion == text: #crea un condicional a ejecutarse si el atributo en la descripción de la tarea actual es igual al parámetro ingresado
                print(tarea_actual.tarea) #si lo anterior es cierto, muestra por pantalla los valores de los atributos de la tarea actual
            tarea_actual = tarea_actual.siguiente #actualiza al siguiente nodo 



    # Funciones estadisticas:
    #este método devuelve la cantidad de tareas que están pendientes de orden lineal
    def contar_tareas_pendientes(self)->int: #define el nombre del método sin parámetros a ingresar 
        tarea_actual = self.cabeza #crea una variable que inicializa a la cabeza de la lista 
        pendiente = 0 #crea una variable que servirá de contador
        while tarea_actual is not None: #crea un ciclo condicional para ejecutar mientras tarea actual sea distinto de None
            if tarea_actual.tarea.completada is False: #si el atributo completada de la tarea del nodo actual es False
                pendiente += 1 #si lo anterior es cierto incrementa la variable pendientes en 1
            tarea_actual = tarea_actual.siguiente #sale del if y actualiza el nodo de la tarea actual al siguiente
        return pendiente #retorna el valor de pendiente


    #este método devuelve la cantidad de tareas que están pendientes de orden constante
    def contar_tareas_pendientes_cte(self)->int: #define el nombre del método sin parámetros
        return self.pendientes #retorna el valor de self.pendientes de la lista 


    #este método muestra por pantalla un cálculo estadístico que muestra la cantidad de tareas completas en relación al total de tareas
    def mostrar_estadisticas(self)->None: #define el nombre del método sin parámetros
        print("Completaste " + str(self.tamano - self.pendientes) + "tareas de " + str(self.tamano)) #muestra por pantalla el mensaje del cálculo del porcentaje


        
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


    #Agrega una tarea a la lista insertándola según la prioridad
    def agregar_tarea_existente(self, tarea): #define el nombre del método y recibe un parámetro
        nuevo_nodo = Nodo(tarea) #crea un nuevo nodo con el valor parámetro ingresado
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: #crea un condicional if donde si la lista esta vacia o si la prioridad del nuevo nodo es mayor a la prioridad de la cabeza ingresa al if
            nuevo_nodo.siguiente = self.cabeza #cambia el siguiente del nuevo nodo , la cabeza  
            self.cabeza = nuevo_nodo #define como cabeza al nuevo nodo que se creó con el valor del parámetro
        else: #si no se cumple el if, se ejecuta el else
            actual = self.cabeza #define en la variable acual la cabeza de la lista
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: #crea un bucle condicional mientras el siguiente al actual no sea None y mientras la prioridad del nodo actual sea mayor a la prioridad de la tarea que se ingresa por parámetro
                actual = actual.siguiente #el actual sera el siguiente nodo
            nuevo_nodo.siguiente = actual.siguiente #si el ciclo while finaliza, entonces el siguinte al nuevo nodo es el actual
            actual.siguiente = nuevo_nodo #el siguiente del actuales el nuevo nodo
        if tarea.id >= self.id_actual: #una vez que la tarea completa el primer condicional if, ejecuta éste segundo if comparando si el id de la tarea ingresada por parámetro es mayor que el id de la actual tarea 
            self.id_actual = tarea.id + 1 #actualiza el id del nodo actual incrementandolo en 1 

#define un procedimiento que muestre en pantalla las opciones posibles
def menu(): #define el procedimiento menu, sin parámetros
    print("\nMenú:") #muestra en pantalla ésta y las lineas siguientes líneas hasta finalizar el procedimiento para especificar al usuario las opciones posibles a elegir enumerandolas del 1 al 8
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Mostrar tareas pendientes")
    print("6. Guardar tareas en archivo CSV")
    print("7. Cargar tareas desde archivo CSV")
    print("8. Salir")


#Crea un procedimiento sin parámetros formado por una lista de tareas de clase lista enlazada donde con un bucle y según la opción ingresada por el ususario, ejecuta los métodos de la lista enlazada
def main(): #llama al procedimiento main
    lista_tareas = ListaEnlazada() #crea la variable lista_tareas que contiene un objeto de clase Lista_Enlazada
    archivo_csv = 'tareas.csv'

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv)

    while True: #crea bucle condicional, mientras sea True
        menu() #llama al procedeimiento menu
        opcion = input("Seleccione una opción: ") #crea una variable que guarda un valor solicitado al usuario
        if opcion == "1": #con el condicional if, si es verdad que el valor guardado en opcion es 1
            descripcion = input("Ingrese la descripción de la tarea: ") #crea una variable que guarda el valor que ingresa el usuario
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): ")) #crea una variable que guarda el valor que ingresa el usuario
            categoria = input("Ingrese la categoría de la tarea: ") #crea una variable que guarda el valor que ingresa el usuario
            lista_tareas.agregar_tarea(descripcion, prioridad, categoria) #ejecuta el método agregar_tarea de la lista enlazada 
        elif opcion == "2": #con el condicional if, si es verdad que el valor guardado en opcion es 2
            id_tarea = int(input("Ingrese el ID de la tarea a completar: ")) #crea una variable que guarda el valor que ingresa el usuario
            if lista_tareas.completar_tarea(id_tarea): #mediante el condicional if si el método completar_tarea (usando el parámetro de id que ingreso el usuario) es True
                print ("Tarea Completada") #muestra en pantalla "Tarea Completada"
            else: #si el método completar_tarea no es True y termna de recorrer la lista, significa que el id buscado no exste en la lista 
                print ("Tarea no encontrada") #muestra en pantalla Tarea no encontrada
        elif opcion == "3":  #con el condicional if, si es verdad que el valor guardado en opcion es 3
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: ")) #crea una variable que guarda el valor que ingresa el usuario
            lista_tareas.eliminar_tarea(id_tarea) #en la lista de tareas ejecuta el método eliminar tarea con parámetrp el id que ingreso el ususario
        elif opcion == "4": #con el condicional if, si es verdad que el valor guardado en opcion es 4
            lista_tareas.mostrar_tareas() #ejecuta el método mostrar tareas en la lista enlazada
        elif opcion == "5":  #con el condicional if, si es verdad que el valor guardado en opcion es 5
            lista_tareas.mostrar_tareas_pendientes() #ejecuta el método mostrar pendientes en la lista enlazada
        elif opcion == "6":  #con el condicional if, si es verdad que el valor guardado en opcion es 6
            lista_tareas.guardar_en_csv(archivo_csv) 
        elif opcion == "7":  
            lista_tareas.cargar_desde_csv(archivo_csv) 
        elif opcion == "8":  #con el condicional if, si es verdad que el valor guardado en opcion es 8
            print("Saliendo del sistema de gestión de tareas.") #avisa al usuario por pantalla "saliendo del sistema de gestion de tareas"
            break #rompe el ciclo while
        else: #si el valor ingresado por el usuario no entro en ninguna opcion anterior, se ejecuta el else
            print("Opción no válida. Por favor, seleccione una opción válida.") #muestra por pantalla al usuario "Opción no válida. Por favor, seleccione una opción válida."

if __name__ == "__main__":
    main()
