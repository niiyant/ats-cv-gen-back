# Documentación Database

## Descripción General

  - **Nombre base de datos:**
  - **Base de Datos** (PostgreSQL)
  - **Propósito:** Guardar los inputs de los CVs de cada usuario
  

## Tablas

  ### app_user
  
  - Datos básicos del usuario
  - Tabla PARENT
  - **Campos/Columnas:** id (PK), first_name (text), last_name (text), email (text), password_hash (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo.
  
  ### cv
  
  - Datos del CV.
  - Vinculada a la tabla app_user
  - Hija de app_user, Parent del resto
  - **Campos/Columnas:** id (PK), app_user_id (FK), telephone (int), role (varchar-30), summary (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo.

  ### experience
  
  - Datos de la experiencia.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), role (varchar-30), company (text), start_date (date), end_date (date), description (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo excepto *end_date*.

  ### skill
  - Datos de las habilidades.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), title (varchar-10), level (text["basic", "intermediate", "advanced"]), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo excepto *title, level*.

  ### soft_skill
  - Datos de las habilidades blandas.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), title (varchar-15), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo excepto *title*.

 ### certification
  - Datos de las certificaciones.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), name (varchar-63), institution (varchar-63), date (date), description (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: id,  cv_id, created_at, updated_at.

### academic
  - Datos de la educación.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), title (varchar-63), institution (varchar-63), start_date (date), end_date (date), description (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo *excepto end_date* y *description*.

### profile
  - Datos de las páginas web.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), name (varchar-20), url (text), created_at (timestamptz), updated_at (timestamptz). NOT NULL: todo

### languages
  - Datos de la educación.
  - Vinculada a la tabla cv.
  - **Campos/Columnas:** id (PK), cv_id (FK), speech (varchar-30), level (text["basic", "intermediate", "advanced"]), certificate (varchar-30), created_at (timestamptz), updated_at (timestamptz). NOT NULL: id, cv_id

