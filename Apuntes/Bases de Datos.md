# Índice

[Bases de Datos](#bases-de-datos)

[Cuando usar SQL y cuando NoSQL](#cuando-usar-sql-y-cuando-nosql)

[MongoDB](#mongodb)

[Escalabilidad Vertical u Horizontal](#escalabilidad-vertical-u-horizontal)

[Vídeos útiles](#vídeos-útiles)


# Bases de Datos

Conjunto de datos perteneciente a un mismo contexto y almacenados sistemáticamente para su uso posterior

* Bases de Datos **SQL**:
**Relacional** o **SGBDR(Sistema de Gestión de Bases de Datos Relacionales)**

    * **Ejemplos SQL**:
        * MySQL
        * SQLite
        * SQL Server
        * Postgresql
        * Oracle

* Bases de Datos **NoSQL**:
**No relacional**, o a veces llamado **No solo SQL**, es una amplia clase de sistemas de gestión de bases de datos que difieren del modelo clásico relacional en aspectos importantes, siendo el punto más destacado la no necesidad de usar **el lenguaje SQL** como medio de consulta

    * **Ejemplos NoSQL**:
        * MongoDB
        * Solr
        * ElasticSearch
        * Cassandra

>> [Volver al Índice](#índice)

# Cuando usar SQL y cuando NoSQL

* Las **SQL** se crearon para mantener la integridad, por lo que los datos introducidos deben ser almacenados de forma estricta. Todos los datos de una tabla, deben tener los mismos campos, con un máximo especificado, un tipo de dato especificado y las tablas deben estar distribuidas correctamente según su información (y otras muchas formas de seguridad)

* Las **NoSQL** no son tan rigurosas, por lo que dan prioridad a la velocidad, en la actualidad en auge en las plataformas que no necesitan tanta seguridad y supone mucha latencia o dificultad mantener una base de datos tan rígida. La introducción de datos es flexible.

>> [Volver al Índice](#índice)

# MongoDB

Es una base de datos documental, lo que significa que almacena datos en forma de documentos tipo **JSON**. Por ende, se le considera una base de datos **NoSQL**

> (NOTA: **JSON** es un formato de texto sencillo para el intercambio de datos y completamente independiente del lenguaje, pero utiliza convenciones que son ampliamente conocidas por los programadores. En la actualidad, es tratado de forma nativa en la mayoría de lenguajes)

>> [Volver al Índice](#índice)

# Escalabilidad Vertical u Horizontal

En lo relacionado a las bases de datos, existen dos conceptos importantes que reflejan el crecimiento de esta:

* **Escalabilidad Vertical** o escalar hacia arriba: significa crecer en cuanto al hardware de uno de los nodos, es decir aumentar el hardware por uno más potente, como disco duro, memoria, procesador, etc. pero también puede ser la migración completa del hardware por uno más potente. El esfuerzo de este crecimiento es mínimo, pues no tiene repercusiones en el software, ya que solo será respaldar y migrar los sistemas al nuevo hardware.

    * **Ventajas**:
        *   No implica un gran problema para las aplicaciones, pues todo el cambio es sobre el hardware
            
        *   Es mucho más fácil de implementar que el escalamiento horizontal.
            
        *   Puede ser una solución rápida y económica (compara con modificar el software)

    * **Desventajas**:
        *   El crecimiento está limitado por el hardware.

        *   Una falla en el servidor implica que la aplicación se detenga.

        *   No soporta la Alta disponibilidad.

        *   Hacer un upgrade del hardware al máximo pues llegar a ser muy caro, ya que las partes más nuevas suelen ser caras con respecto al rendimiento de un modelo anterior.

* **Escalabilidad horizontal** es sin duda el más potente, pero también el más complicado. Este modelo implica tener varios servidores (conocidos como Nodos) trabajando como un todo. Se crea una red de servidores conocida como Cluster, con la finalidad de repartirse el trabajo entre todos nodos del cluster, cuando el performance del cluster se ve afectada con el incremento de usuarios, se añaden nuevos nodos al cluster, de esta forma a medida que es requeridos, más y más nodos son agregados al cluster. Para que el escalamiento horizontal funcione deberá existir un servidor primario desde el cual se administra el cluster. Cada servidor del cluster deberá tener un software que permite integrase al cluster, por ejemplo, para las aplicaciones Java, tenemos los servidores de aplicaciones como Weblogic, Widfly, Websphere, etc. y sobre estos se montan las aplicaciones que queremos escalar.

    * **Ventajas**:
        *   El crecimiento es prácticamente infinito, podríamos agregar cuantos servidores sean necesarios

        *   Es posible combinarse con el escalamiento vertical.

        *   Soporta la alta disponibilidad

        *   Si un nodo falla, los demás sigue trabajando.

        *   Soporta el balanceo de cargas.
 
    * **Desventajas**:
        *   Requiere de mucho mantenimiento

        *   Es difícil de configurar

        *   Requiere de grandes cambios en las aplicaciones (si no fueron diseñadas para trabajar en cluster)

        *   Requiere de una infraestructura más grande.

>> [Volver al Índice](#índice)

# Vídeos útiles

[Curso de MongoDB](https://www.youtube.com/watch?v=qmZrygfP7cQ&list=PLCTD_CpMeEKQ9_WJOtexctR6Iqw7whMXY&index=3)

[MongoDB con Python](https://www.youtube.com/watch?v=y2HFAYBao8M&list=PLCTD_CpMeEKR5cVnmTyFqUuzBOmEAjG4z)

[Manejo Básico SQLite](https://www.youtube.com/watch?v=ZJuVQ9jUg-A&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=55)

>> [Volver al Índice](#índice)