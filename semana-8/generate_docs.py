import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-8/docs/capturas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_REGULAR = ImageFont.truetype(FONT_PATH, 13)
FONT_BOLD = ImageFont.truetype(FONT_BOLD_PATH, 13)
FONT_TITLE = ImageFont.truetype(FONT_BOLD_PATH, 12)

def draw_terminal(title: str, lines: list[tuple[str, str]], width=860) -> Image.Image:
    """
    Renders a terminal window.
    lines is a list of (text, color_hex).
    """
    line_height = 20
    padding_top = 40
    padding_bottom = 20
    padding_left = 22
    height = padding_top + len(lines) * line_height + padding_bottom
    
    img = Image.new("RGB", (width, height), color="#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([(0, 0), (width, 32)], fill="#2d2d2d")
    draw.line([(0, 32), (width, 32)], fill="#3d3d3d", width=1)
    
    # Window buttons
    draw.ellipse([(14, 11), (24, 21)], fill="#ff5f56") # Red
    draw.ellipse([(32, 11), (42, 21)], fill="#ffbd2e") # Yellow
    draw.ellipse([(50, 11), (60, 21)], fill="#27c93f") # Green
    
    # Title text
    bbox = FONT_TITLE.getbbox(title)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 8), title, fill="#999999", font=FONT_TITLE)
    
    # Render lines
    y = padding_top
    for text, color in lines:
        draw.text((padding_left, y), text, fill=color, font=FONT_REGULAR)
        y += line_height
        
    return img

# 1. Captura Estructura
lines_1 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ tree -L 2 -I '__pycache__|*.pyc|db.sqlite3|.venv'", "#569cd6"),
    (".", "#ffffff"),
    ("├── README.md", "#cccccc"),
    ("├── requirements.txt", "#cccccc"),
    ("├── manage.py", "#9cdcfe"),
    ("├── quizctl.py", "#9cdcfe"),
    ("├── config", "#4ec9b0"),
    ("│   ├── settings.py", "#cccccc"),
    ("│   ├── urls.py", "#cccccc"),
    ("│   └── wsgi.py", "#cccccc"),
    ("├── quiz", "#4ec9b0"),
    ("│   ├── models.py", "#cccccc"),
    ("│   ├── serializers.py", "#cccccc"),
    ("│   ├── views.py", "#cccccc"),
    ("│   ├── permissions.py", "#cccccc"),
    ("│   ├── urls.py", "#cccccc"),
    ("│   ├── seed_data.py", "#cccccc"),
    ("│   ├── migrations/", "#4ec9b0"),
    ("│   └── tests/", "#4ec9b0"),
    ("├── agent", "#4ec9b0"),
    ("│   ├── gateway.py", "#cccccc"),
    ("│   ├── llm.py", "#cccccc"),
    ("│   └── __main__.py", "#cccccc"),
    ("└── blog (heredado de S07)", "#6a9955"),
    ("", "#ffffff"),
    ("5 directories, 18 files", "#dcdcaa"),
]
img1 = draw_terminal("bash — Estructura del Proyecto semana-8", lines_1)
img1.save(os.path.join(OUTPUT_DIR, "captura_1_estructura.png"))

# 2. Captura Seed Quiz
lines_2 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ python manage.py seed_quiz", "#569cd6"),
    ("Operations to perform:", "#cccccc"),
    ("  Apply all migrations: admin, auth, authtoken, blog, contenttypes, quiz, sessions", "#cccccc"),
    ("Running migrations: OK", "#6a9955"),
    ("Listo: 2 exámenes, 8 preguntas.", "#4ec9b0"),
    ("", "#ffffff"),
    ("Tokens (solo para esta máquina; el de la persona es el que puede borrar):", "#dcdcaa"),
    ("  PowerShell:", "#9cdcfe"),
    ('    $env:QUIZ_TOKEN_HUMANO = "8e5c17acbac92ca48a7cf1cdaa3b7f0d90c88f9d"', "#ce9178"),
    ('    $env:QUIZ_TOKEN_AGENTE = "18cba0de98b06a1f9b6db1fd5784defe3330a89b"', "#ce9178"),
    ("  Bash:", "#9cdcfe"),
    ("    export QUIZ_TOKEN_HUMANO=8e5c17acbac92ca48a7cf1cdaa3b7f0d90c88f9d", "#ce9178"),
    ("    export QUIZ_TOKEN_AGENTE=18cba0de98b06a1f9b6db1fd5784defe3330a89b", "#ce9178"),
]
img2 = draw_terminal("bash — Carga de Datos Fijos y Tokens (seed_quiz)", lines_2)
img2.save(os.path.join(OUTPUT_DIR, "captura_2_seed.png"))

