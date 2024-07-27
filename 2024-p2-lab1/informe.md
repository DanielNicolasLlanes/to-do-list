## Informe del Proyecto: Sistema de Gestión de Tareas Pendientes
1. Introducción

    Breve descripción del proyecto y su importancia.
    Objetivos del proyecto y qué se espera lograr con la implementación del sistema.
    Este proyecto titulado "Sistema de Gestión de Tareas Pendientes" es una propuesta de la cátedra de Programación 2 de la Tecnicatura en Desarrollo de Software del Instituto Técnico Superios Córdoba. El desarrollo del mismo se orienta a desarrollar un sistema que permita a usuarios facilitar la gestión de tareas de manera efectiva. SU funcionamiento se basa tanto en la posibilidad de agregar, eliminar y marcar tareas como completas como en la posibilidad de tener un sistema de prioridades de dichas tareas, realizar búsquedasm organizarlas, etc.
    
    Es importante recalcar que la práctica ayuda a aprehender conocimientos y conceptos trabajados en clase, tales como POO, estructuras de datos (en este caso, focalizando en listas enlazadas), nociones de orden y annálisis de algoritmos, etc. Muchas veces los ejercicios realizados en el transcurso de la mcursada son pequeños recortes que no reflejan del todo la compleja realidad de la profesión. De esta manera comenzamos a entender cómo se aplica en un caso concreto todo lo visto en la materia de manera integral. Es importante destacar que el trabajo en grupo es una práctica que nos prepara para integrar en un futuro algún equipo de trabajo.


Los objetivos específicos del proyecto propuestos por el docente son:

    -Reforzar conceptos de programación orientada a objetos (POO), proporcionando una base sólida para el desarrollo de software complejo y eficiente.
    -Practicar el uso de estructuras de datos lineales, en particular listas enlazadas, lo que nos permitirá como estudiantes entender mejor su implementación y manejo.
    -Desarrollar habilidades en el análisis de algoritmos y notación asintótica, cruciales para evaluar y optimizar la eficiencia del código.
    -Fomentar el trabajo en equipo y la colaboración, como así también la apropiación de buenas prácticas como comentar el código, la documentación, la validación, verificación y testing.


