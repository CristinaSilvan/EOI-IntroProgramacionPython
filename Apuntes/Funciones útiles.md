# Índice

>[Operaciones matemáticas](#operaciones-matemáticas)
>[Variables matemáticas](#variables-matemáticas)
>[Parsear](#parsear)
>[Conjuntos de datos](#conjuntos-de-datos)
>>(**NOTA: las funciones con un punto delante, se utilizan con el identificador del objeto al que queremos aplicar la función delante del punto**)

# Operaciones matemáticas
> Importando el módulo **math**
* math.trunc() -> Trunca
* math.factorial() -> Factorial
* math.pow() -> Potencia
* math.cos() -> Coseno
* math.sin() -> Seno
* math.tan() -> Tangente
* math.log() -> Logaritmo (en base n)
* math.log2() -> Logaritmo (en base 2)
* math.log10() -> Logaritmo (en base 10)
* math.sqrt() -> Raíz cuadrada

# Variables matemáticas
> Importando el módulo **math**
* math.e -> Número e
* math.pi -> Número pi

# Parsear
* int()
* float()
* str()
* list()
* tuple()
* set()
> (**NOTA: solo pueden usarse con objetos con propiedades o datos compatibles**)

# Conjuntos de datos
>>* in -> Palabra reservada que devuelve un boolean si encuentra el elemento (puede usarse en el bucle **for** para que una variable recorra las posiciones de una colección)
>>* not -> Palabra reservada que cambia le valor boolean a su opuesto (**not True == False** y **not False == True**)

* len() -> Tamaño
* max() -> Mayor elemento
* min() -> Menor elemento
* clone(**_objeto colección_**) -> Para clonar una colección (copiar los elementos y sustituirlos en la que queremos)
* .index(**_dato_**) -> Muestra la posición en la que se encuentra el dato
* .count(**_dato_**) -> Muestra cuántas veces se repite el dato
* .pop(**_dato_**) -> Elimina el dato de la colección (si no le especificamos, elimina el último)
* .remove(**_posición_**) -> Elimina el dato que se encuentra en la posición
* .clear() -> Elimina todos los elementos
* .reverse() -> Pone los elementos en orden inverso
* .sort() -> Ordena los elementos de forma ascendente (descendente si especificamos **reverse=True**)
* append(**_dato_**) -> Para agregar un elemento al final
* insert(**_posición_**, **_elemento_**) -> Para agregar un elemento en la posición especificada
* extend(**_dato1_**, **_dato2_**, **_dato3_**) -> Para agredar varios elementos a la vez (al final)
> (**NOTA: las funciones que modifican las colecciones, no se pueden utilizar con colecciones inmutables (tuplas, cadenas)**)

## Cadenas y caracteres
* .isdigit() -> Consultar si hay un dígito en la cadena
* .lower() -> Convertir en minúsculas
* .upper() -> Convertir a mayúsculas
* .swapcase() -> Convertir minúsculas a mayúsculas y viceversa
* len(**_cadena_**) -> Longitud de la cadena
* .capitalize() -> El primer caracter en mayúsculas y el resto en minúsculas
* .count(**_caracter_**) -> Cuenta cuántas veces se repide el caracter
* .replace(**_cadena1_**, **_cadena2_**) -> Reemplaza la cadena1 por la cadena2
* .find(**_cadena_**) -> Enumera los caracteres existentes hasta la cadena seleccionada

## Diccionarios
> (**NOTA: para agregar elementos diccionario[clave] = valor**)
* del(**_diccionario[clave]_**) -> Para eliminar un elemento (la clave y su valor)
* .get(**_clave_**) -> Encuentra el valor para la clave
* .get(**_clave_**, **_mensaje_**) -> (Opcional) si no encuentra la clave o el valor, devuelve un mensaje específico
* .keys() -> Devuelve todas las claves en el diccionario
* .values() -> Devuelve todos los valores en el diccionario
* .items() -> Devuelve todos los elementos (clave y valor/valores) en forma de **lista**

## Sets
* set(**_elementos_**) -> Para crear un objeto **set**
* .add(**_elemento_**) -> Para agregar un elemento (se pondrá en una posición u otra según el orden de elementos)
* .discard(**_elemento_**) -> Elimina el elemento
* .issubset(**_set_**) -> Pregunta si los elementos de nuestro **set** se encuentran TODOS en el set que especifiquemos
* .issuperset(**_set_**) -> Pregunta si en los elementos de nuestro **set** se encuentran TODOS los elementos del set que especifiquemos
* .isdisjoin(**_set_**) -> Pregunta si los elementos de nuestro **set** son TODOS diferentes a los del set que especifiquemos
* frozenset(**_set_**) -> Para convertir a **inmutable**
> (**NOTA: es recomendable declarar estos conjuntos con la función set(), ya que los diccionarios también se identifican con { } y puede haber confusión por parte del lenguaje**)


## Json