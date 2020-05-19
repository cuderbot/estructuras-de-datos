# Listas Enlazadas

Una Lista Enlazadas (linked list en inglés), es una de las estructuras de datos fundamentales, y puede ser utilizada para implementar otras estructuras de datos. Consiste en una secuencia de nodos, en los que se puede almacenar datos, y una o dos referencias (enlaces o punteros) al nodo anterior o posterior. El principal beneficio de las listas enlazadas respecto a los vectores convencionales es que el orden de los elementos enlazados puede ser diferente al orden de almacenamiento en la memoria o el disco, permitiendo que el orden de recorrido de la lista sea diferente al de almacenamiento.

Una lista enlazada es un tipo de dato autorreferenciado porque contienen un puntero o enlace (en inglés link, del mismo significado) a otro dato del mismo tipo. Las listas enlazadas permiten inserciones y eliminación de nodos en cualquier punto de la lista en tiempo constante (suponiendo que dicho punto está previamente identificado o localizado), pero no permiten un acceso aleatorio. Existen diferentes tipos de listas enlazadas: listas enlazadas simples, listas doblemente enlazadas, listas enlazadas circulares y listas enlazadas doblemente circulares.


## Tipos de listas enlazadas

Las listas enlazadas se pueden clasificar en:

### Listas enlazadas lineales

#### Listas enlazadas lineales simples

Estas se caracterizan en que su nodo solo posee un puntero al nodo siguiente, y el enlace del último nodo contiene NULL para indicar el final de la lista. Aunque normalmente a la variable de referencia se la suele llamar top, se le podría llamar como se desee.

#### Listas enlazadas lineales dobles

Un tipo de lista enlazada más sofisticado es la lista doblemente enlazada o lista enlazadas de dos vías. Cada nodo tiene dos enlaces: uno apunta al nodo anterior, o apunta al valor NULL si es el primer nodo; y otro que apunta al nodo siguiente, o apunta al valor NULL si es el último nodo.


### Listas enlazadas circulares

#### Listas enlazadas circulares simples

En una lista enlazada circular, el primer y el último nodo están unidos juntos. Esto se puede hacer tanto para listas enlazadas simples como para las doblemente enlazadas. Para recorrer una lista enlazada circular podemos empezar por cualquier nodo y seguir la lista en cualquier dirección hasta que se regrese hasta el nodo original. Desde otro punto de vista, las listas enlazadas circulares pueden ser vistas como listas sin comienzo ni fin. Este tipo de listas es el más usado para dirigir buffers para “ingerir” datos, y para visitar todos los nodos de una lista a partir de uno dado.

#### Listas enlazadas circulares dobles

En una lista enlazada doblemente circular, cada nodo tiene dos enlaces, similares a los de la lista doblemente enlazada, excepto que el enlace anterior del primer nodo apunta al último y el enlace siguiente del último nodo, apunta al primero. Como en una lista doblemente enlazada, las inserciones y eliminaciones pueden ser hechas desde cualquier punto con acceso a algún nodo cercano. Aunque estructuralmente una lista circular doblemente enlazada no tiene ni principio ni fin, un puntero de acceso externo puede establecer el nodo apuntado que está en la cabeza o al nodo cola, y así mantener el orden tan bien como en una lista doblemente enlazada.


## Operaciones

* ***crear (constructor)***: Crea una lista enlazada vacia.
* ***Insertar (insert)***: Inserta un nodo en la lista enlazada. La inserción puede ser:
  * Al comienzo (push)
  * En la mitad (insertAfter)
  * Al final (append)
* ***Buscar (search)***: Permite buscar un nodo en base a una condicion (por lo general en base a una llave).
* ***Eliminar (remove)***: Remueve un nodo en la lista enlazada. Al igual que en la inserción puede ser:
  * Al comienzo (remove at the beginning)
  * En la mitad (remove to the middle)
  * Al final (remove at the end)
* ***Tamaño de la lista (size)***: devuelve la cantidad de nodos en la lista.
* ***esta vacia(is empty)***: devuelve un valor booleano si la lista esta vacia o no.


## Referencias
[wikipedia](https://es.wikipedia.org/wiki/Lista_enlazada)