2. Descripción del Sistema

    Funcionalidades Implementadas:
        Lista y descripción de las funcionalidades básicas y avanzadas desarrolladas.
        Funcionalidades Básicas y avanzadas dsarrolladas en el proyecto: 

        -   esta_vacia: pregunta si la cabeza de la lista es igual a None y devuelve un valor booleano que indica si la lista enladaza esta vacía o no.

        -   agregar_tarea: con los 3 valores que pide como parámetros, crea un objeto de clase tarea, y transforma esa tarea en un nodo. Da un id a cada nueva tarea agregada. Va acomodando las tareas en la lista según la prioridad mas alta, mostrando al usuario un msj satisfactorio en caso de haberse agregado de manera efectiva la tarea. En éste mismo método usa dos atributos diferentes que servirán para contar las tareas pendientes y para contar la cantidad de nodos de la lista.

        -   buscar_tarea_descripción: recorre la lista y devuelve un valor booleano al pedir que se ingrese como parámetro un texto que lo compara con la despcrición de la tarea del nodo. Cuando compara el texto (que en ambos casos se trasnforma a letra minúscula) y resulta cierta retorna True. Si esta condición no se cumple en ningún elemento de la lista retorna False.

        -   completar_tarea: recorre la lista, busca tarea por id comparandola con el parámetro. Cuando la comparación es cierta, marca la tarea como completada. Resta 1 a las tareas pendientes y retorna True. Si recorre toda la lista y no coincide ningún id retorna False.

        -   eliminar_tarea: recorre la lista y pide un id para comparar con el id de la tarea actual. Crea dos variables para guardar el elemento actual y el previo. Si el id coincide con el primer elemento de la lista, la cabeza vale el siguiente del actual. En el caso de que no sea el primer elemento el que debe ser eliminado, se le asigna el siguiente del previo al siguiente del actual perdiendo la referencia al nodo actual. Muestra en pantalla la descripción de la tarea eliminada o un mensaje de que la tarea no fue encontrada. Antes de eliminar una tarea pregunta si no estaba completada para descontar en la variable "pendientes" y resta 1 al tamaño.

        -   mostrar_tareas: Recorre la lista y muestra todos los atributos de cada tarea y el estado "pendiente" o "completada" dependiendo de su valor booleano.

        -   mostrar_tareas_pendientes: recorre la lista. Pregunta si la tarea no está completada y en ese caso muestra en pantalla la tarea actual con sus atributos. Usa dos contadores uno para contar los elementos y otro para contar las tareas completadas de manera que pueda comparar dichos valores y si ambos son iguales se muestra en pantalla que no hay tareas pendientes.

        -   mostrar_tareas_descripcion: recorre la lista. Pide un parámetro de texto que si coincide con la descripcion del nodo actual, muestar en pantalla la tarea con sus parámetros

        -   buscar_categoria: recorre la lista en busca de una categoria pasada por parámetro. A cada elemento pregunta si su categoria es igual a la pasada por parámentro en minúscula devolviendo True si la encuentra o False si no existe en la lista.

        -   mostrar_tareas_categoria: al igual que mostrar descripción imprime las tareas que coinciden con la categoria psada por parámetro.

        -   contar_tareas_pendientes: de orden lineal. Recorre la lista, guarda en una variable contadora un valor por cada tarea pendiente de la lista. Al final retorna la cantidad de elementos contados.

        -   contar_tareas_pendientes_cte: de orden cconstante. Simplemente retorna el valor de la variable pendiente de la lista enlazada.Esta variable se va actualizando con los métodos agregar tarea, eliminar tarea y completar tarea.

        -   mostrar_estadisticas: muestra por pantalla un calculo del porcentaje de tareas que figuran completas sobre el total de las tareas de la lista enlazada.

        -   menu: es un procedimiento que muestra en pantalla las opciones posibles a elegir enumerandolas del 1 al 12

        -   main: es una función sin parámetros formado por una lista de tareas de clase lista enlazada donde con un bucle y según la opción ingresada por el ususario, ejecuta los métodos de la lista enlazada. Se crea la variable lista_tareas que contiene un objeto de clase Lista_Enlazada. Con un bucle que se ejecute siempre y cuando no se ingrese la opción 12 para salir del programa. Se ejecuta usando el procedimiento menu(), según la opción ingresada por el usuario en esa variable y ejecuta los métodos definidos de la lista enlazada para correr el programa.
        

    Estructuras de Datos Utilizadas:
        Explicación de la implementación de la lista enlazada y nodos en el sistema.
        El programa usa una estructura de datos de lista enlazada. Para lograr su implementación hacemos uso de las clases Nodo que los elementos que componen a la lista. Cada Nodo guarda un dato y una referencia hacia un siguiente nodo. En ese dato almacenamos objetos de una clase tarea.


3. Metodología y Diseño
    Diseño del Código:
        Descripción concisa de las clases principales (Tarea, Nodo, ListaEnlazada) y su interacción.
        -   clase Tarea: cada objeto de esta clase se crea con el id, descripcion y prioridad ingresadas por el usuario, mientras que el atributo categoria si no es ingresado por el usuario el programa le asigna por defecto el valor "General" y el atributo completada siempre inicializado en False.

        -   clase Nodo: se crea con dos atributos, uno que guardará la tarea en si y otra parte que hará referencia al siguiente nodo. Esta clase creará los nodos que necesita la lista enlazada para operar.

        -   clase ListaEnlazada: crea el atributo de la cabeza de a lista en None, crea un atributo para manejar los id de cada tarea, crea dos atributos mas (pendiente y tamano) uno para manejar las tareas pendientes y otro para saber el tamaño de la lista. Iniciados estos últimos en 0.

        Interacción: Todas las clases definidas en el programa, se comunican entre ellas a través del uso de los métodos creados en la clase Lista Enlzazada. Estos métodos crean objetos de clase Tarea y objetos de clase Nodo los cuales serán unidos gracias a sus referencias y almacenarán los datos de cada tarea.

