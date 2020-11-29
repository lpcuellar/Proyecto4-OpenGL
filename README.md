# OpenGL1-Cameras

## Controles:

Traslación de cámara:
* a --> mover la cámara para la izquierda
* d --> mover la cámara para la derecha
* s --> mover la cámara para la atrás
* w --> mover la cámara para la adelante
* KEY UP --> mover la cámara hacia arriba
* KEY DOW --> mover la cámara hacia abajo

Rotación de cámara:
* q --> aumenta roll de cámara
* e --> disminuye roll de cámara
* r --> aumenta pitch de cámara
* f --> disminuye pitch de cámara
* x --> aumenta yaw de cámara
* z --> disminuye yaw de cámara

Cambio de modelos:
* 1 --> cambiar a carro F1 Ferrari
* 2 --> cambiar a Top Gun
* 3 --> cambiar a calabaza de halloween
* 4 --> cambiar a carro de F1 Lotus

Tipo de render:
* o --> cambiar a modo relleno
* p --> cambiar a modo wireframe



## Descripción:

El objetivo de éste proyecto es demostrar los conocimientos adquiridos a lo largo del semestre.

Los alumnos deben entregar un visualizador de modelos creado en base al renderer de OpenGL que se les proveyó.

La nota máxima es de 100 puntos. Se entregarán los siguientes puntos por cada uno de los objetivos que se cumplan. Pueden escoger los objetivos que quieran. No hay puntos extra.

* 40 puntos máximo por modelos cargados en el visualizador.
* 10 puntos cada modelo, máximo de 4 modelos.
    * Sólamente un modelo se debe ver a la vez. Implementar algún input para cambiar modelos.
* 40 puntos máximo por movimiento de cámara.
    * 15 puntos, movimiento circular al rededor del modelo, enfocado siempre en el centro del modelo.
    * 15 puntos, movimiento de la cámara hacia arriba y hacia abajo, pero siempre enfocado en el centro del modelo.
    * 10 puntos, Zoom In y Zoom out de la cámara, con un límite de cuanto se puede acercar o cuanto se puede alejar.
* 20 puntos, la cámara se puede controlar usando input del mouse.
* 0 - 30 puntos según uso creativo de shaders (iluminación compleja, usar input para variar algún valor dentro del shader, uso de mapas normales, toon  shading, etc)
* 0 - 20 puntos según características extras que el alumno agregue al programa (menús, música o efectos de sonido, imagen de fondo, etc)

Pueden usar texturas o modelos que encuentren en internet. Se les recuerda también que hay bastante documentación en línea en caso de que necesiten más información acerca de OpenGL.
