# preentrega3

#  Navegación:
Dentro del sitio se encuentra la barra de navegación (Nav bar), que contiene enlaces a las siguientes páginas:

Nuevos Autores: Página para agregar nuevos autores al sistema.<br>
Nuevos Libros: Página para agregar nuevos libros al sistema.<br>
Nuevos Generos: Página para agregar nuevos géneros al sistema.<br>
Busqueda: Página para realizar búsquedas en la base de datos, la búsqueda se realiza con el nombre del autor.

Cada una de estas páginas permite interactuar con los modelos de datos mediante formularios fáciles de usar.

#  Funcionalidades:
Agregar Autor:<br>
Para agregar un nuevo autor, navega a la página "Nuevos Autores" desde la barra de navegación. Completa el formulario con la información requerida y haz clic en "Enviar". Una vez agregado un autor, serás redirigido a la página de inicio.

Agregar Libro:<br>
Para agregar un nuevo libro, navega a la página "Nuevos Libros" desde la barra de navegación. Completa el formulario con la información requerida y haz clic en "Enviar". Una vez agregado un libro, serás redirigido a la página de inicio.

Agregar Genero:<br>
Para agregar un nuevo género, navega a la página "Nuevos Generos" desde la barra de navegación. Completa el formulario con la información requerida y haz clic en "Enviar". Una vez agregado un género, serás redirigido a la página de inicio.


Búsqueda:<br>
Para realizar búsqueda de un autor, hay que navegar a la página de búsqueda desde la barra de navegación, ingresa el nombre del autor y envía el formulario con el botón enviar. Los resultados se mostrarán en una nueva página.

Estructura del Proyecto:<br>
El proyecto sigue una estructura organizada y modular, utilizando herencia HTML para evitar la redundancia de código y facilitar el mantenimiento. La lógica de la aplicación se encuentra en las vistas de la aplicación preentrega3app, donde se gestionan las solicitudes y respuestas HTTP.

#  Modelos
Autor: Representa a un autor literario con atributos como nombre y biografía.<br>
Libro: Representa un libro con atributos como título y fecha de publicación.<br>
Genero: Representa un género literario con atributos como tipo y descripción.

#  Vistas
Las vistas gestionan los formularios para crear nuevos autores, libros y géneros, además de la lógica de búsqueda. Estas se pueden encontrar en el archivo views.py de la aplicación preentrega3app.

#  Plantillas
Las plantillas HTML utilizan herencia para compartir elementos comunes entre las páginas, como la barra de navegación y los estilos. Esto se logra mediante la creación de una plantilla base que es extendida por otras plantillas específicas.
