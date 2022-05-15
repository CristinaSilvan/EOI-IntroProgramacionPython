# Índice

>[Operaciones matemáticas](#operaciones-matemáticas)
>
>[Variables matemáticas](#variables-matemáticas)
>
>[Parsear](#parsear)
>
>[Conjuntos de datos](#conjuntos-de-datos)
>
>>(**NOTA: las funciones con un punto delante, se utilizan con el identificador del objeto al que queremos aplicar la función delante del punto**)

dir(**_objeto_**) -> Devuelve toda la información sobre la clase del objeto (atributos, métodos, etc)

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
* type() -> Consultar tipo de dato o clase
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
* **_símbolo_**.join(**_colección_**) -> Para asignar a un objeto los elementos de la colección unidos por el **_símbolo_** especificado
* .strip() -> Elimina los espacios de una cadena al principio y al final
* .strip(**_elementos_**) -> Elimina los elementos **especificados** de la cadena
* .rstrip() -> Elimina los espacios en blanco solo del final (**right**)
* .lstrip() -> Elimina los espacios en blanco del principio (**left**)
* .clone(**_objeto colección_**) -> Para clonar una colección (copiar los elementos y sustituirlos en la que queremos)
* .index(**_dato_**) -> Muestra la posición en la que se encuentra el dato
* .count(**_dato_**) -> Muestra cuántas veces se repite el dato
* .pop(**_dato_**) -> Elimina el dato de la colección (si no le especificamos, elimina el último)
* .remove(**_elemento_**) -> Elimina el dato correspondiente (da un error si no encuentra el elemento)
* .discard(**_elemento_**) -> Elimina el dato correspondiente
* .clear() -> Elimina todos los elementos
* .reverse() -> Pone los elementos en orden inverso
* .sort() -> Ordena los elementos de forma ascendente (descendente si especificamos **reverse=True**)
* .append(**_dato_**) -> Para agregar un elemento al final
* .insert(**_posición_**, **_elemento_**) -> Para agregar un elemento en la posición especificada
* .extend(**_dato1_**, **_dato2_**, **_dato3_**) -> Para agredar varios elementos a la vez (al final)
* .update(**_colección_**) -> Para agregar los elementos de una **colección de datos** dentro de **otra colección**
> (**NOTA: las funciones que modifican las colecciones, no se pueden utilizar con colecciones inmutables (tuplas, cadenas)**)

> (**NOTA: si pasamos por patámetros una colección, update y extend introducirán uno a uno los elementos mientras que append añadirá dicha colección como un elemento por sí solo**)

```
lista1 = [1,2,3]
lista2 = [4,5,6]

lista1.extend(lista2) -> lista1 = [1,2,3,4,5,6]
# De igual forma con el método update
```

```
lista1 = [1,2,3]
lista2 = [4,5,6]

lista1.append(lista2) -> lista1 = [1,2,3,[4,5,6]]
```

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
* .keys() -> Devuelve todas las claves en el diccionario en forma de **lista**
* .values() -> Devuelve todos los valores en el diccionario en forma de **lista**
* .items() -> Devuelve todos los elementos (clave y valor/valores) en forma de **tupla**

## Sets

> Los elementos de los Sets o Conjuntos **NO PUEDEN** ser accedidos mediante índices:

```
set = {1,2,3}
print(set[0]) -> ERROR
```

* set(**_elementos_**) -> Para crear un objeto **set**
* .add(**_elemento_**) -> Para agregar un elemento (se pondrá en una posición u otra según el orden de elementos)
* .discard(**_elemento_**) -> Elimina el elemento
* .issubset(**_set_**) -> Pregunta si los elementos de nuestro **set** se encuentran TODOS en el set que especifiquemos
* .issuperset(**_set_**) -> Pregunta si en los elementos de nuestro **set** se encuentran TODOS los elementos del set que especifiquemos
* .isdisjoin(**_set_**) -> Pregunta si los elementos de nuestro **set** son TODOS diferentes a los del set que especifiquemos
* frozenset(**_set_**) -> Para convertir a **inmutable**
> (**NOTA: es recomendable declarar estos conjuntos con la función set(), ya que los diccionarios también se identifican con { } y puede haber confusión por parte del lenguaje**)


## Json
> Importando el módulo **json**
* json.dumps() -> Serializar o hidratar (convertir a colección json) (**La clase del objeto es String**)
* json.loads() -> Deserializar o deshidratar (convertir a colección diccionario, lista o string según los elementos)