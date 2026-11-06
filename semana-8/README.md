# Laboratorio N° 8: Implementación de Servicios Web con Django REST Framework

**Estudiante:** Israel Angel Huaman Huaman  
**Curso:** Desarrollo de Aplicaciones Empresariales (DAE) — Tecsup  
**Docente:** Michael Montgomery Rosell  
**Sección:** 4-C24-A  

---

## 1. Resumen y Arquitectura

Este laboratorio implementa una **API REST headless completa con Django REST Framework (DRF)** para la gestión de exámenes y cuestionarios (`quiz`), construida de forma acumulativa sobre la base del proyecto de la Semana 7 (`blog`).

### Componentes Clave:
1. **Modelos:** `Exam`, `Question`, `Choice` con relaciones relacionales y borrado en cascada.
2. **Serializadores (`ModelSerializer`):** Opciones (`Choice`) que viajan anidadas dentro de la pregunta (`nested serializer`) y examen referenciado por identificador (`id`).
3. **Validación de Negocio:** Validación estricta que exige **exactamente una opción correcta** y al menos dos opciones por pregunta.
4. **Conjunto de Vistas y Enrutadores:** `ExamViewSet`, `QuestionViewSet` y `ChoiceViewSet` expuestos mediante `DefaultRouter`, con optimización `select_related`/`prefetch_related` para evitar problemas $N+1$, filtros por examen y búsqueda textual por enunciado.
5. **Autenticación y Permisos por Rol:** Basado en tokens (`TokenAuthentication`). Dos identidades:
   * **Persona (Staff / Profesor):** Acceso total (lectura, creación, edición y eliminación `DELETE`).
   * **Agente (Grupo `agente`):** Puede leer, crear y modificar (`PATCH`/`PUT`), pero **nunca eliminar**. Devuelve `403 Forbidden` en intentos de eliminación.
   * **Usuario sin rol / no autenticado:** Solo lectura si está autenticado; `401 Unauthorized` si no presenta token.
6. **Contrato OpenAPI:** Documentado e interactivo mediante `drf-spectacular` en `/api/docs/` y `/api/schema/`.
7. **Cliente de Consola Headless (`quizctl.py`):** Cliente de terminal con códigos de salida leíbles por máquina (0=OK, 2=Validación, 3=Prohibido/No autorizado, 4=No encontrado, 5=Error de servidor).
8. **Pasarela de Seguridad del Agente (`agent/`):** Frontera cerrada con clasificación de riesgo:
   * **R0:** Lectura (se ejecuta de inmediato).
   * **R1:** Creación (se ejecuta con token del agente).
   * **R2:** Destructivo (nunca se ejecuta automáticamente; genera un plan con hash criptográfico que requiere aprobación humana explícita con token de staff).
   * **Registro de Auditoría:** Todas las decisiones se guardan en `agent_audit.jsonl`.

---

## 2. Puesta en Marcha

```bash
cd semana-8

# 1. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate          # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate

# 4. Sembrar datos fijos y generar tokens
python manage.py seed_quiz
```

`seed_quiz` creará 2 exámenes con 8 preguntas y los tokens fijos para pruebas:
```bash
export QUIZ_TOKEN_HUMANO=8e5c17acbac92ca48a7cf1cdaa3b7f0d90c88f9d
export QUIZ_TOKEN_AGENTE=18cba0de98b06a1f9b6db1fd5784defe3330a89b
```

---

## 3. Tabla Completa de la API

