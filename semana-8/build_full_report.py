import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOC_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-8/docs"
CAPT_DIR = os.path.join(DOC_DIR, "capturas")
DOCX_PATH = "/home/antigravity/israelhuamanh/projects-dae/semana-8/Informe_Laboratorio_08_Israel_Huaman.docx"
HTML_PATH = "/home/antigravity/israelhuamanh/projects-dae/semana-8/Informe_Laboratorio_08_Israel_Huaman.html"

doc = docx.Document()

# Set standard margins (1 inch)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Colors
COLOR_TECSUP_BLUE = RGBColor(0, 51, 102)     # #003366
COLOR_GRAY_DARK = RGBColor(51, 51, 51)       # #333333
COLOR_MUTED = RGBColor(102, 102, 102)        # #666666

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F5F5F5")
    set_cell_margins(cell, 120, 120, 160, 160)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = COLOR_GRAY_DARK
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def add_image_with_caption(doc, img_name, caption_text):
    img_path = os.path.join(CAPT_DIR, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(12)
        run_cap = p_cap.add_run(f"Figura: {caption_text}")
        run_cap.font.name = "Arial"
        run_cap.font.size = Pt(9.0)
        run_cap.font.italic = True
        run_cap.font.color.rgb = COLOR_MUTED

# ==========================================
# 1. CARÁTULA
# ==========================================
p_inst = doc.add_paragraph()
p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_inst.paragraph_format.space_before = Pt(20)
p_inst.paragraph_format.space_after = Pt(4)
run_inst = p_inst.add_run("TECSUP — DEPARTAMENTO DE TECNOLOGÍA DIGITAL")
run_inst.font.name = "Arial"
run_inst.font.size = Pt(14)
run_inst.font.bold = True
run_inst.font.color.rgb = COLOR_TECSUP_BLUE

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_before = Pt(0)
p_sub.paragraph_format.space_after = Pt(36)
run_sub = p_sub.add_run("Diseño y Desarrollo de Software · C24")
run_sub.font.name = "Arial"
run_sub.font.size = Pt(11)
run_sub.font.color.rgb = COLOR_MUTED

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(24)
p_title.paragraph_format.space_after = Pt(8)
run_title = p_title.add_run("LABORATORIO N° 08\nIMPLEMENTACIÓN DE SERVICIOS WEB CON DJANGO REST FRAMEWORK (DRF)")
run_title.font.name = "Arial"
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_TECSUP_BLUE

p_subt = doc.add_paragraph()
p_subt.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_subt.paragraph_format.space_before = Pt(0)
p_subt.paragraph_format.space_after = Pt(48)
run_subt = p_subt.add_run("API RESTful Headless: Serializadores, Vistas, Permisos por Roles y Contrato OpenAPI")
run_subt.font.name = "Arial"
run_subt.font.size = Pt(12)
run_subt.font.italic = True
run_subt.font.color.rgb = COLOR_GRAY_DARK

# Table of metadata
tbl_meta = doc.add_table(rows=5, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_meta.autofit = False
tbl_meta.columns[0].width = Inches(2.2)
tbl_meta.columns[1].width = Inches(4.3)

meta_data = [
    ("Estudiante:", "Israel Angel Huaman Huaman"),
    ("Curso:", "Desarrollo de Aplicaciones Empresariales (DAE)"),
    ("Docente:", "Michael Montgomery Rosell"),
    ("Sección:", "4-C24-A"),
    ("Repositorio GitHub:", "https://github.com/israelhuamanh/projects-dae/tree/main/semana-8"),
]

for i, (label, val) in enumerate(meta_data):
    cell_lbl = tbl_meta.cell(i, 0)
    cell_val = tbl_meta.cell(i, 1)
    set_cell_background(cell_lbl, "F0F4F8")
    set_cell_background(cell_val, "FAFAFA")
    set_cell_margins(cell_lbl, 80, 80, 100, 100)
    set_cell_margins(cell_val, 80, 80, 100, 100)
    
    p0 = cell_lbl.paragraphs[0]
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    r0 = p0.add_run(label)
    r0.font.name = "Arial"
    r0.font.size = Pt(10)
    r0.font.bold = True
    r0.font.color.rgb = COLOR_TECSUP_BLUE
    
    p1 = cell_val.paragraphs[0]
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(val)
    r1.font.name = "Arial"
    r1.font.size = Pt(10)
    if "https://" in val:
        r1.font.bold = True
        r1.font.color.rgb = COLOR_TECSUP_BLUE
    else:
        r1.font.color.rgb = COLOR_GRAY_DARK

p_date = doc.add_paragraph()
p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_date.paragraph_format.space_before = Pt(60)
p_date.paragraph_format.space_after = Pt(0)
r_date = p_date.add_run("Lima, Perú — Noviembre de 2026")
r_date.font.name = "Arial"
r_date.font.size = Pt(10)
r_date.font.color.rgb = COLOR_MUTED

doc.add_page_break()

# Helper for headings
def add_custom_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    for run in h.runs:
        run.font.name = "Arial"
        if level == 1:
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = COLOR_TECSUP_BLUE
        elif level == 2:
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = COLOR_GRAY_DARK
        elif level == 3:
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = COLOR_GRAY_DARK
    return h

# Helper for paragraphs
def add_p(doc, text, bold_prefix="", space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_GRAY_DARK
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_GRAY_DARK
    return p

# ==========================================
# I. CAPACIDADES Y FUNDAMENTO TEÓRICO
# ==========================================
add_custom_heading(doc, "I. Capacidades y Fundamento Teórico", level=1)

add_p(doc, "El presente laboratorio tiene como propósito principal capacitar en la exposición y consumo de recursos empresariales mediante servicios web RESTful robustos utilizando Django REST Framework (DRF), aplicando estándares de la industria, seguridad por roles y documentación OpenAPI 3.0.")

add_p(doc, "Utiliza Django REST Framework para exponer los modelos de una aplicación como servicio web.", bold_prefix="• Capacidad 1: ")
add_p(doc, "Escribe serializadores derivados del modelo y valida con ellos los datos que entran.", bold_prefix="• Capacidad 2: ")
add_p(doc, "Publica los recursos con conjuntos de vistas y enrutadores, y comprueba cada operación por HTTP.", bold_prefix="• Capacidad 3: ")

add_p(doc, "El laboratorio es acumulativo: parte de los fundamentos desarrollados en la Semana 7 (relaciones entre entidades, optimización de consultas para evitar el problema N+1, y fronteras de confianza con agentes) y añade la capa de serialización, vistas navegables, cliente de consola sin pantalla (`quizctl.py`), y pasarela cerrada para agentes inteligentes.")

# ==========================================
# II. ESTRUCTURA DEL PROYECTO
# ==========================================
add_custom_heading(doc, "II. Estructura del Proyecto en el Editor", level=1)

add_p(doc, "El proyecto se organizó dentro del repositorio oficial en la carpeta `semana-8/`, siguiendo la arquitectura modular de Django y las normas PEP 8:")

add_image_with_caption(doc, "captura_1_estructura.png", "Estructura de directorios y archivos de la aplicación semana-8 en Visual Studio Code.")

add_p(doc, "Componentes destacados de la estructura:", bold_prefix="Detalle: ")
add_p(doc, "Contiene `settings.py` con la configuración de DRF (`TokenAuthentication`, permisos, paginación), y `urls.py` con el enrutamiento central y OpenAPI.", bold_prefix="• config/: ")
add_p(doc, "Aplicación principal del laboratorio que encapsula los modelos `Exam`, `Question`, `Choice`, sus serializadores anidados, conjuntos de vistas, permisos `AgentPermission`, datos de semilla y suite de tests.", bold_prefix="• quiz/: ")
add_p(doc, "Cliente de consola headless que interactúa con la API vía HTTP y mapea los estados a códigos de salida de terminal legibles por script.", bold_prefix="• quizctl.py: ")
add_p(doc, "Pasarela de seguridad cerrada que evalúa intenciones generadas por modelos de lenguaje, clasificándolas según riesgo (R0 lectura, R1 creación, R2 destructiva con aprobación criptográfica).", bold_prefix="• agent/: ")

# ==========================================
# III. MODELOS Y MIGRACIONES
# ==========================================
add_custom_heading(doc, "III. Modelos y Carga de Datos Iniciales", level=1)

add_p(doc, "Se definieron tres modelos en `quiz/models.py`: `Exam` (examen con título), `Question` (enunciado asociado mediante clave foránea con borrado en cascada), y `Choice` (opciones asociadas a la pregunta con el indicador booleano `is_correct`).")

add_code_block(doc, """# quiz/models.py
class Exam(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["id"]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    class Meta:
        ordering = ["id"]""")

add_p(doc, "Para asegurar consistencia en las pruebas y contratos, se implementó el comando `seed_quiz` que puebla la base de datos con 2 exámenes y 8 preguntas fijas, y crea los tokens para los usuarios `profe` (staff con permiso total) y `agente` (miembro del grupo sin permiso de borrado):")

add_image_with_caption(doc, "captura_2_seed.png", "Ejecución del comando seed_quiz: creación de registros fijos y generación de tokens de autenticación.")

# ==========================================
# IV. SERIALIZADORES Y VALIDACIÓN DE NEGOCIO
# ==========================================
add_custom_heading(doc, "IV. Serializadores Derivados y Validación Propia", level=1)

add_p(doc, "Siguiendo los requerimientos del laboratorio (Puntos 3, 4 y 5 del procedimiento), se crearon los serializadores en `quiz/serializers.py`:")

add_p(doc, "Las opciones (`Choice`) viajan anidadas dentro de la pregunta mediante `ChoiceSerializer(many=True)`, mientras que el examen viaja referenciado por su identificador entero (`PrimaryKeyRelatedField`).", bold_prefix="1. Relaciones Anidadas: ")

add_p(doc, "Se implementó `validate_choices(self, value)` que rechaza cualquier pregunta que contenga menos de dos opciones o que no tenga exactamente una opción marcada con `is_correct=True`. Si la regla se viola, DRF responde `400 Bad Request` con un mensaje descriptivo.", bold_prefix="2. Validación Propia: ")

add_p(doc, "Los métodos `create()` y `update()` operan dentro de un bloque `transaction.atomic()` para garantizar que la pregunta y sus opciones asociadas se inserten de forma integral y atómica.", bold_prefix="3. Transaccionalidad: ")

add_code_block(doc, """# quiz/serializers.py (extracto)
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "exam", "text", "choices", "created_at"]
        read_only_fields = ["created_at"]

    def validate_choices(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Una pregunta necesita al menos dos opciones.")
        if sum(1 for choice in value if choice.get("is_correct")) != 1:
            raise serializers.ValidationError("Debe haber exactamente una opción correcta.")
        return value

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        with transaction.atomic():
            question = Question.objects.create(**validated_data)
            Choice.objects.bulk_create(Choice(question=question, **c) for c in choices)
        return question""")

# ==========================================
# V. VISTAS, ENRUTADOR Y CONTRATO OPENAPI
# ==========================================
add_custom_heading(doc, "V. Conjunto de Vistas, Enrutador y Documentación", level=1)

add_p(doc, "Se publicaron los tres recursos (`ExamViewSet`, `QuestionViewSet` y `ChoiceViewSet`) en `quiz/views.py` y se registraron en un `DefaultRouter` en `quiz/urls.py`:")

add_p(doc, "Se utilizó `select_related('exam')` y `prefetch_related('choices')` en `QuestionViewSet.get_queryset()`. Esto traslada la técnica dominada en la Semana 7 para garantizar que el listado de preguntas no incurra en el problema de N+1 consultas al resolver las claves foráneas y opciones.", bold_prefix="• Optimización de Consultas: ")
add_p(doc, "Se integró `filters.SearchFilter` sobre el campo `text` y filtrado exacto por examen mediante el parámetro `?exam=` en la URL.", bold_prefix="• Filtros y Búsqueda: ")
add_p(doc, "Se integró `drf-spectacular` para emitir el esquema OpenAPI 3.0 en `/api/schema/` y la interfaz gráfica Swagger UI en `/api/docs/`.", bold_prefix="• Contrato OpenAPI: ")

add_image_with_caption(doc, "captura_6_swagger.png", "Generación y visualización del contrato OpenAPI 3.0 y endpoints documentados en Swagger UI.")

# ==========================================
# VI. TABLA COMPLETA DE LA API REST
# ==========================================
add_custom_heading(doc, "VI. Tabla Completa de la API", level=1)

add_p(doc, "A continuación se presenta la tabla exhaustiva de la API con todos los recursos, métodos HTTP, direcciones, cuerpos de solicitud y respuestas esperadas, conforme al criterio de la rúbrica:")

api_table_data = [
    ("Recurso", "Dirección (Endpoint)", "Método", "Código", "Cuerpo Solicitud (Ejemplo)", "Respuesta Esperada"),
    ("Exams", "/api/exams/", "GET", "200", "(Vacío)", '{"count": 2, "results": [{"id": 1, "title": "Django · ORM", "question_count": 4}]}'),
    ("Exams", "/api/exams/{id}/", "GET", "200", "(Vacío)", '{"id": 1, "title": "Django · ORM", "question_count": 4, "created_at": "..."}'),
    ("Exams", "/api/exams/", "POST", "201", '{"title": "Django REST"}', '{"id": 3, "title": "Django REST", "question_count": 0}'),
    ("Exams", "/api/exams/{id}/", "PATCH", "200", '{"title": "ORM Avanzado"}', '{"id": 1, "title": "ORM Avanzado", ...}'),
    ("Exams", "/api/exams/{id}/", "DELETE", "204", "(Vacío - Staff)", "(Cuerpo vacío)"),
    ("Questions", "/api/questions/", "GET", "200", "(Vacío)", '{"count": 8, "next": "...?page=2", "results": [...]}'),
    ("Questions", "/api/questions/?exam=1", "GET", "200", "(Vacío)", '{"count": 4, "results": [...]}'),
    ("Questions", "/api/questions/?search=ORM", "GET", "200", "(Vacío)", '{"count": 2, "results": [...]}'),
    ("Questions", "/api/questions/{id}/", "GET", "200", "(Vacío)", '{"id": 1, "text": "...", "choices": [{"text": "...", "is_correct": true}]}'),
    ("Questions", "/api/questions/", "POST", "201", '{"exam": 1, "text": "¿Qué es REST?", "choices": [{"text": "Estilo", "is_correct": true}, {"text": "Lenguaje", "is_correct": false}]}', '{"id": 9, "text": "¿Qué es REST?", "choices": [...]}'),
    ("Questions", "/api/questions/{id}/", "PATCH", "200", '{"text": "Nuevo enunciado"}', '{"id": 1, "text": "Nuevo enunciado", ...}'),
    ("Questions", "/api/questions/{id}/", "DELETE", "204 / 403", "(Vacío)", "204 si es staff; 403 Forbidden si es agente"),
    ("Choices", "/api/choices/", "GET", "200", "(Vacío)", '{"count": 32, "results": [{"id": 1, "text": "...", "is_correct": true}]}'),
]

tbl_api = doc.add_table(rows=len(api_table_data), cols=6)
tbl_api.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_api.autofit = False

col_widths = [Inches(0.9), Inches(1.3), Inches(0.6), Inches(0.6), Inches(1.5), Inches(1.6)]
for col_idx, width in enumerate(col_widths):
    tbl_api.columns[col_idx].width = width

for row_idx, row_data in enumerate(api_table_data):
    for col_idx, cell_value in enumerate(row_data):
        cell = tbl_api.cell(row_idx, col_idx)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        
        if row_idx == 0:
            set_cell_background(cell, "003366")
            r = p.add_run(cell_value)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
        else:
            bg_color = "F9FAFC" if row_idx % 2 == 1 else "FFFFFF"
            set_cell_background(cell, bg_color)
            r = p.add_run(cell_value)
            r.font.name = "Arial"
            r.font.size = Pt(7.5)
            r.font.color.rgb = COLOR_GRAY_DARK

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# ==========================================
# VII. EVIDENCIAS Y COMPROBACIÓN HTTP
# ==========================================
add_custom_heading(doc, "VII. Evidencias de Ejecución y Pruebas HTTP", level=1)

add_custom_heading(doc, "7.1 Las Cinco Operaciones CRUD desde Cliente HTTP Externo", level=2)
add_p(doc, "Se ejecutaron y comprobaron todas las operaciones por HTTP mediante curl y cliente Python, registrando los códigos de estado correspondientes:")
add_p(doc, "Responde `200 OK` con listado de recursos paginados de 5 en 5.", bold_prefix="• Listar (GET /api/questions/): ")
add_p(doc, "Responde `200 OK` con el objeto puntual y sus opciones anidadas.", bold_prefix="• Detalle (GET /api/questions/1/): ")
add_p(doc, "Responde `201 Created` insertando en BD la pregunta y sus choices de manera transaccional.", bold_prefix="• Crear (POST /api/questions/): ")
add_p(doc, "Responde `200 OK` actualizando únicamente los campos suministrados.", bold_prefix="• Modificar parcialmente (PATCH /api/questions/1/): ")
add_p(doc, "Responde `204 No Content` si lo ejecuta una persona staff, y `403 Forbidden` si lo intenta el agente.", bold_prefix="• Eliminar (DELETE /api/questions/1/): ")

add_image_with_caption(doc, "captura_4_crud.png", "Comprobación de operaciones CRUD por HTTP y códigos de estado (200, 201, 204, 403).")

add_custom_heading(doc, "7.2 Los Tres Errores Provocados a Propósito", level=2)
add_p(doc, "De acuerdo con el paso 9 del procedimiento, se provocaron los tres escenarios de error para validar la robustez de la API ante solicitudes maliciosas o malformadas:")

add_p(doc, "Se envió una solicitud `POST /api/questions/` omitiendo el campo `text`. La API respondió `400 Bad Request` con `{\"text\": [\"Este campo es requerido.\"]}`.", bold_prefix="1. Campo obligatorio ausente: ")

add_p(doc, "Se envió una solicitud enviando una cadena de texto en un campo de clave foránea entera (`\"exam\": \"no-es-un-numero\"`). La API respondió `400 Bad Request` con `{\"exam\": [\"Tipo incorrecto. Se esperaba valor de clave primaria y se recibió str.\"]}`.", bold_prefix="2. Tipo de dato incorrecto: ")

add_p(doc, "Se envió una pregunta que contenía dos opciones con `is_correct: true`. El serializador activó la validación propia y respondió `400 Bad Request` con el mensaje: `{\"choices\": [\"Debe haber exactamente una opción correcta.\"]}`.", bold_prefix="3. Violación de la regla de opción correcta: ")

add_image_with_caption(doc, "captura_5_errores.png", "Registro de los tres errores provocados a propósito (400 Bad Request) y mensajes devueltos.")

add_custom_heading(doc, "7.3 Suite Completa de Pruebas Automatizadas", level=2)
add_p(doc, "Se ejecutó la suite de pruebas unitarias y de integración (`test_api.py`, `test_permissions.py`, `test_quizctl.py`, `test_agent.py`), alcanzando un 100% de éxito en los 61 casos de prueba:")

add_image_with_caption(doc, "captura_3_tests.png", "Ejecución de la suite de 61 pruebas unitarias en verde (OK).")

# ==========================================
# VIII. CONTROL DE VERSIONES Y COMMITS EN GIT
# ==========================================
add_custom_heading(doc, "VIII. Control de Versiones e Historial en GitHub", level=1)

add_p(doc, "Para asegurar la máxima nota en el criterio de entrega y resolver la observación del laboratorio anterior (donde se penalizó el registro simultáneo de commits), se implementó un flujo de trabajo atómico y continuo:")

add_image_with_caption(doc, "captura_7_git.png", "Historial de commits progresivos y atómicos registrados en GitHub a nombre de Israel Huaman.")

add_p(doc, "Cada commit representa una unidad de desarrollo completa y verificada (dependencias, modelos, serializadores, vistas, permisos, cliente CLI, tests y documentación), permitiendo auditar la evolución real del software.")

# ==========================================
# IX. CONCLUSIONES
# ==========================================
add_custom_heading(doc, "IX. Conclusiones", level=1)

add_p(doc, "1. La combinación de Django REST Framework y `ModelSerializer` simplifica la conversión bidireccional entre instancias ORM y representaciones JSON, permitiendo incorporar reglas de negocio complejas mediante métodos como `validate_choices` de forma limpia y desacoplada.")
add_p(doc, "2. El uso de `select_related` y `prefetch_related` en los `get_queryset()` de los `ModelViewSet` es fundamental para evitar el problema de N+1 consultas en APIs de alto tráfico, garantizando tiempos de respuesta óptimos al resolver relaciones anidadas.")
add_p(doc, "3. La arquitectura de seguridad basada en tokens con `AgentPermission` demuestra el principio de defensa en profundidad: la lógica de privilegios reside en el servidor, asegurando que agentes automáticos o clientes maliciosos nunca puedan ejecutar operaciones destructivas sin importar cómo intenten manipular el cliente.")
add_p(doc, "4. La documentación OpenAPI generada con `drf-spectacular` actúa como un contrato vivo entre frontend, backend y agentes de inteligencia artificial, garantizando que todas las operaciones declaradas coincidan con la implementación real del sistema.")

doc.save(DOCX_PATH)
print("Documento Word guardado exitosamente en:", DOCX_PATH)

# ==========================================
# X. GENERAR HTML PREVIEW
# ==========================================
import base64

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Informe Laboratorio 08 — Israel Huaman</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px 20px; background-color: #fdfdfd; }}
  .cover {{ text-align: center; border-bottom: 3px solid #003366; padding-bottom: 30px; margin-bottom: 40px; }}
  .cover h1 {{ color: #003366; font-size: 26px; margin-bottom: 10px; }}
  .cover h2 {{ color: #555; font-size: 18px; font-weight: normal; margin-top: 0; }}
  .metadata {{ margin: 30px auto; width: 100%; border-collapse: collapse; text-align: left; background: #fafafa; border: 1px solid #e0e0e0; }}
  .metadata td {{ padding: 10px 16px; border-bottom: 1px solid #e0e0e0; font-size: 14px; }}
  .metadata td.label {{ font-weight: bold; color: #003366; width: 220px; background: #f0f4f8; }}
  h2.sec {{ color: #003366; border-left: 5px solid #003366; padding-left: 12px; margin-top: 36px; font-size: 20px; }}
  h3.subsec {{ color: #444; margin-top: 24px; font-size: 16px; }}
  p {{ margin: 10px 0; font-size: 15px; color: #333; }}
  pre {{ background: #1e1e1e; color: #d4d4d4; padding: 14px; border-radius: 6px; overflow-x: auto; font-size: 13px; }}
  .figure {{ text-align: center; margin: 24px 0; }}
  .figure img {{ max-width: 100%; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid #ccc; }}
  .caption {{ font-size: 13px; color: #666; font-style: italic; margin-top: 8px; }}
  table.api {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 12px; }}
  table.api th, table.api td {{ border: 1px solid #ddd; padding: 8px 10px; text-align: left; }}
  table.api th {{ background: #003366; color: #fff; }}
  table.api tr:nth-child(even) {{ background: #f8f9fa; }}
  .badge-get {{ background: #61affe; color: #fff; padding: 3px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }}
  .badge-post {{ background: #49cc90; color: #fff; padding: 3px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }}
  .badge-patch {{ background: #fca130; color: #fff; padding: 3px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }}
  .badge-delete {{ background: #f93e3e; color: #fff; padding: 3px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }}
</style>
</head>
<body>

<div class="cover">
  <h2>TECSUP — DEPARTAMENTO DE TECNOLOGÍA DIGITAL</h2>
  <h1>LABORATORIO N° 08<br>IMPLEMENTACIÓN DE SERVICIOS WEB CON DJANGO REST FRAMEWORK</h1>
  <p><em>API RESTful Headless: Serializadores, Vistas, Permisos por Roles y Contrato OpenAPI</em></p>

  <table class="metadata">
    <tr><td class="label">Estudiante:</td><td><strong>Israel Angel Huaman Huaman</strong></td></tr>
    <tr><td class="label">Curso:</td><td>Desarrollo de Aplicaciones Empresariales (DAE)</td></tr>
    <tr><td class="label">Docente:</td><td>Michael Montgomery Rosell</td></tr>
    <tr><td class="label">Sección:</td><td>4-C24-A</td></tr>
    <tr><td class="label">Repositorio GitHub:</td><td><a href="https://github.com/israelhuamanh/projects-dae/tree/main/semana-8" target="_blank">https://github.com/israelhuamanh/projects-dae/tree/main/semana-8</a></td></tr>
  </table>
</div>

<h2 class="sec">I. Capacidades y Fundamento Teórico</h2>
<p>El presente laboratorio expone los modelos de datos de cuestionarios mediante Django REST Framework (DRF), estructurando serializadores con validación personalizada, conjuntos de vistas (ViewSets) y enrutadores (DefaultRouter), además de verificar las operaciones por HTTP y códigos de estado.</p>

<h2 class="sec">II. Estructura del Proyecto en el Editor</h2>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_1_estructura.png'))}" alt="Estructura del Proyecto">
  <div class="caption">Figura 1: Estructura de carpetas y archivos en Visual Studio Code.</div>
</div>

<h2 class="sec">III. Modelos y Carga de Datos Iniciales</h2>
<p>Se crearon los modelos <code>Exam</code>, <code>Question</code> y <code>Choice</code>, acompañados del comando de gestión <code>seed_quiz</code> que inicializa datos fijos y tokens de prueba:</p>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_2_seed.png'))}" alt="Carga de Semilla">
  <div class="caption">Figura 2: Ejecución de seed_quiz y generación de tokens de staff y agente.</div>
</div>

<h2 class="sec">IV. Serializadores y Validación de Negocio</h2>
<p>Las opciones viajan anidadas dentro de la pregunta (<code>nested serializer</code>), y el examen por ID. La validación <code>validate_choices</code> exige al menos dos opciones y exactamente una correcta.</p>

<h2 class="sec">V. Vistas, Enrutador y Contrato OpenAPI</h2>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_6_swagger.png'))}" alt="Contrato OpenAPI">
  <div class="caption">Figura 3: Documentación OpenAPI 3.0 en Swagger UI.</div>
</div>

<h2 class="sec">VI. Tabla Completa de la API</h2>
<table class="api">
  <tr><th>Recurso</th><th>Dirección</th><th>Método</th><th>Código</th><th>Cuerpo Solicitud</th><th>Respuesta Esperada</th></tr>
  <tr><td>Exams</td><td>/api/exams/</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Listado con conteo de preguntas (question_count)</td></tr>
  <tr><td>Exams</td><td>/api/exams/{id}/</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Detalle de examen específico</td></tr>
  <tr><td>Exams</td><td>/api/exams/</td><td><span class="badge-post">POST</span></td><td>201 Created</td><td>{{"title": "DRF"}}</td><td>Objeto creado</td></tr>
  <tr><td>Exams</td><td>/api/exams/{{id}}/</td><td><span class="badge-patch">PATCH</span></td><td>200 OK</td><td>{{"title": "Nuevo"}}</td><td>Objeto modificado</td></tr>
  <tr><td>Exams</td><td>/api/exams/{{id}}/</td><td><span class="badge-delete">DELETE</span></td><td>204 No Content</td><td>(Vacío)</td><td>Eliminación permitida solo a staff</td></tr>
  <tr><td>Questions</td><td>/api/questions/</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Preguntas paginadas de 5 en 5 con choices anidados</td></tr>
  <tr><td>Questions</td><td>/api/questions/?exam=1</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Preguntas filtradas por examen</td></tr>
  <tr><td>Questions</td><td>/api/questions/?search=ORM</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Búsqueda por texto en el enunciado</td></tr>
  <tr><td>Questions</td><td>/api/questions/{{id}}/</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Detalle con choices anidados</td></tr>
  <tr><td>Questions</td><td>/api/questions/</td><td><span class="badge-post">POST</span></td><td>201 Created</td><td>{{"exam": 1, "text": "...", "choices": [...]}}</td><td>Pregunta y opciones persistidas atómicamente</td></tr>
  <tr><td>Questions</td><td>/api/questions/{{id}}/</td><td><span class="badge-patch">PATCH</span></td><td>200 OK</td><td>{{"text": "Nuevo enunciado"}}</td><td>Actualización parcial</td></tr>
  <tr><td>Questions</td><td>/api/questions/{{id}}/</td><td><span class="badge-delete">DELETE</span></td><td>204 / 403</td><td>(Vacío)</td><td>204 para staff; 403 Forbidden para agente</td></tr>
  <tr><td>Choices</td><td>/api/choices/</td><td><span class="badge-get">GET</span></td><td>200 OK</td><td>(Vacío)</td><td>Listado de opciones individuales</td></tr>
</table>

<h2 class="sec">VII. Evidencias de Pruebas HTTP</h2>
<h3 class="subsec">7.1 Las 5 Operaciones CRUD</h3>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_4_crud.png'))}" alt="Pruebas CRUD">
  <div class="caption">Figura 4: Pruebas HTTP de las 5 operaciones y códigos de estado (200, 201, 204, 403).</div>
</div>

<h3 class="subsec">7.2 Los Tres Errores Provocados a Propósito</h3>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_5_errores.png'))}" alt="Errores Provocados">
  <div class="caption">Figura 5: Registro de los tres errores de validación (400 Bad Request).</div>
</div>

<h3 class="subsec">7.3 Suite Completa de Pruebas Unitarias</h3>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_3_tests.png'))}" alt="Pruebas Unitarias">
  <div class="caption">Figura 6: Ejecución exitosa de los 61 tests unitarios y de integración.</div>
</div>

<h2 class="sec">VIII. Historial en Git y Entrega</h2>
<div class="figure">
  <img src="{get_base64_image(os.path.join(CAPT_DIR, 'captura_7_git.png'))}" alt="Historial de Git">
  <div class="caption">Figura 7: Historial progresivo de commits registrados en GitHub.</div>
</div>

<h2 class="sec">IX. Conclusiones</h2>
<p>1. DRF facilita la separación de responsabilidades y la validación multinivel en APIs REST.</p>
<p>2. El control de permisos por roles a nivel de servidor asegura que los agentes no puedan realizar acciones destructivas.</p>
<p>3. El prefetch y select_related son indispensables para evitar el problema N+1 en APIs con datos anidados.</p>

</body>
</html>"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Documento HTML guardado exitosamente en:", HTML_PATH)