4. Implementación y Ejemplo
    Detalles de Implementación:
        Explicación breve de cómo se implementaron las funcionalidades principales.
        
"""""""""////////----------

    Casos de Uso y Ejemplos:
        Ejemplos de ejecución del sistema para diferentes escenarios de uso.
        Se puede utilizar para: 
            -   Instituciones privadas y públicas que necesiten llevar un control real sobre obligaciones, actividades, tareas, objetivos, etc que necesiten llevarse a cabo.
            -   También se puede usar para uso personal como agenda diaria en la cual un usuario puede marcar sus actividades y llevar un control sobre ellas. 
            -   Puede ser usada también por profesionales para organizar sus objetivos y / o responsabilidades en su vida diaria.
            -   Tambien podria funcionar como una lista de compras
        Es decir el uso del programa puede ser individual o colectivo dependiendo de la necesidad de los usuarios o de la empresa. Es un programa bastante versátil en cuanto a la solución que brinda en organización de tareas.


5. Preguntas Conceptuales

    Preguntas para Análisis:
        ¿Qué sucede si intentamos agregar una tarea que ya existe en la lista?
        Si intentamos agregar una tarea que ya existe, el programara llamará a la función buscar_tarea_descripcion que corroborará con el "descripción" si esa tarea ya existe en la lista, mostrando en pantalla al usuario en caso de ser cierto no permitiendo su agregación a la lista. 

        ¿Cómo se implementa la priorización de tareas en la lista enlazada? 
        La priorización se implementa en el momento en que se agrega una tarea. La Tarea solo se agregará al principio de la lista si la prioridad es mayor a la de la primer tarea, sino se agregará por delante de la tarea que tenga la misma prioridad o menor que ella.

        ¿Qué sucede si dos tareas tienen la misma prioridad?
        Si dos tareas tienen la misma prioridad, la que se intenta agregar se colocará antes de la que ya se encuentra en la lista quedando como una tarea mas reciente.

        ¿Cuál es la complejidad temporal del método para eliminar una tarea de la lista enlazada?
        La complejidad temporal de eliminar tareas es de orden lineal ya que en el peor de los casos, el método deberá recorrer toda la lista pasando por todos los elementos. Podemos deducir esto gracias a la condición "While actual is not None" que nos indica que la variable actual recorre todos los elementos hasta llegar al último en caso de no encontrar la coincidencia con el id.


"""""""""////////----------
        ¿Cómo podríamos modificar el sistema para soportar múltiples categorías por tarea?
        Podemos asignarle al atributo categoria, una lista vacia en la que se guarden las categorias que el usuario quiera ingresar, lo que nos llevaría a modificar el atributo en la clase Tarea y modificar el menú debiendo crear una función que maneje la agregación de las categorias a la lista. 
        
        Ejemplo propuesto para que soporte múltiples categorias:
        Creamos una función para insertar un elemento a una lista que será la lista de categorias.

        def menu_categoria(categoria):
            elemento = input("Ingrese la categoría de la tarea: ")
            categoria.append(elemento)

        if opcion == "1":  
            descripcion = input("Ingrese la descripción de la tarea: ") 
            prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3=alta)))
            categoria = []
            menu_categoria(categoria)
            
            opcion_categoria = 1
            while eleccion != 0:
                print("desea agregar otra categoria?")
                print("Presione 0 para no, 1 para si")
                eleccion = int(input("Ingrese la opcion: "))
                if eleccion == 1:
                    menu_categoria(categoria)



6. Resultados y Conclusiones

    Resultados Obtenidos:
        Evaluación del éxito en la implementación de las funcionalidades.
    Conclusiones:
        Resumen de los hallazgos y reflexiones sobre lecciones aprendidas y mejoras futuras.

7. Referencias

    Lista de referencias utilizadas para la implementación y desarrollo del sistema.

**Apéndices**

    [Planilla de Autoevaluación](https://docs.google.com/spreadsheets/d/1cc_deQ0V0TbBGHj1S45etZ_w8wjDF2ecA7n0Xwxf-p8/edit?gid=0#gid=0)
    Código fuente comentado (si es necesario).
    Ejemplos adicionales de ejecución o casos de prueba.
    