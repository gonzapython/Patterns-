
# CULTURILLA
Los patrones de diseño se pueden clasificar en tres categorías:

 * Patrón creacional.  Ejemplos:  MVC, Singleton, Factory.
 * Patrón estructural
 * Patrón de comportamiento

# PATRÓN SINGLETON:
Se utiliza para:
 * Garantizar que una clase tenga sólo una instancia: sucesivas instancias de la clase son, en realidad, la misma dirección de memoria.
 * Proporcionar un único punto de acceso a la instancia.

Es muy utilizado para hacer login, donde sólo se quiere tener una instancia que centralice todo.


# CONCEPTOS PREVIOS
Antes de ver el programa de ejemplo singleton.py, hemos de conocer:

 - Métodos `__new__` / `__init__`
------------------------------
Hay que saber que:
 * el método `__init__` crea el objeto y luego lo inicializa.
 * el método `__new__` sólo crea el objeto, no le da un valor inicial.

El método `__new_` recibe el parámetro `'cls'`, que indica la clase que va a ser instanciada: `__new__(cls)`.
Éste parámetro lo informa automáticamente el 'parser' (analizador) de Python en el momento de la instanciación.


 - `hasattr( objeto, nombre )` - Built-in (función incorporada) 
---------------------------
Los argumentos son: un objeto y un string.
El resultado es `True` si el string es el nombre de uno de los atributos del objeto, `False` si no. 
Ejemplo: nos dice si una propiedad determinada es de una clase concreta.


Utilizando los conceptos descritos, en el programa `singleton.py` se puede ver que, usando el método `__new__(cls)`, se genera siempre la misma dirección de memoria al hacer sucesivas instancias de la clase `SoyUno()`.



Referencias:
------------

https://riptutorial.com/es/python/example/30108/introduccion-a-los-patrones-de-diseno-y-patron-singleton-

https://www.code-learner.com/how-to-use-python-__new__-method-example/

https://docs.python.org/3/library/functions.html#hasattr
