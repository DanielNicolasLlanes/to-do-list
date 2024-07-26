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
        -   esta_vacia: recorre la lista y devuelve un valor booleano que indica si la lista enladaza esta vacía.

        -   agregar_tarea: con los 3 valores que pide como parámetros, crea los nodos de la lista enlazada, le da un id a cada nueva tarea agragada, y las va acomodando en la lista según la prioridad mas alta, mostrando al usuario un msj satisfactorio en caso de haberse agregado de manera efectiva la tarea. En éste mismo método en dos atributos diferentes, se van contando las tareas que se ingresan las cuales inmediatamente suman como pendientes y el tamaño que refiere a la cantidad de tareas agregadas.

        -   buscar_tarea_descripción: recorre la lista y devuelve un valor booleano al pedir que se ingrese como parámetro un texto que lo compara con la descrición de la tarea del nodo.

        -   completar_tarea: (pide id y cambia completado a True. no devuelve nada. actualiza self.pendientes)

        -   eliminar_tarea: (pide id para buscar y eliminar, recorre la lista, actualiza self.pendientes y self.tamano, muestar en pantalla tarea elimnada o  no encontrada)

        -   mostrar_tareas: (recorre la lista. muestra estado de completada o pendiente, y los datos de las tarea)

        -   mostrar_tareas_pendientes: (recorre la lista y si completada es falso muestra en pantalla la tarea actual con sus parámetros)

        -   mostrar_tareas_descripcion: (recorre la lista. pide un parámetro de texto que si coincide con la descripcion del nodo actual, muestar en pantalla la tarea con sus parámetros)

        -   contar_tareas_pendientes: (de orden lineal. cuenta la cantidad de tareas que figuran pendientes)

        -   contar_tareas_pendientes_cte: (de orden cte. devuelve el valor del atributo self.pendientes)

        -   mostrar_estadisticas: (muestra por pantalla un calculo del porcentaje de tareas que figuran completas sobre el total de las tareas ingresadas)

        -   agregar_tarea_existente: (pide una tarea, crea un nodo con esa tarea, compara prioridades y va buscando el lugar para agregar ese nodo. cuando inserta el nodo actualiza el id de la tarea)

        -   menu: (procedimiento que muestra en pantalla las opciones posibles a elegir enumerandolas del 1 al 8)

        -   main: (procedimiento sin parámetros formado por una lista de tareas de clase lista enlazada donde con un bucle y según la opción ingresada por el ususario, ejecuta los métodos de la lista enlazada. crea la variable lista_tareas que contiene un objeto de clase Lista_Enlazada. Con un bucle while True y usando el procedimiento menu(), según la opción ingresada por el usuario ejecuta los métodos definidos de la lista enlazada y efectiviza el programa)
        
    Estructuras de Datos Utilizadas:
        Explicación de la implementación de la lista enlazada y nodos en el sistema.

3. Metodología y Diseño
    Diseño del Código:
        Descripción concisa de las clases principales (Tarea, Nodo, ListaEnlazada) y su interacción.
        -   clase Tarea:(cada objeto de esta clase se crea con el id, descripcion y prioridad ingresadas por el usuario, mientras que el atributo categoria si no es ingresado por el usuario el programa le asigna por defecto el valor "General" y el atributo completada siempre inicializado en False.)

        -   clase nodo: (dcreada con dos atributos, uno que es la tarea en si y otra parte que es el espacio que apunta al siguiente. Esta clase creará los nodos que necesita la lista enlazada) 

        -   clase ListaEnlazada: (define el contructor de la lista inicializando la cabeza en None, el id_actual en 1 que luego va incrementando y se definen dos atributos pendiente y tamano iniciados en 0 que se usan en los metodos de la misma clase)

        Interacción: La lista enlazada esta formada por nodos que se crean con la clase nodo y cuyos datos serán los referidos a la clase Tarea

4. Implementación y Ejemplo
    Detalles de Implementación:
        Explicación breve de cómo se implementaron las funcionalidades principales.
        
    Casos de Uso y Ejemplos:
        Ejemplos de ejecución del sistema para diferentes escenarios de uso.

5. Preguntas Conceptuales

    Preguntas para Análisis:
        ¿Qué sucede si intentamos agregar una tarea que ya existe en la lista?
        ¿Cómo se implementa la priorización de tareas en la lista enlazada? ¿Qué sucede si dos tareas tienen la misma prioridad?
        ¿Cuál es la complejidad temporal del método para eliminar una tarea de la lista enlazada?
        ¿Cómo podríamos modificar el sistema para soportar múltiples categorías por tarea?

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
    