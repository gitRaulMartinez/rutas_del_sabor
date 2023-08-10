# Rutas del Sabor

Proyecto Integrador de Mil Programadores Salteños con Python. Este proyecto cumple con el requisito para finalizar el curso Mil Programadores con Python. La aplicación elegida fue "Food Travel", una aplicación que facilita a los usuarios la búsqueda de destinos culinarios.

## Herramientas utilizadas

Se utilizaron diversas bibliotecas y herramientas para llevar a cabo el proyecto, que se dividen en dos partes: FrontEnd y Backend.

### FrontEnd

Para la parte visual, se hizo uso principalmente de **customtkinter**, con **Pillow** y **tkintermapview** para imágenes y mapas, respectivamente.

### Backend

Se empleó el framework **Flask**, con la base de datos **Realtime Database** de Firebase. También se empleó Google Cloud Storage para guardar algunas imágenes de mayor peso.

Es importante tener en cuenta que el servidor de Flask se encuentra en producción. Puede consultar los distintos Modelos de datos en los siguientes enlaces:

| Model     | Link      | Url                |
| :-------- | :------- | :------------------------- |
| General | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/all/) | rutasdelsabor.softwarebasics.com.ar/all/ |
| Users | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/users/) | rutasdelsabor.softwarebasics.com.ar/users/ |
| Destinos culinarios | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/culinary_destinations/) | rutasdelsabor.softwarebasics.com.ar/culinary_destinations/ |
| Ubicaciónes | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/locations/) | rutasdelsabor.softwarebasics.com.ar/locations/ |
| Actividades | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/activities/) | rutasdelsabor.softwarebasics.com.ar/activities/ |
| Rutas | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/routes_visit/) | rutasdelsabor.softwarebasics.com.ar/routes_visit/ |
| Reviews | [Ver json](https://rutasdelsabor.softwarebasics.com.ar/reviews/) | rutasdelsabor.softwarebasics.com.ar/reviews/ |

## Iniciar proyecto

Si usa virtualenv. Inicie virtualenv

```
virtualenv env
```
Active el virtualenv

**Windows**

```
venv\Scripts\activate
```

**Linux o Mac**
```
source venv/bin/activate
```

Instale las librerias.
```
pip install -r requirements.txt
```

Se dirige a la carpeta  tkinter
```
cd tkinter
```
Ejecuta la aplicacion
```
python main.py
```

## Rutas del Sabor con Customtkinter

A continuación, se presentan algunas imágenes del proyecto:

### Inicio de Sesión
![Login](https://storage.googleapis.com/rutas-del-sabor/documentation-github/login.png)

### Registro
![Registro](https://storage.googleapis.com/rutas-del-sabor/documentation-github/register.png)

### Inicio
![Inicio](https://storage.googleapis.com/rutas-del-sabor/documentation-github/home.png)

### Actividades
![Actividades](https://storage.googleapis.com/rutas-del-sabor/documentation-github/activity.png)

### Planificación de creación de rutas
![Rutas](https://storage.googleapis.com/rutas-del-sabor/documentation-github/create_route.png)

### Reseñas
![Reseñas](https://storage.googleapis.com/rutas-del-sabor/documentation-github/review.png)

### Mapa
![Mapa](https://storage.googleapis.com/rutas-del-sabor/documentation-github/map.png)



