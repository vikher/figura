# Figuras
---

Esta es una API que se recogen los clics del ratón. Si los clics forman un triángulo, entonces se calcula el área. Lo mismo ocurrirá con un cuadrado.

##Pasos

La aplicación consiste en una página HTML, cargando un script JS que hará lo siguiente:

1. El usuario podrá hacer clic en cualquier parte de la pantalla, cada vez que el usuario haga clic (con cualquier botón), la aplicación registrará los puntos

2. En la parte superior de la página,se agrega un campo de texto deshabilitado que contiene los resultados de validación (id = "response")

3. En la parte inferior de la pantalla habrá un botón llamado "Enviar"

4. Una vez que haga clic en el botón enviar, la aplicación:

4.1. Recojera los puntos e identificar si el usuario dibujó un CUADRADO, un TRIÁNGULO u otra figura.

4.1.1 Si el usuario dibujó un CUADRADO, calculará el área de la figura y creará la alerta:```"Pensamientos cuadrados: <area>"```

4.1.2 Si el usuario dibujó un TRIÁNGULO, entonces calculará el área de la figura, identificará el tipo de triángulo y creará la alerta indicando qué tipo de triángulo fue encontrado, si es Isósceles o no: "Isósceles!" || "Sólo otro triángulo"

_Hint: _isosceles = (b == c || a == b || c == a))? verdadero Falso;

4.1.3 Si el usuario dibuja una forma aleatoria, calcule la distancia recorrida desde el primer clic hasta el último (justo antes de presionar "Enviar")

5. Una vez que los datos estén listos, valide sus resultados:

5.1. Para Squares - Llame ```https://example.org/square?area=<area>;&points=<a base64 cadena representación de [(x1, y1), (x2, y2), (x3, y3), (x4, Y4)]>``` e inserta la respuesta en el campo de texto de respuesta

5.2. Para Triángulos - Llame ```https://example.org/triangle?area=<area>&type=<isosceles|other>&points=<a base64 representación de cadena de [(x1, y1), (x2, y2), (x3, Y3)]>``` e inserta la respuesta en el campo de texto de respuesta _Response es sólo la cadena "response = true;" O "respuesta = falso;" Dependiendo de los resultados

Importante: No use AJAX para este ejercicio



## Cómo ejecutar

`Python server.py`

## Subir a heroku
El proyecto incluye `Procfile`; Prácticamente todo lo que se necesita hacer es comentar la configuración de registro en `server.py` o crear el archivo` server.log` antes de ejecutar un git push a su repositorio ** heroku **.

## Requisitos
* Python 2.7 o 3.6
Frasco
* Un navegador (para sus pruebas)

## URL de prueba

* URL válida: `https://localhost:5000/triangle?area=3353&type=other&points=W1szNDIsODBdLFszNjIsMjldLFs0NjgsOTRdXQ==`

Los puntos son una matriz de N puntos codificados a base64. 

Ejemplo

```b'[[342,80],[362,29],[468,94]]' encoded ==> /triangle?area=3353&type=other&points=W1szNDIsODBdLFszNjIsMjldLFs0NjgsOTRdXQ==``