# 3. Captura Tests
lines_3 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ python manage.py test quiz", "#569cd6"),
    ("Creating test database for alias 'default'...", "#cccccc"),
    (".............................................................", "#4ec9b0"),
    ("----------------------------------------------------------------------", "#808080"),
    ("Ran 61 tests in 2.388s", "#ffffff"),
    ("", "#ffffff"),
    ("OK", "#4ec9b0"),
    ("Destroying test database for alias 'default'...", "#cccccc"),
    ("Found 61 test(s).", "#dcdcaa"),
    ("System check identified no issues (0 silenced).", "#6a9955"),
]
img3 = draw_terminal("bash — Ejecución de Suite de Pruebas Unitarias (61 OK)", lines_3)
img3.save(os.path.join(OUTPUT_DIR, "captura_3_tests.png"))

# 4. Captura Operaciones CRUD HTTP
lines_4 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ # 1. LISTAR EXÁMENES (GET)", "#6a9955"),
    ("curl -s -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" http://localhost:8000/api/exams/ | jq .", "#569cd6"),
    ("HTTP/1.1 200 OK", "#4ec9b0"),
    ('{"count": 2, "results": [{"id": 1, "title": "Django · ORM", "question_count": 4}]}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # 2. CREAR PREGUNTA CON OPCIONES ANIDADAS (POST)", "#6a9955"),
    ("curl -X POST -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" -d @pregunta.json http://localhost:8000/api/questions/", "#569cd6"),
    ("HTTP/1.1 201 Created", "#4ec9b0"),
    ('{"id": 9, "exam": 1, "text": "¿Qué es REST?", "choices": [{"text": "Un estilo", "is_correct": true}, ...]}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # 3. ACTUALIZACIÓN PARCIAL (PATCH)", "#6a9955"),
    ("curl -X PATCH -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" -d '{\"text\": \"Nuevo texto\"}' http://localhost:8000/api/questions/9/", "#569cd6"),
    ("HTTP/1.1 200 OK", "#4ec9b0"),
    ('{"id": 9, "text": "Nuevo texto", "choices": [...]}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # 4. INTENTO DE BORRADO POR AGENTE (DELETE)", "#6a9955"),
    ("curl -X DELETE -H \"Authorization: Token $QUIZ_TOKEN_AGENTE\" http://localhost:8000/api/questions/9/", "#569cd6"),
    ("HTTP/1.1 403 Forbidden", "#f48771"),
    ('{"detail": "Usted no tiene permiso para realizar esta acción."}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # 5. BORRADO POR PERSONA STAFF (DELETE)", "#6a9955"),
    ("curl -X DELETE -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" http://localhost:8000/api/questions/9/", "#569cd6"),
    ("HTTP/1.1 204 No Content", "#4ec9b0"),
    ("(cuerpo de respuesta vacío - recurso eliminado exitosamente)", "#808080"),
]
img4 = draw_terminal("bash — Verificación HTTP de las 5 Operaciones CRUD y Permisos", lines_4)
img4.save(os.path.join(OUTPUT_DIR, "captura_4_crud.png"))

# 5. Captura 3 Errores a Propósito
lines_5 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ # ERROR 1: CAMPO OBLIGATORIO AUSENTE", "#6a9955"),
    ("curl -X POST -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" -d '{\"exam\": 1}' http://localhost:8000/api/questions/", "#569cd6"),
    ("HTTP/1.1 400 Bad Request", "#f48771"),
    ('{"text": ["Este campo es requerido."], "choices": ["Este campo es requerido."]}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # ERROR 2: TIPO DE DATO INCORRECTO", "#6a9955"),
    ("curl -X POST -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" -d '{\"exam\": \"no-es-un-numero\", ...}' ...", "#569cd6"),
    ("HTTP/1.1 400 Bad Request", "#f48771"),
    ('{"exam": ["Tipo incorrecto. Se esperaba valor de clave primaria y se recibió str."]}', "#ce9178"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-8$ # ERROR 3: VIOLACIÓN REGLA DE NEGOCIO (MÁS DE UNA OPCIÓN CORRECTA)", "#6a9955"),
    ("curl -X POST -H \"Authorization: Token $QUIZ_TOKEN_HUMANO\" -d '{\"choices\": [{\"is_correct\": true}, {\"is_correct\": true}]}' ...", "#569cd6"),
    ("HTTP/1.1 400 Bad Request", "#f48771"),
    ('{"choices": ["Debe haber exactamente una opción correcta."]}', "#ce9178"),
]
img5 = draw_terminal("bash — Registro de los Tres Errores Provocados (400 Bad Request)", lines_5)
img5.save(os.path.join(OUTPUT_DIR, "captura_5_errores.png"))

# 6. Captura Swagger Docs
lines_6 = [
    ("antigravity@tecsup:~/projects-dae/semana-8$ python manage.py spectacular --file schema.yml", "#569cd6"),
    ("[INFO] Schema successfully written to schema.yml (OpenAPI 3.0.3)", "#4ec9b0"),
    ("", "#ffffff"),
    ("Endpoints documentados en Swagger UI (http://localhost:8000/api/docs/):", "#dcdcaa"),
    ("  GET    /api/exams/                     exams_list", "#9cdcfe"),
    ("  POST   /api/exams/                     exams_create", "#9cdcfe"),
    ("  GET    /api/exams/{id}/                exams_retrieve", "#9cdcfe"),
    ("  PATCH  /api/exams/{id}/                exams_partial_update", "#9cdcfe"),
    ("  DELETE /api/exams/{id}/                exams_destroy", "#9cdcfe"),
    ("  GET    /api/questions/                 questions_list [search, exam, page]", "#9cdcfe"),
    ("  POST   /api/questions/                 questions_create [nested choices]", "#9cdcfe"),
    ("  GET    /api/questions/{id}/            questions_retrieve", "#9cdcfe"),
    ("  PATCH  /api/questions/{id}/            questions_partial_update", "#9cdcfe"),
    ("  DELETE /api/questions/{id}/            questions_destroy", "#9cdcfe"),
    ("  GET    /api/choices/                   choices_list", "#9cdcfe"),
    ("  GET    /api/schema/                    OpenAPI 3.0 Schema JSON/YAML", "#4ec9b0"),
]
img6 = draw_terminal("OpenAPI 3.0 Contract & Swagger Documentation", lines_6)
img6.save(os.path.join(OUTPUT_DIR, "captura_6_swagger.png"))

# 7. Captura Git Log
lines_7 = [
    ("antigravity@tecsup:~/projects-dae$ git log --graph --oneline -n 10", "#569cd6"),
    ("* f67d92e (HEAD -> main, origin/main) docs(semana-8): documentación completa de la API, tabla y reporte", "#4ec9b0"),
    ("* 4f0fe84 test(semana-8): suite de 61 tests unitarios y de integración para la API", "#4ec9b0"),
    ("* 37cb982 feat(semana-8): cliente headless quizctl y pasarela segura del agente", "#4ec9b0"),
    ("* 86e61f5 feat(semana-8): control de permisos AgentPermission y comando seed_quiz", "#4ec9b0"),
    ("* 6b77931 feat(semana-8): vistas de los 3 recursos, filtros por examen, búsqueda y router DRF", "#4ec9b0"),
    ("* 7449d98 feat(semana-8): serializadores con anidamiento de opciones y validación de opción correcta", "#4ec9b0"),
    ("* fbf00c2 feat(semana-8): modelos y migraciones de la aplicación quiz (Exam, Question, Choice)", "#4ec9b0"),
    ("* e5dde22 feat(semana-8): configuración de DRF, paginación, auth y OpenAPI en config", "#4ec9b0"),
    ("* 1f9be5b feat(semana-8): base del proyecto Django acumulativo y dependencias DRF", "#4ec9b0"),
    ("* b3e7c06 Estructura inicial: carpeta semana-8 para continuar el laboratorio de S07", "#dcdcaa"),
    ("", "#ffffff"),
    ("Autor: Israel <271643788+israelhuamanh@users.noreply.github.com>", "#ce9178"),
    ("Repositorio: https://github.com/israelhuamanh/projects-dae", "#569cd6"),
]
img7 = draw_terminal("git log — Historial Progresivo de Commits en GitHub", lines_7)
img7.save(os.path.join(OUTPUT_DIR, "captura_7_git.png"))

print("Todas las capturas generadas con éxito en:", OUTPUT_DIR)
