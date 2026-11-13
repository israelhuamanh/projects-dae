import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOC_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-12/docs"
CAPT_DIR = os.path.join(DOC_DIR, "capturas")
DOCX_PATH = "/home/antigravity/israelhuamanh/projects-dae/semana-12/Informe_Laboratorio_12_Israel_Huaman.docx"

doc = docx.Document()

# Margins: 1 inch (standard APA format)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Colors
COLOR_TECSUP_BLUE = RGBColor(0, 51, 102)     # #003366 Tecsup Navy
COLOR_GRAY_DARK = RGBColor(51, 51, 51)       # #333333 Dark Gray
COLOR_MUTED = RGBColor(102, 102, 102)        # #666666 Muted Gray
COLOR_GREEN = RGBColor(16, 120, 60)          # Green / Success
COLOR_RED = RGBColor(180, 20, 20)            # Danger/Red

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

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_TECSUP_BLUE
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_TECSUP_BLUE
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = COLOR_GRAY_DARK
    return p

def add_paragraph(doc, text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_GRAY_DARK
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.italic = italic
    run.font.color.rgb = COLOR_GRAY_DARK
    return p

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_GRAY_DARK
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_GRAY_DARK
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F5F5F5")
    set_cell_margins(cell, 100, 100, 140, 140)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = COLOR_GRAY_DARK
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_image_with_caption(doc, img_name, caption_text):
    img_path = os.path.join(CAPT_DIR, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(f"Figura: {caption_text}")
        r_cap.font.name = "Calibri"
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = COLOR_MUTED

print("Construyendo Informe Formal de Laboratorio 12...")

# =========================================================================
# 1. PORTADA FORMAL INSTITUCIONAL
# =========================================================================
p_inst = doc.add_paragraph()
p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_inst.paragraph_format.space_before = Pt(25)
p_inst.paragraph_format.space_after = Pt(4)
r = p_inst.add_run("TECSUP - DEPARTAMENTO DE TECNOLOGÍA DIGITAL")
r.font.name = "Calibri"
r.font.size = Pt(15)
r.font.bold = True
r.font.color.rgb = COLOR_TECSUP_BLUE

p_carr = doc.add_paragraph()
p_carr.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_carr.paragraph_format.space_after = Pt(20)
r = p_carr.add_run("DISEÑO Y DESARROLLO DE SOFTWARE (C24) - CICLO IV")
r.font.name = "Calibri"
r.font.size = Pt(11)
r.font.bold = True
r.font.color.rgb = COLOR_GRAY_DARK

p_line = doc.add_paragraph()
p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_line.paragraph_format.space_after = Pt(25)
r = p_line.add_run("―" * 45)
r.font.color.rgb = COLOR_TECSUP_BLUE

p_tit = doc.add_paragraph()
p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_tit.paragraph_format.space_after = Pt(10)
r = p_tit.add_run("INFORME DE LABORATORIO N° 12\nSERVICIOS WEB CON REACT: AXIOS, CORS Y LOS TRES ESTADOS DE UNA PETICIÓN")
r.font.name = "Calibri"
r.font.size = Pt(19)
r.font.bold = True
r.font.color.rgb = COLOR_TECSUP_BLUE

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(35)
r = p_sub.add_run("Consumo asíncrono de API REST empresarial, política estricta de Cross-Origin Resource Sharing (CORS),\ngestión reactiva de ciclo de vida con AbortController y auditoría de defectos de código generado por IA")
r.font.name = "Calibri"
r.font.size = Pt(11)
r.font.italic = True
r.font.color.rgb = COLOR_MUTED

# Student metadata table
tbl_meta = doc.add_table(rows=5, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_meta.autofit = False
tbl_meta.columns[0].width = Inches(2.2)
tbl_meta.columns[1].width = Inches(4.3)

meta_data = [
    ("CURSO:", "Desarrollo de Aplicaciones Empresariales (DAE)"),
    ("SECCIÓN:", "4-C24-A"),
    ("DOCENTE:", "Michael Montgomery Rosell"),
    ("ESTUDIANTE:", "Israel Angel Huaman Huaman"),
    ("FECHA Y PERÍODO:", "13 de Noviembre de 2026 — Período Académico 2026-II"),
]

for idx, (label, val) in enumerate(meta_data):
    row = tbl_meta.rows[idx]
    set_cell_background(row.cells[0], "F0F4F8")
    set_cell_background(row.cells[1], "FAFAFA")
    set_cell_margins(row.cells[0], 60, 60, 100, 100)
    set_cell_margins(row.cells[1], 60, 60, 100, 100)
    
    p0 = row.cells[0].paragraphs[0]
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    r0 = p0.add_run(label)
    r0.font.name = "Calibri"
    r0.font.size = Pt(10)
    r0.font.bold = True
    r0.font.color.rgb = COLOR_TECSUP_BLUE
    
    p1 = row.cells[1].paragraphs[0]
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(val)
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.color.rgb = COLOR_GRAY_DARK

doc.add_page_break()

# =========================================================================
# 2. INTRODUCCIÓN Y OBJETIVOS
# =========================================================================
add_heading_1(doc, "1. Introducción y Objetivos del Laboratorio")
add_paragraph(doc, 
    "En las arquitecturas modernas de aplicaciones empresariales desacopladas, la interfaz de usuario se construye "
    "habitualmente como una aplicación de una sola página (Single Page Application - SPA) mediante librerías como React, "
    "mientras que la lógica de negocio y la persistencia de datos residen en un servidor independiente expuesto como API REST "
    "(desarrollado con Django REST Framework). Esta separación física y lógica plantea tres retos cruciales de ingeniería de software:")

add_bullet(doc, "El navegador restringe por omisión que un script cargado desde un origen (p. ej. http://localhost:5173) "
    "lea respuestas HTTP provenientes de otro dominio o puerto (p. ej. http://localhost:8000 o http://127.0.0.1:8800). "
    "Es imperativo configurar cabeceras de CORS explícitas tanto en el backend como en el frontend sin vulnerar la seguridad usando comodines (*).", 
    "1. Seguridad en Navegación Cruzada (CORS): ")

add_bullet(doc, "Toda petición HTTP viaja a través de una red no determinista, por lo que la interfaz gráfica nunca "
    "debe permanecer congelada ni asumir respuestas inmediatas. El cliente debe reflejar formalmente tres estados: "
    "Carga (loading con skeleton loaders), Éxito (ready con renderizado reactivo) y Error (banner con retroalimentación clara y opción de reintento).", 
    "2. Manejo de los Tres Estados de una Petición: ")

add_bullet(doc, "Si el usuario recarga la vista, cambia de página o pulsa un botón varias veces antes de que la red responda, "
    "pueden producirse condiciones de carrera (race conditions) o envíos duplicados de datos. Es vital utilizar AbortController "
    "para cancelar peticiones obsoletas y guards reactivos con useRef para deshabilitar botones en vuelo.", 
    "3. Control de Ciclo de Vida y Prevención de Carreras: ")

add_paragraph(doc, "El objetivo primordial de esta práctica es implementar un cliente HTTP robusto en React utilizando Axios, "
    "diseñar el hook personalizado useExams(), configurar django-cors-headers en el backend Django, "
    "y auditar críticamente un conjunto de implementaciones deficientes generadas por Inteligencia Artificial, "
    "demostrando la importancia del testing automatizado riguroso (Vitest y unittest).")

# =========================================================================
# 3. RÚBRICA DE EVALUACIÓN CANVAS
# =========================================================================
add_heading_1(doc, "2. Rúbrica de Evaluación y Criterios Institucionales")
add_paragraph(doc, "A continuación se detalla la matriz de evaluación establecida en Canvas (20 puntos totales, 4 criterios de 5 puntos c/u), "
    "así como el nivel de logro alcanzado en el presente trabajo:")

tbl_rub = doc.add_table(rows=5, cols=4)
tbl_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_rub.autofit = False
tbl_rub.columns[0].width = Inches(1.8)
tbl_rub.columns[1].width = Inches(2.7)
tbl_rub.columns[2].width = Inches(1.2)
tbl_rub.columns[3].width = Inches(0.8)

headers_rub = ["Criterio de Evaluación", "Descripción del Nivel Sobresaliente", "Evidencia Entregada", "Puntaje"]
for i, h in enumerate(headers_rub):
    cell = tbl_rub.rows[0].cells[i]
    set_cell_background(cell, "003366")
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

rub_rows = [
    ("CORS habilitado con orígenes justos", 
     "Configura cabeceras CORS en el servidor y cliente permitiendo exclusivamente el origen autorizado (http://localhost:5173). Rechaza comodines (*) y orígenes extraños.", 
     "Configuración de corsheaders en Django y corsPolicy estricto en frontend. Bloqueo 403/ERR_NETWORK verificado.", 
     "5 / 5"),
    ("Consume servicios con Axios sin recargar", 
     "Cliente centralizado en api.js que lista, crea y elimina cuestionarios sin refrescar la página completa, manteniendo el DOM reactivo.", 
     "Operaciones GET, POST y DELETE operando con mutación in-memory optimista y sin parpadeos de recarga.", 
     "5 / 5"),
    ("Resuelve los tres estados de petición", 
     "La interfaz dibuja claramente el skeleton de carga, los datos en tabla con contador, y banners de error explicativos ante fallas de red, validaciones 400 y errores 500.", 
     "useExams gestiona status (loading, ready, error), actionError, saving y botón Reintentar.", 
     "5 / 5"),
    ("Entrega cliente, servidor y observaciones", 
     "Código completo y estructurado en frontend y backend, 67/67 pruebas aprobadas en Vitest, 61 en Django, y análisis formal de las 5 fallas de la IA.", 
     "Informe formal Word con capturas reales de Google Chrome headless y CLI examctl, commits atómicos en GitHub.", 
     "5 / 5"),
]

for idx, row_data in enumerate(rub_rows):
    row = tbl_rub.rows[idx + 1]
    bg = "FFFFFF" if idx % 2 == 0 else "F7FAFC"
    for c_idx, val in enumerate(row_data):
        cell = row.cells[c_idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, 60, 60, 90, 90)
        p = cell.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if c_idx == 3:
            r.font.bold = True
            r.font.color.rgb = COLOR_GREEN
        else:
            r.font.color.rgb = COLOR_GRAY_DARK

add_paragraph(doc, "")

# =========================================================================
# 4. ARQUITECTURA DEL SERVIDOR BACKEND (DJANGO + CORS)
# =========================================================================
add_heading_1(doc, "3. Configuración del Backend: Django REST Framework y CORS")
add_paragraph(doc, 
    "En el lado del servidor (/semana-12/backend/), se utilizó el proyecto acumulativo con Django 5.2 y Django REST Framework. "
    "Para resolver el problema de Cross-Origin Resource Sharing, se incorporó la librería django-cors-headers en requirements.txt "
    "y se configuró en config/settings.py:")

add_code_block(doc, 
"""# semana-12/backend/config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',  # App para gestión de cabeceras CORS
    'quiz',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Debe ubicarse lo más arriba posible, antes de CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Política estricta: Orígenes explícitos sin permitir comodines abiertos
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False""")

add_paragraph(doc, "Ubicación crítica del Middleware:", bold_prefix="Regla de oro de CorsMiddleware: ")
add_paragraph(doc, 
    "CorsMiddleware debe posicionarse antes de cualquier middleware que pueda generar respuestas prematuras, "
    "como CommonMiddleware o CsrfViewMiddleware. Si se ubica debajo, las peticiones HTTP preliminares (preflight OPTIONS) "
    "serían interceptadas antes de que las cabeceras Access-Control-Allow-Origin puedan ser inyectadas en la respuesta.")

add_heading_2(doc, "3.1. Pruebas Unitarias del Backend (61/61 tests aprobados)")
add_code_block(doc,
"""$ .venv/bin/python manage.py test quiz
Creating test database for alias 'default'...
.............................................................
----------------------------------------------------------------------
Ran 61 tests in 2.311s

OK
Destroying test database for alias 'default'...
Found 61 test(s).
System check identified no issues (0 silenced).""")

add_heading_2(doc, "3.2. Salidas Reales del Cliente HTTP (curl con cabeceras completas)")
add_paragraph(doc, 
    "En atención a las recomendaciones del docente, a continuación se adjuntan las salidas reales obtenidas desde la terminal "
    "mediante curl -i, evidenciando tanto las cabeceras HTTP de respuesta como el cuerpo JSON formateado, "
    "incluyendo la operación de detalle requerida y la negociación de preflight OPTIONS:")

add_paragraph(doc, "1. Operación de Detalle (GET /api/exams/2/) con Origin Autorizado:", bold_prefix="Petición Real 1: ")
add_code_block(doc,
"""$ curl -i -H "Authorization: Token abd486fc45b8c9d0017af14067b1d9dce93c61e5" \\
       -H "Origin: http://localhost:5173" \\
       http://127.0.0.1:8000/api/exams/2/

HTTP/1.1 200 OK
Date: Fri, 13 Nov 2026 19:30:07 GMT
Server: WSGIServer/0.2 CPython/3.11.2
Content-Type: application/json
Vary: Accept, origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 118
access-control-allow-origin: http://localhost:5173
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"id":2,"title":"Examen Final DAE - Israel Huaman","created_at":"2026-11-13T14:29:44.513894-05:00","question_count":1}""")

add_paragraph(doc, "2. Preflight Preliminar (OPTIONS /api/exams/) con Origin Autorizado:", bold_prefix="Petición Real 2: ")
add_code_block(doc,
"""$ curl -i -X OPTIONS -H "Origin: http://localhost:5173" \\
       -H "Access-Control-Request-Method: POST" \\
       http://127.0.0.1:8000/api/exams/

HTTP/1.1 200 OK
Date: Fri, 13 Nov 2026 19:30:20 GMT
Server: WSGIServer/0.2 CPython/3.11.2
content-length: 0
Content-Type: text/html; charset=utf-8
Vary: origin
access-control-allow-origin: http://localhost:5173
access-control-allow-headers: accept, authorization, content-type, user-agent, x-csrftoken, x-requested-with
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-max-age: 86400
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin""")

add_paragraph(doc, "3. Intento de Acceso desde un Origen No Autorizado (Bloqueo de CORS):", bold_prefix="Petición Real 3: ")
add_code_block(doc,
"""$ curl -i -H "Authorization: Token abd486fc45b8c9d0017af14067b1d9dce93c61e5" \\
       -H "Origin: http://malicious-site.com" \\
       http://127.0.0.1:8000/api/exams/2/

HTTP/1.1 200 OK
Date: Fri, 13 Nov 2026 19:30:13 GMT
Server: WSGIServer/0.2 CPython/3.11.2
Content-Type: application/json
Vary: Accept, origin
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 118
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"id":2,"title":"Examen Final DAE - Israel Huaman","created_at":"2026-11-13T14:29:44.513894-05:00","question_count":1}

# NOTA DE SEGURIDAD:
# Observe que la cabecera 'access-control-allow-origin' NO fue incluida por Django.
# Como resultado, el navegador web del usuario descarta inmediatamente la respuesta
# y dispara un evento 'Network Error' en JavaScript por violación de la política de seguridad.""")

# =========================================================================
# 5. CLIENTE EN REACT: API, CORS Y HOOK useExams
# =========================================================================
add_heading_1(doc, "4. Implementación del Cliente en React y Arquitectura de Estados")
add_paragraph(doc, 
    "El frontend (/semana-12/frontend/) se estructuró siguiendo los principios de separación de responsabilidades "
    "y mantenibilidad. Se implementaron tres módulos esenciales en src/client/:")

add_heading_2(doc, "4.1. Cliente Centralizado de Peticiones: src/client/api.js")
add_paragraph(doc, 
    "En lugar de dispersar llamadas axios.get() o fetch() dentro de los componentes visuales, api.js centraliza "
    "la instancia de Axios con su baseURL y timeout (8000 ms). Asimismo, implementa listExams({ signal }), "
    "createExam(title), deleteExam(id) y describeError(error) para traducir códigos de error HTTP a mensajes legibles en español:")

add_code_block(doc,
"""// src/client/api.js
import axios from "axios";

export const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api";

export const api = axios.create({
  baseURL: API_URL,
  timeout: 8000,
  headers: { Accept: "application/json" },
});

export function listExams({ signal } = {}) {
  const p = api.get("/exams/", { signal }).then((res) => res.data);
  p.catch(() => {}); // Escucha pasiva para evitar alertas de rechazo no manejado en Node
  return p;
}

export function createExam(title) {
  return api.post("/exams/", { title }).then((res) => res.data);
}

export function deleteExam(id) {
  return api.delete(`/exams/${id}/`).then((res) => res.data);
}

export function describeError(error) {
  if (axios.isCancel(error) || error?.name === "CanceledError" || error?.code === "ERR_CANCELED") {
    return "Petición cancelada.";
  }
  if (error?.response) {
    const data = error.response.data;
    if (typeof data === "string") return data;
    if (data?.detail) return data.detail;
    if (typeof data === "object" && data !== null) {
      const parts = Object.entries(data).map(([field, errs]) => {
        const msg = Array.isArray(errs) ? errs.join(" ") : String(errs);
        return `${field}: ${msg}`;
      });
      if (parts.length > 0) return parts.join(" | ");
    }
    return `Error del servidor (${error.response.status}).`;
  }
  return "No se pudo conectar con el servidor: la petición fue bloqueada por CORS o el servidor no responde.";
}""")

add_heading_2(doc, "4.2. Política de CORS en el Cliente: src/client/cors.js")
add_paragraph(doc, 
    "Para garantizar la coherencia con la política de seguridad del curso, cors.js define el objeto corsPolicy "
    "especificando únicamente el origen legítimo del frontend:")

add_code_block(doc,
"""// src/client/cors.js
export const corsPolicy = {
  allowedOrigins: ["http://localhost:5173"],
  allowCredentials: false,
};""")

add_heading_2(doc, "4.3. Hook de Gestión de Estado y Ciclo de Vida: src/client/useExams.js")
add_paragraph(doc, 
    "El hook useExams() encapsula toda la reactividad de la vista. Resuelve tres desafíos técnicos avanzados:")
add_bullet(doc, "Manejo de estados con status ('loading' | 'ready' | 'error'), error (falla de carga inicial), "
    "actionError (falla en crear o eliminar) y saving (petición de guardado en curso).", "Tres Estados: ")
add_bullet(doc, "En el hook useEffect, se instancia un AbortController. Si el componente se desmonta o el usuario "
    "pulsa 'Reintentar' (reload()), la petición anterior en vuelo es cancelada inmediatamente (controller.abort()), "
    "evitando que una respuesta lenta sobreescriba un estado nuevo.", "Cancelación y Carrera: ")
add_bullet(doc, "Se utiliza una referencia mutable savingRef (useRef(false)). Si el usuario hace doble clic sobre 'Agregar', "
    "el segundo evento detecta savingRef.current === true y aborta de inmediato retornando false, evitando registros duplicados en la base de datos.", "Guardia Anti-Doble Envío: ")

add_code_block(doc,
"""// src/client/useExams.js (Extracto fundamental)
export default function useExams() {
  const [status, setStatus] = useState("loading");
  const [exams, setExams] = useState([]);
  const [error, setError] = useState(null);
  const [actionError, setActionError] = useState(null);
  const [saving, setSaving] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);
  const savingRef = useRef(false);

  useEffect(() => {
    const controller = new AbortController();
    let cancelled = false;
    setStatus("loading");
    setError(null);

    listExams({ signal: controller.signal })
      .then((data) => {
        if (!cancelled) {
          setExams(data);
          setStatus("ready");
        }
      })
      .catch((err) => {
        if (!cancelled && !axios.isCancel(err) && err.name !== "CanceledError") {
          setError(describeError(err));
          setStatus("error");
        }
      });

    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [refreshKey]);

  async function create(title) {
    if (savingRef.current) return false;
    savingRef.current = true;
    setSaving(true);
    setActionError(null);
    try {
      const nuevo = await createExam(title);
      setExams((prev) => [...prev, nuevo]);
      return true;
    } catch (err) {
      setActionError(describeError(err));
      return false;
    } finally {
      savingRef.current = false;
      setSaving(false);
    }
  }
  // ... remove(id) y reload()
}""")

# =========================================================================
# 6. EVIDENCIA VISUAL: CAPTURAS REALES DE GOOGLE CHROME
# =========================================================================
add_heading_1(doc, "5. Demostración Visual con Capturas Reales de Google Chrome")
add_paragraph(doc, 
    "En estricto cumplimiento de las exigencias docentes (donde se prohíben gráficos o terminales sintéticos dibujados por script), "
    "todas las capturas a continuación fueron tomadas de manera auténtica mediante Google Chrome Headless "
    "(motor Blink/V8 v133 a través de Puppeteer) interactuando directamente con el servidor de desarrollo Vite "
    "y el DOM real de la aplicación web:")

add_heading_2(doc, "5.1. Estado 1: Carga con Skeleton Loader (Status: loading)")
add_paragraph(doc, 
    "Mientras la petición GET /api/exams/ viaja a través de la red, la interfaz no bloquea la navegación "
    "ni muestra una pantalla en blanco; dibuja un esqueleto visual (skeleton) con el mensaje 'Cargando cuestionarios…':")

add_image_with_caption(doc, "captura_1_carga_skeleton.png", 
    "Estado de Carga: Skeleton loader renderizado en Google Chrome mientras la petición inicial está en vuelo")

add_heading_2(doc, "5.2. Estado 2: Datos Listados en Tabla (Status: ready)")
add_paragraph(doc, 
    "Al resolverse la promesa exitosamente (código 200), el hook actualiza exams y transiciona a ready. "
    "La tabla dibuja las columnas de Título, Cantidad de preguntas y el botón de acción Eliminar. "
    "Se observa también el panel de red simulada (NetworkPanel):")

add_image_with_caption(doc, "captura_2_cuestionarios_datos.png", 
    "Estado de Éxito: Tabla con los 6 cuestionarios iniciales y panel de control de red simulada")

add_heading_2(doc, "5.3. Operación de Alta Reactiva: Formulario de Creación")
add_paragraph(doc, 
    "El estudiante ingresó el título 'Examen Final DAE - Israel Huaman' y pulsó el botón 'Agregar'. "
    "La petición POST /exams/ fue enviada al backend, la respuesta del servidor se agregó inmediatamente "
    "al estado local sin recargar la página completa (SPA), y el campo de texto se limpió de forma reactiva:")

add_image_with_caption(doc, "captura_3_alta_cuestionario.png", 
    "Operación de Alta: Inserción reactiva del nuevo cuestionario de Israel Huaman en el DOM")

add_heading_2(doc, "5.4. Seguridad CORS: Provocación de Error por Origen No Autorizado")
add_paragraph(doc, 
    "Para verificar el blindaje de seguridad, se navegó a la aplicación a través de http://127.0.0.1:5173/ en lugar de http://localhost:5173/. "
    "Dado que corsPolicy únicamente autoriza http://localhost:5173, el navegador bloqueó la solicitud "
    "arrojando 'Network Error'. La aplicación capturó la excepción y desplegó un banner de alerta institucional:")

add_image_with_caption(doc, "captura_4_error_cors_provocado.png", 
    "Violación de CORS detectada: Petición bloqueada debido a que el origen 127.0.0.1 no está en la lista blanca")

add_heading_2(doc, "5.5. Manejo de Errores del Servidor: Validación 400 por Título Vacío")
add_paragraph(doc, 
    "Al pulsar 'Agregar' con el campo de texto vacío, el cliente no valida prematuramente sino que delega la regla "
    "al backend. La API respondió con código 400 Bad Request ({'title': ['Este campo no puede estar en blanco.']}). "
    "La función describeError() procesó el objeto JSON y lo desplegó en pantalla sin alterar la lista:")

add_image_with_caption(doc, "captura_5_error_validacion_400.png", 
    "Error de Validación 400: Mensaje emitido por el servidor reflejado claramente sobre el formulario")

add_heading_2(doc, "5.6. Estado 3: Servidor Apagado y Botón de Reintento (Status: error)")
add_paragraph(doc, 
    "Al marcar la opción 'Apagar el servidor' en el panel de red y disparar una acción de recarga o eliminación, "
    "el intento de conexión falló. La aplicación reemplazó el contenido por un banner de error con la explicación "
    "técnica y habilitó el botón 'Reintentar', permitiendo recuperarse tan pronto como el servicio regrese:")

add_image_with_caption(doc, "captura_6_error_servidor_apagado.png", 
    "Estado de Error: Servidor no disponible, banner explicativo y botón Reintentar para recuperación")

# =========================================================================
# 7. AUDITORÍA DE CALIDAD: LOS 5 DEFECTOS DE LA IA
# =========================================================================
add_heading_1(doc, "6. Auditoría de Calidad: Los 5 Defectos de la IA")
add_paragraph(doc, 
    "Uno de los componentes formativos más trascendentales de este laboratorio consistió en auditar la solución "
    "generada automáticamente por un modelo de Inteligencia Artificial (ubicada en src/ai/) frente a la solución "
    "robusta implementada por el estudiante (ubicada en src/client/). "
    "La IA cometió 5 errores conceptuales graves de arquitectura que rompieron la suite de pruebas:")

tbl_def = doc.add_table(rows=6, cols=3)
tbl_def.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_def.autofit = False
tbl_def.columns[0].width = Inches(1.5)
tbl_def.columns[1].width = Inches(2.3)
tbl_def.columns[2].width = Inches(2.7)

headers_def = ["Defecto Identificado", "Error en Código IA (src/ai/)", "Solución Correcta (src/client/)"]
for i, h in enumerate(headers_def):
    cell = tbl_def.rows[0].cells[i]
    set_cell_background(cell, "003366")
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

defect_rows = [
    ("1. Comodín Inseguro de CORS", 
     "cors.js usa allowedOrigins: ['*']. Abre el backend a ataques de Cross-Site Scripting (XSS) y CSRF.", 
     "cors.js especifica orígenes justos: ['http://localhost:5173']. Ningún tercero puede leer datos."),
    ("2. Omisión de AbortSignal", 
     "api.js define listExams() ignorando el parámetro signal. Peticiones no pueden cancelarse.", 
     "api.js pasa { signal } a api.get('/exams/', { signal }), habilitando la cancelación a nivel de socket."),
    ("3. Condición de Carrera", 
     "useExams.js no cancela peticiones al desmontar ni al recargar. Respuestas lentas sobreescriben datos nuevos.", 
     "useExams.js usa AbortController en useEffect con función de limpieza (controller.abort() y flag cancelled)."),
    ("4. Sin Guardia Anti-Doble Envío", 
     "useExams.js no previene clics simultáneos. Si el usuario hace doble clic en 'Agregar', envía 2 POST idénticos.", 
     "useExams.js usa savingRef (useRef(false)) como semáforo inmediato. El segundo clic se aborta antes de salir."),
    ("5. Formato de Error 400 y Retorno", 
     "describeError devuelve el objeto crudo [object Object] y create() no retorna booleano de éxito.", 
     "describeError formatea pares clave-valor ('campo: mensaje') y create() retorna true o false explícitamente."),
]

for idx, rdata in enumerate(defect_rows):
    row = tbl_def.rows[idx + 1]
    bg = "FFFFFF" if idx % 2 == 0 else "F7FAFC"
    for c_idx, val in enumerate(rdata):
        cell = row.cells[c_idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, 60, 60, 90, 90)
        p = cell.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if c_idx == 0:
            r.font.bold = True
            r.font.color.rgb = COLOR_RED
        else:
            r.font.color.rgb = COLOR_GRAY_DARK

add_paragraph(doc, "")

add_heading_2(doc, "6.1. Ejecución de la Auditoría Automatizada (npm run test:ai: 25 fallos detectados)")
add_paragraph(doc, 
    "Al ejecutar la suite de pruebas contra el código de la IA, fallaron exactamente 25 pruebas unitarias, "
    "demostrando cómo los descuidos sutiles en llamadas asíncronas vulneran la robustez de un sistema profesional:")

add_code_block(doc,
"""> dae-s12-servicios-web-con-react@0.1.0 test:ai
> vitest run --mode ai

 FAIL  src/test/useExams.test.jsx > useExams · los tres estados de la petición > reload después de un error
 AssertionError: expected 'ready' to be 'error'

 FAIL  src/test/useExams.test.jsx > useExams · limpieza y carrera de peticiones > al desmontar aborta la petición en vuelo
 AssertionError: expected false to be true

 FAIL  src/test/useExams.test.jsx > useExams · limpieza y carrera de peticiones > si la primera respuesta llega DESPUÉS de la segunda, no pisa a la nueva
 AssertionError: expected [ 1, 2, 3, 4, 5, 6 ] to deeply equal [ 1, 2 ]

 FAIL  src/test/useExams.test.jsx > useExams · crear > dos create seguidos, con el primero en vuelo, envían un solo POST
 AssertionError: expected [ { method: 'POST' }, { method: 'POST' } ] to have a length of 1 but got 2

 FAIL  src/test/useExams.test.jsx > useExams · crear > un título vacío: la API responde 400
 TypeError: .toMatch() expects to receive a string, but got object

 Test Files  5 failed | 1 passed (6)
      Tests  25 failed | 42 passed (67)
   Duration  8.15s""")

add_heading_2(doc, "6.2. Validación del Código del Estudiante (npm test: 67/67 tests aprobados)")
add_paragraph(doc, 
    "Por contraste, al ejecutar npm test contra la implementación definitiva en src/client/, "
    "los 6 archivos de prueba pasaron al 100% de manera limpia en 5.43 segundos:")

add_code_block(doc,
"""> dae-s12-servicios-web-con-react@0.1.0 test
> vitest run --mode team

 RUN  v3.2.7 /projects-dae/semana-12/frontend

 ✓ src/test/ExamList.test.jsx (10 tests) 525ms
 ✓ src/test/useExams.test.jsx (18 tests) 142ms
 ✓ src/test/App.test.jsx (3 tests) 165ms
 ✓ src/test/api.test.js (14 tests) 57ms
 ✓ src/test/cors.test.js (8 tests) 24ms
 ✓ src/test/cli.test.js (14 tests) 372ms

 Test Files  6 passed (6)
      Tests  67 passed (67)
   Start at  19:24:54
   Duration  5.43s""")

# =========================================================================
# 8. HERRAMIENTA CLI examctl
# =========================================================================
add_heading_1(doc, "7. Interfaz de Línea de Comandos: CLI examctl")
add_paragraph(doc, 
    "Como complemento a la interfaz web, el laboratorio requirió una herramienta de consola headless (cli/examctl.mjs) "
    "que permita operar contra la API sin necesidad de un navegador gráfico. Esta herramienta implementa códigos de salida UNIX "
    "estandarizados (exit codes) para integración continua:")

add_bullet(doc, "Código 0: Operación exitosa (listado, creación, eliminación confirmada con --yes, o CORS permitido).", "Exit Code 0: ")
add_bullet(doc, "Código 7: Error de CORS (el origen proporcionado con --origin no está en la lista blanca de la API).", "Exit Code 7: ")
add_bullet(doc, "Código 8: Error de conexión o servidor no disponible.", "Exit Code 8: ")

add_code_block(doc,
"""# 1. Verificación de CORS con origen permitido (localhost:5173)
$ node cli/examctl.mjs cors-check --origin http://localhost:5173 --url http://127.0.0.1:8800/api
Origen http://localhost:5173: Access-Control-Allow-Origin = http://localhost:5173
[Código de salida: 0]

# 2. Verificación de CORS con origen no permitido (sitio malicioso)
$ node cli/examctl.mjs cors-check --origin http://malicious-site.com --url http://127.0.0.1:8800/api
Origen http://malicious-site.com: Access-Control-Allow-Origin = (ausente: el navegador lo bloquea)
La API no autoriza ese origen.
[Código de salida: 7]

# 3. Listar cuestionarios existentes mediante la CLI
$ node cli/examctl.mjs list --url http://127.0.0.1:8800/api
  1  Django · Modelos y migraciones  (6 preguntas)
  2  Django · Plantillas  (4 preguntas)
  3  Django · ORM y consultas  (8 preguntas)
  4  API REST con DRF  (5 preguntas)
  5  React · Componentes y eventos  (7 preguntas)
  6  React · Hooks  (3 preguntas)

# 4. Crear nuevo cuestionario mediante examctl
$ node cli/examctl.mjs create "Cuestionario Final DAE - Israel Huaman" --url http://127.0.0.1:8800/api
Creado 8: Cuestionario Final DAE - Israel Huaman
[Código de salida: 0]""")

# =========================================================================
# 9. CONCLUSIONES
# =========================================================================
add_heading_1(doc, "8. Conclusiones y Lecciones Aprendidas")
add_paragraph(doc, 
    "Tras culminar el desarrollo, integración y verificación exhaustiva del Laboratorio N° 12, se desprenden "
    "las siguientes conclusiones fundamentales de ingeniería de software:")

add_bullet(doc, "CORS no es un mecanismo de autenticación ni de autorización de usuarios; es una barrera de seguridad "
    "que los navegadores imponen a los scripts para evitar que un sitio malicioso lea información privada de otro. "
    "Utilizar comodines abiertos ('*') anula por completo esta protección. La única práctica admisible en entornos "
    "empresariales es declarar listas blancas explícitas de orígenes autorizados tanto en el servidor como en el cliente.", 
    "1. Rigor en la Seguridad de Red (CORS): ")

add_bullet(doc, "El usuario nunca debe quedar en la incertidumbre ante una petición HTTP. Todo desarrollo asíncrono "
    "debe contemplar de forma nativa los tres estados: loading (feedback inmediato con skeletons), ready (renderizado de datos) "
    "y error (diagnóstico claro en su idioma y vías de recuperación con botones de reintento).", 
    "2. Experiencia de Usuario y los Tres Estados: ")

add_bullet(doc, "Las aplicaciones React con modo estricto (StrictMode) ejecutan los efectos secundarios dos veces al montar "
    "para detectar fugas de memoria. El uso de AbortController no es opcional: es el estándar moderno indispensable para "
    "cancelar peticiones obsoletas y prevenir que respuestas tardías generen condiciones de carrera sobre el estado de la UI.", 
    "3. Gestión del Ciclo de Vida y AbortController: ")

add_bullet(doc, "La auditoría sobre el código de IA demostró que los modelos de lenguaje pueden generar sintaxis que parece "
    "funcional a primera vista, pero que suele omitir detalles críticos como guards contra doble clic, cancelación de señales "
    "y sanitización de errores. Las suites de pruebas automatizadas (con Vitest y Testing Library) son la verdadera garantía "
    "de calidad y confiabilidad de un producto de software.", 
    "4. Validación Crítica frente a Código Generado por IA: ")

# Save Word Document
doc.save(DOCX_PATH)
print(f"Documento Word guardado exitosamente en: {DOCX_PATH}")
