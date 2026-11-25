# Sistema de Gestión de Clínicas Veterinarias - SQLAlchemy ORM
## Descripción del proyecto
Este proyecto fue desarrollado como parte de la actividad práctica de la asignatura **Desarrollo Basado en Plataformas Web**.
El objetivo de este proyecto es aplicar los conceptos de Object Relational Mapping (ORM) mediante SQLAlchemy en Python, permitiendo gestionar la información de una base de datos relacional utilizando clases y objetos.
La aplicación representa la gestión de una red de clínicas veterinarias, donde se administra información de clínicas, consultorios, veterinarios e historias clínicas de mascotas.

## Tecnologías utilizadas
- Lenguaje de programación: **Python**
- ORM: **SQLAlchemy**
- Base de datos: **SQLite**
- Entorno de desarrollo: **Visual Studio Code**

## Modelo de datos
El sistema está compuesto por las siguientes entidades:

### Clínica
Almacena la información principal de cada clínica veterinaria:
- Identificador
- Nombre comercial
- Dirección
- Médico veterinario responsable

### Consultorio
Representa los consultorios pertenecientes a cada clínica:
- Identificador
- Nombre o número del consultorio
- Especialidad principal

### Veterinario
Contiene la información de los profesionales que trabajan en los consultorios:
- Identificador
- Nombres y apellidos
- Correo electrónico
- Número de licencia profesional

### Historia Clínica
Registra la atención médica realizada a las mascotas:
- Identificador
- Fecha de atención
- Diagnóstico
- Tratamiento
- Nombre de la mascota

## Relaciones entre entidades
La estructura del sistema se maneja mediante relaciones ORM:
- Una Clínica puede tener varios Consultorios.
- Un Consultorio pertenece a una sola Clínica.
- Un Consultorio puede tener varios Veterinarios.
- Un Veterinario pertenece a un solo Consultorio.
- Un Veterinario puede generar varias Historias Clínicas.
- Una Historia Clínica pertenece a un único Veterinario.

## Estructura del proyecto
La organización de archivos del proyecto es la siguiente:

Desarrollo Basado en Plataformas web/
│
├── configuracion.py
│   └── Configuración de conexión con SQLite
│
├── crear_base_entidades.py
│   └── Creación de entidades ORM y tablas
│
├── poblar_base.py
│   └── Inserción de datos iniciales
│
├── consulta_all.py
│   └── Consulta utilizando all()
│
├── consulta_filter.py
│   └── Consulta utilizando filter()
│
├── consulta_order_by.py
│   └── Consulta utilizando order_by()
│
├── consulta_or.py
│   └── Consulta utilizando or_()
│
├── consulta_and.py
│   └── Consulta utilizando and_()
│
├── veterinaria.db
│   └── Base de datos SQLite
│
└── README.md
    └── Atrchivo de documentación del proyecto

## Instalación y ejecución del proyecto
Para ejecutar correctamente el proyecto se deben seguir los siguientes pasos:

### 1. Instalar dependencias: 
Instalar la librería SQLAlchemy mediante el siguiente comando:
pip install sqlalchemy

### 2. Crear la base de datos: 
Ejecutar el archivo encargado de crear las entidades y tablas mediante SQLAlchemy:
python crear_base_entidades.py

### Resultado:
Este proceso genera la base de datos SQLite llamada: 
veterinaria.db

### 3. Insertar información inicial:
Ejecutar el archivo para ingresar datos de prueba:
python poblar_base.py

### 4. Ejecutar consultas:
El proyecto contiene diferentes archivos para demostrar el uso de consultas ORM:
python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py

## Consultas implementadas
Dentro del proyecto se aplicaron diferentes métodos de consulta utilizando SQLAlchemy ORM:
- **all():** Permite obtener todos los registros almacenados en una entidad. En este proyecto se utiliza para mostrar las clínicas registradas y la cantidad de historias clínicas asociadas a cada una.
- **filter():** Permite realizar búsquedas aplicando condiciones específicas sobre los datos almacenados.
- **order_by():** Permite organizar los resultados obtenidos según un atributo determinado.
- **or_():** Permite realizar consultas donde se cumpla una condición u otra dentro de la búsqueda.
- **and_():** Permite realizar consultas donde se deben cumplir varias condiciones al mismo tiempo.

## Conclusión
El desarrollo de este proyecto permitió aplicar los conceptos de Object Relational Mapping (ORM) mediante la librería SQLAlchemy en Python, facilitando la conexión entre una aplicación y una base de datos relacional.
Mediante la creación de entidades, relaciones y consultas se logró representar la gestión de una red de clínicas veterinarias, organizando la información de manera estructurada y eficiente.
El uso de ORM permite mejorar la organización del código, facilitar el mantenimiento del sistema y realizar operaciones con bases de datos utilizando objetos de Python en lugar de consultas SQL tradicionales.
Durante el desarrollo se pudo comprender cómo SQLAlchemy facilita la comunicación entre Python y la base de datos, evitando trabajar directamente con instrucciones SQL para cada operación.

## Autor
Brigitte Gonzabay Reyes  
Carrera: Tecnología de la Información  
Universidad Técnica Particular de Loja (UTPL)