# Mundo Música - Blog de Música

¡Bienvenido a Mundo Música, tu destino musical definitivo! Este blog, desarrollado en Django y respaldado por una base de datos SQLite3, está diseñado para ofrecer una experiencia única para amantes de la música de todas partes del mundo. A continuación, encontrarás toda la información necesaria para poner en marcha y entender el funcionamiento de Mundo Música.

## Instalación y Configuración

1. **Requisitos Previos:**

   - Asegúrate de tener Python instalado en tu sistema. Si no lo tienes, puedes descargarlo [aquí](https://www.python.org/downloads/).

2. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/tuusuario/mundo-musica.git
   cd mundo-musica
   ```

3. **Configuración del Entorno Virtual:**

   ```bash
   python -m venv env
   source env/bin/activate
   ```

4. **Instalación de Dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Aplicar Migraciones:**

   ```bash
   python manage.py migrate
   ```

6. **Crear Superusuario (Admin):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el Servidor:**

   ```bash
   python manage.py runserver
   ```

8. **Acceder a la Aplicación:**
   Visita [http://localhost:8000/](http://localhost:8000/) en tu navegador.

## Funcionalidades Principales

### Roles de Usuario

1. **Admin:**

   - Puede crear categorías.
   - Puede habilitar o deshabilitar colaboradores cambiando el campo `role` en la base de datos.
   - Tiene acceso total a la gestión del blog.

2. **Colaborador:**

   - Puede crear, editar y eliminar posts.
   - Puede eliminar comentarios de usuarios.

3. **Usuario:**
   - Puede crear, editar y eliminar sus propios comentarios.
   - Puede navegar, leer y comentar en los posts del blog.

## Estructura del Proyecto

- **`mundo_musica/`**: Contiene la configuración principal del proyecto Django.
- **`core/`**: Aplicación principal del blog.
- **`posts/`**: Lógica para administrar los posts.
- **`usuarios/`**: App de usuarios y modelos para los mismos.
- **`comentarios/`**: Lógica para el manejo de los comentarios.
- **`templates/`**: Plantillas HTML.
- **`env/`**: Entorno virtual.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

¡Disfruta de tu experiencia en Mundo Música! 🎶🌍
