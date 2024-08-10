## Informe del Proyecto: Sistema de Gestión de Tareas Pendientes
1. Introducción

    Este proyecto titulado "Sistema de Gestión de Tareas Pendientes" es una propuesta de la cátedra de Programación 2 de la Tecnicatura en Desarrollo de Software del Instituto Técnico Superior Córdoba. El desarrollo del mismo se orienta a implementar un sistema que permita a usuarios facilitar la gestión de tareas de manera efectiva. SU funcionamiento se basa tanto en la posibilidad de agregar, eliminar y marcar tareas como completas como en la posibilidad de tener un sistema de prioridades de dichas tareas, realizar búsquedas y organizarlas, etc.
    
    Es importante recalcar que la práctica ayuda a aprehender conocimientos y conceptos trabajados en clase, tales como POO, estructuras de datos (en este caso, focalizando en listas enlazadas), nociones de orden y análisis de algoritmos, etc. Muchas veces los ejercicios realizados en el transcurso de la cursada son pequeños recortes que no reflejan del todo la compleja realidad de la profesión. De esta manera comenzamos a entender cómo se aplica en un caso concreto todo lo visto en la materia de manera integral. Es importante destacar que el trabajo en grupo es una práctica que nos prepara para integrar en un futuro algún equipo de trabajo.


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

        -buscar_tarea_id: recorre la lista y recibe un parámetro para comparar con el id de la tarea del nodo actuak que tenga.

        -   mostrar_estadisticas: muestra por pantalla un calculo del porcentaje de tareas que figuran completas sobre el total de las tareas de la lista enlazada.

        -   menu: es un procedimiento que muestra en pantalla las opciones posibles a elegir enumerandolas del 1 al 12

        -   main: es una función sin parámetros formado por una lista de tareas de clase lista enlazada donde con un bucle y según la opción ingresada por el ususario, ejecuta los métodos de la lista enlazada. Se crea la variable lista_tareas que contiene un objeto de clase Lista_Enlazada. Con un bucle que se ejecute siempre y cuando no se ingrese la opción 12 para salir del programa. Se ejecuta usando el procedimiento menu(), según la opción ingresada por el usuario en esa variable y ejecuta los métodos definidos de la lista enlazada para correr el programa.
        
    Estructuras de Datos Utilizadas:
        Explicación de la implementación de la lista enlazada y nodos en el sistema.

3. Metodología y Diseño
    Diseño del Código:
        Descripción concisa de las clases principales (Tarea, Nodo, ListaEnlazada) y su interacción.

4. Implementación y Ejemplos

    Detalles de Implementación:
        Explicación breve de cómo se implementaron las funcionalidades principales.

    Implementamos el menú para que el usuario pueda interactuar y utilizar el programa de acuerdo a sus necesidades. Cada una de las funcionalidades fue testeada y modificada/corregida a medida que nos fue necesario para que el programa funcione eficientemente.


    Casos de Uso y Ejemplos:
        Ejemplos de ejecución del sistema para diferentes escenarios de uso.

5. Preguntas Conceptuales

    Preguntas para Análisis:
        ¿Qué sucede si intentamos agregar una tarea que ya existe en la lista?
        ¿Cómo se implementa la priorización de tareas en la lista enlazada? ¿Qué sucede si dos tareas tienen la misma prioridad?
        ¿Cuál es la complejidad temporal del método para eliminar una tarea de la lista enlazada?


        La complejidad temporal de eliminar tareas es de orden lineal ya que en el peor de los casos, el método deberá recorrer toda la lista pasando por todos los elementos. Podemos deducir esto gracias a la condición "While actual is not None" que nos indica que la variable actual recorre todos los elementos hasta llegar al último en caso de no encontrar la coincidencia con el id.

        ¿Cómo podríamos modificar el sistema para soportar múltiples categorías por tarea?
        Podemos asignarle al atributo categoria, una lista vacia en la que se guarden las categorias que el usuario quiera ingresar, lo que nos llevaría a modificar el atributo en la clase Tarea y modificar el menú debiendo crear una función que maneje la agregación de las categorias a la lista. 
        
        Ejemplo propuesto para que soporte múltiples categorias:
        Creamos una función para insertar un elemento a una lista que será la lista de categorias.


6. Resultados y Conclusiones

    Resultados Obtenidos:
        Evaluación del éxito en la implementación de las funcionalidades.
    La implementación de las funcionalidades fue exitosa aunque con errores en una primera etapa. Nos encontramos con varias excepciones que no sabiamos manejar o que se nos habían pasado por alto lo cual nos llevo a una revisión mas minusiosa para corregir los errores críticos que se hacian notar a la ejecución del programa y rompian la ejecución. Quedan aún muchas cosas por mejorar o corregir.

    Conclusiones:
        Resumen de los hallazgos y reflexiones sobre lecciones aprendidas y mejoras futuras.
    Nos encontramos con una nueva  estructura de datos que tuvimos que analizar y comprender para poder modificarla y agregar métodos, atributos, y funcionalidades que eran necesarias para cumplimentar lo requerido y el mismo funcionamiento del programa. Previo a estudiar esta estructura debimos trabajar en los trabajos prácticos propuestos y que no forman parte de este proyecto, lo que nos fue necesario para poder entender la funcionalidad del programa. Nos fue útil empezar a dibujar las partes del nodo y su comportamiento cuando debíamos recorrer la lista, determinar variables y su comportamiento. Tambien notamos la necesidad de muchas veces usar variables tipo "banderas" que nos ayudaron a manejar la lógica de la estructura de datos. Notamos que los inputs realizados no necesariamente se deben transformar a un entero, si no que muchas veces nos convino primero evaluar el valor ingresado para ver si nos iba a servir según lo que nosotros necesitabamos, y si nos servía transformarlo en un entero o en su caso contrario, conservarlo como string. Creamos un método que nos fue de mas utilidad para trabajar en la opcion 3 de eliminar tarea. 
    Como mejoras evaluaríamos hacer que los métodos trabajen retornando True y False de manera que podamos sacar los prints y a éstos usarlos en la funcionalidad de las opciones.
    Como lecciones aprendidas, podemos decir que es necesario documentar todo avance, corrección o propuesta en resolución para no perder la idea. Comentar con el equipo de trabajo alguna solución que creamos que puede funcionar para intercambiar conocimientos e ideas de manera que el código pueda mejorar con el aporte de todas las ideas. Fue necesario hacer una tabla donde tomabamos nota de todos los posibles errores que pudiesen presentarse para que no se pierda ninguno y poder trabajar en ellos.

7. Referencias

    Lista de referencias utilizadas para la implementación y desarrollo del sistema.

**Apéndices**

    [Planilla de Autoevaluación](https://docs.google.com/spreadsheets/d/1cc_deQ0V0TbBGHj1S45etZ_w8wjDF2ecA7n0Xwxf-p8/edit?gid=0#gid=0)
    [Planilla Testing](https://docs.google.com/spreadsheets/d/1P0drrJUKzYMrdugy-SfrxAiWSMMYc31YnIFXeRP8NN0/edit?pli=1&gid=0)
    Código fuente comentado (si es necesario).
    Ejemplos adicionales de ejecución o casos de prueba.
    