| Recurso | Dirección (Endpoint) | Método | Descripción | Código | Cuerpo de Solicitud (Ejemplo) | Respuesta Esperada (Ejemplo) |
|---|---|:---:|---|:---:|---|---|
| **Exams** | `/api/exams/` | `GET` | Listar exámenes con conteo de preguntas | `200 OK` | *(Vacío)* | `{"count": 2, "results": [{"id": 1, "title": "Django · ORM", "question_count": 4}]}` |
| **Exams** | `/api/exams/{id}/` | `GET` | Detalle de un examen | `200 OK` | *(Vacío)* | `{"id": 1, "title": "Django · ORM", "question_count": 4, "created_at": "..."}` |
| **Exams** | `/api/exams/` | `POST` | Crear nuevo examen | `201 Created` | `{"title": "Django REST Framework"}` | `{"id": 3, "title": "Django REST Framework", "question_count": 0, ...}` |
| **Exams** | `/api/exams/{id}/` | `PATCH` | Modificar examen | `200 OK` | `{"title": "Django ORM Avanzado"}` | `{"id": 1, "title": "Django ORM Avanzado", ...}` |
| **Exams** | `/api/exams/{id}/` | `DELETE` | Eliminar examen (solo staff) | `204 No Content` | *(Vacío)* | *(Cuerpo vacío)* |
| **Questions** | `/api/questions/` | `GET` | Listar preguntas paginadas (5 por página) | `200 OK` | *(Vacío)* | `{"count": 8, "next": "...?page=2", "results": [...]}` |
| **Questions** | `/api/questions/?exam=1` | `GET` | Filtrar preguntas por examen | `200 OK` | *(Vacío)* | `{"count": 4, "results": [...]}` |
| **Questions** | `/api/questions/?search=ORM` | `GET` | Búsqueda por texto en enunciado | `200 OK` | *(Vacío)* | `{"count": 2, "results": [...]}` |
| **Questions** | `/api/questions/{id}/` | `GET` | Detalle de pregunta con opciones anidadas | `200 OK` | *(Vacío)* | `{"id": 1, "exam": 1, "text": "...", "choices": [{"id": 1, "text": "...", "is_correct": true}]}` |
| **Questions** | `/api/questions/` | `POST` | Crear pregunta con opciones anidadas | `201 Created` | `{"exam": 1, "text": "¿Qué es REST?", "choices": [{"text": "Un estilo:ok", "is_correct": true}, {"text": "Un lenguaje", "is_correct": false}]}` | `{"id": 9, "exam": 1, "text": "¿Qué es REST?", "choices": [...]}` |
| **Questions** | `/api/questions/{id}/` | `PATCH` | Actualizar texto de pregunta | `200 OK` | `{"text": "¿Qué es una API RESTful?"}` | `{"id": 1, "text": "¿Qué es una API RESTful?", ...}` |
| **Questions** | `/api/questions/{id}/` | `DELETE` | Eliminar pregunta (solo staff) | `204 No Content` | *(Vacío)* | *(Cuerpo vacío)* |
| **Choices** | `/api/choices/` | `GET` | Listar opciones individuales | `200 OK` | *(Vacío)* | `{"count": 32, "results": [{"id": 1, "text": "...", "is_correct": true}]}` |

---

## 4. Evidencias de Pruebas HTTP y Códigos de Estado

### A. Las 5 Operaciones CRUD Principales

1. **Listar (`GET /api/questions/`)**  
   * **Código devuelto:** `200 OK`  
   * Retorna las preguntas con paginación (`PAGE_SIZE = 5`) y las opciones anidadas en cada resultado.
2. **Detalle (`GET /api/questions/1/`)**  
   * **Código devuelto:** `200 OK`  
   * Retorna el objeto único con su lista de `choices`.
3. **Crear (`POST /api/questions/`)**  
   * **Código devuelto:** `201 Created`  
   * Inserta en base de datos la pregunta y sus opciones asociadas atómicamente (`transaction.atomic`).
4. **Modificar parcialmente (`PATCH /api/questions/1/`)**  
   * **Código devuelto:** `200 OK`  
   * Actualiza únicamente los campos suministrados sin alterar el resto.
5. **Eliminar (`DELETE /api/questions/1/`)**  
   * **Código devuelto con token de staff:** `204 No Content` (eliminación exitosa).  
   * **Código devuelto con token de agente:** `403 Forbidden` (el servidor deniega la acción destructiva).  
   * **Código devuelto sin token:** `401 Unauthorized`.

---

### B. Los Tres Errores a Propósito (Paso 9 del Procedimiento)

| Caso de Error Provocado | Causa | Código HTTP | Mensaje de Error de la API |
|---|---|:---:|---|
| **1. Campo obligatorio ausente** | Se envía un `POST /api/questions/` omitiendo el campo `text`. | `400 Bad Request` | `{"text": ["Este campo es requerido."]}` |
| **2. Tipo de dato incorrecto** | Se envía `"exam": "no-es-un-numero"` (cadena en lugar de entero). | `400 Bad Request` | `{"exam": ["Tipo de clave primaria incorrecta. Se esperaba un entero."]}` |
| **3. Validación de opción correcta** | Se envía una pregunta con **dos opciones marcadas como correctas** (`is_correct: true`). | `400 Bad Request` | `{"choices": ["Debe haber exactamente una opción correcta."]}` |

---

## 5. Pruebas Automatizadas

El proyecto incluye una suite de **61 pruebas automatizadas** que validan la API, los contratos, los permisos de roles, el cliente `quizctl` y la pasarela del agente:

```bash
python manage.py test quiz
```

**Resultado:**
```text
Creating test database for alias 'default'...
.............................................................
----------------------------------------------------------------------
Ran 61 tests in 2.393s

OK
Destroying test database for alias 'default'...
Found 61 test(s).
System check identified no issues (0 silenced).
```
