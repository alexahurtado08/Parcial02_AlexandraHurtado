# Parcial02_AlexandraHurtado

Este programa implementa un microservicio en Flask (Python) que recibe un número por la URL y devuelve una respuesta JSON con:
- El número recibido  
- Su factorial  
- Una etiqueta par o impar según corresponda al número ingresado por URL
- 
# Ejecución del microservicio (sin Docker)

Nota: No es necesario tener Docker instalado. El proyecto se ejecuta directamente con Python.

Requisitos

Python 3.8 o superior

Flask (se instalará automáticamente con pip)

### Instalación y ejecución

Clona el repositorio o descarga los archivos del proyecto.
```bash
git clone https://github.com/alexahurtado08/Parcial02_AlexandraHurtado.git 
```

Abre una terminal en la carpeta del proyecto y ejecuta los siguientes comandos:

```bash
 
python -m venv venv
venv\Scripts\activate
pip install Flask
python app.py

```

Abre tu navegador y accede a:

http://localhost:8080/factorial/<numero>


Ejemplo:

http://localhost:8080/factorial/7



# Ejecuicón del microservcicio (con Docker)

Requisitos

Python 3.8 o superior

Flask (se instalará automáticamente con pip)

Docker installado en tu pc, puedes comprobarlo con el comando 

```bash
docker -- version

```

### Instalación y ejecución:

Clona el repositorio o descarga los archivos del proyecto.

```bash
git clone https://github.com/alexahurtado08/Parcial02_AlexandraHurtado.git 
```

Ejecuta el siguiente comando en la terminal para la construcción de la imagen: 

```bash
 
docker build -t microservicio-factorial .
docker run -p 8080:8080 microservicio-factorial
```

Abre tu navegador y accede a:

http://localhost:8080/factorial/<numero>


Ejemplo:

http://localhost:8080/factorial/7



# Preguntas de Analisis:

1. Explique cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.
Actualmente el programa ya cuenta con un Dockerfile

Si el microservicio tuviera que comicarse con el historial de calculos lo primero sería tener en cuenta los 2 microservicios que tendriamos 

1. Calculo de factoriales
   
3. Guardar y consultar el historial.
   
Para la comunicación entre servicios deberíamos usar peticiones de tipo REST entre estos servicios, es decir cuando el servicio 1 calcule un factorial se envia un POST  a 2

También se debería tener en cuenta que ambos servicios deben tener bd diferentes, es decir, la bd del microservicio 2 sería aislada del servicio 1. 

También deberíamos proceder a la creación de un archivo compose.yml para definir ambos servicios, la bd y las conexiones o redes entre ellos.



