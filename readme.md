# BackEnd Trabajo con Juanes

## Descripción
Este proyecto es un back para conectar y realizar consultas para el frondEnd de manejo de usuarios, registros, etc.


## Configuración del Entorno de Desarrollo

### Creación de un .Env
Se debe crear un env para guardar las variables de entorno que en este caso seria de esta manera:
 ```bash
    DB_USERNAME= Nombre del usuario de bd
    DB_PASSWORD= contraseña
    DB_SERVER= servidor
    DB_DATABASE= base de datos
```


### Creación de un Entorno Virtual en Python
Se recomienda usar un entorno virtual para manejar las dependencias del proyecto de forma aislada.

1. **Instalación de Virtualenv**:
    ```bash
    pip install virtualenv
    ```

2. **Creación del Entorno Virtual**:
    En el directorio del proyecto, ejecuta:
    ```bash
    python -m venv .venv
    ```

3. **Activación del Entorno Virtual**:
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En Unix o MacOS:
      ```bash
      source venv/bin/activate
      ```

### Instalación de Dependencias
Con el entorno virtual activado, instala las dependencias:
```bash
    pip install -r requirements.txt
```

### Ejecución de la Aplicación
Para ejecutar la aplicación:
```bash
    uvicorn main:app --reload
```
