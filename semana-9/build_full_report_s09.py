import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOC_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-9/docs"
CAPT_DIR = os.path.join(DOC_DIR, "capturas")
DOCX_PATH = "/home/antigravity/israelhuamanh/projects-dae/semana-9/Informe_Laboratorio_09_Israel_Huaman.docx"

doc = docx.Document()

# Margins
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
    set_cell_margins(cell, 100, 100, 140, 140)
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
run_title = p_title.add_run("LABORATORIO N° 09\nINTRODUCCIÓN A REACTJS")
run_title.font.name = "Arial"
run_title.font.size = Pt(20)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_TECSUP_BLUE

p_subt = doc.add_paragraph()
p_subt.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_subt.paragraph_format.space_before = Pt(0)
p_subt.paragraph_format.space_after = Pt(48)
run_subt = p_subt.add_run("Construcción de Cartelera de Cine con React, Vite, Componentes Funcionales JSX y Props")
run_subt.font.name = "Arial"
run_subt.font.size = Pt(12)
run_subt.font.italic = True
run_subt.font.color.rgb = COLOR_GRAY_DARK

# Metadata table
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
    ("Repositorio GitHub:", "https://github.com/israelhuamanh/projects-dae/tree/main/semana-9"),
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

add_p(doc, "El presente laboratorio introduce el desarrollo frontend moderno mediante ReactJS y el empaquetador Vite, orientado a la creación de interfaces de usuario declarativas, modulares y reactivas para aplicaciones empresariales.")

add_p(doc, "Crea un proyecto de React con Vite y lo levanta en el servidor de desarrollo.", bold_prefix="• Capacidad 1: ")
add_p(doc, "Escribe componentes funcionales con JSX y los compone para armar una interfaz completa.", bold_prefix="• Capacidad 2: ")
add_p(doc, "Pasa datos de un componente padre a sus hijos mediante props.", bold_prefix="• Capacidad 3: ")

add_p(doc, "Conforme a la metodología acumulativa del curso de DAE, este laboratorio no parte de un proyecto en blanco, sino que hereda la arquitectura construida en la Semana 8. Dentro de `semana-9/` se consolida una estructura Full-Stack que alberga el backend en Django REST Framework (`backend/`) y la nueva aplicación cliente en React (`frontend/`), preparando el terreno para el consumo de servicios web en sesiones posteriores.")

# ==========================================
# II. ESTRUCTURA DEL PROYECTO
# ==========================================
add_custom_heading(doc, "II. Estructura del Proyecto en el Editor", level=1)

add_p(doc, "Siguiendo los estándares del curso y las directivas de la guía, la carpeta `semana-9/` se organizó en dos módulos principales (Backend y Frontend):")

add_image_with_caption(doc, "captura_1_estructura.png", "Estructura de directorios y archivos de la solución Full-Stack semana-9.")

add_p(doc, "Detalle de la arquitectura implementada:", bold_prefix="Organización: ")
add_p(doc, "Contiene la API RESTful de la Semana 8 (Django, modelos, serializadores, enrutadores y suite de tests).", bold_prefix="• semana-9/backend/: ")
add_p(doc, "Proyecto React inicializado con Vite, estructurado en carpetas por responsabilidad:", bold_prefix="• semana-9/frontend/: ")
add_p(doc, "Colección de componentes funcionales en PascalCase (`Header`, `Hero`, `MovieCard`, `MovieList`, `Footer`), cada uno con su archivo de estilos dedicado.", bold_prefix="  - src/components/: ")
add_p(doc, "Archivo `movies.js` con el arreglo de 8 películas detalladas (títulos, posters, sinopsis, clasificaciones, valoraciones y horarios).", bold_prefix="  - src/data/: ")
add_p(doc, "Variables de diseño CSS (`variables.css`) y hoja de estilos globales (`global.css`) con tema oscuro para la experiencia de cine.", bold_prefix="  - src/styles/: ")

# ==========================================
# III. PROYECTO REACT CON VITE Y DEV SERVER
# ==========================================
add_custom_heading(doc, "III. Creación y Puesta en Marcha con Vite", level=1)

add_p(doc, "Se verificó la versión de Node.js (v24 LTS) y se creó el proyecto mediante el comando `npm create vite@latest frontend -- --template react`. Posteriormente, se instalaron las dependencias del proyecto (`npm install`) y se validó la compilación de producción (`npm run build`) y el servidor de desarrollo (`npm run dev`):")

add_image_with_caption(doc, "captura_2_dev_server.png", "Ejecución de build y servidor de desarrollo Vite corriendo en http://localhost:5173/.")

add_p(doc, "Se limpió el andamiaje por defecto de Vite (logos svg de demostración, contadores y estilos genéricos) para dejar un `index.html` optimizado con tipografía Inter y un `main.jsx` limpio en modo estricto (`StrictMode`).")

# ==========================================
# IV. COMPONENTES FUNCIONALES Y PROPS FLOW
# ==========================================
add_custom_heading(doc, "IV. Componentes Funcionales y Flujo de Props", level=1)

add_p(doc, "La aplicación sigue el principio de responsabilidad única y flujo unidireccional de datos:", bold_prefix="Principio de Diseño: ")

add_image_with_caption(doc, "captura_4_props_flow.png", "Diagrama de jerarquía de componentes y flujo de datos mediante props en React.")

add_p(doc, "Componente raíz que importa los datos desde `src/data/movies.js`. Selecciona la película destacada y pasa las props correspondientes a `<Hero movie={featuredMovie} />` y `<MovieList movies={movies} />`.", bold_prefix="1. App.jsx: ")
add_p(doc, "Barra superior que muestra el logotipo CineStar DAE, enlaces de navegación y buscador. Es un componente presentacional puro.", bold_prefix="2. Header.jsx: ")
add_p(doc, "Recibe la película destacada mediante la prop `movie` y muestra su imagen de fondo (backdrop), título, calificación, sinopsis y horarios.", bold_prefix="3. Hero.jsx: ")
add_p(doc, "Recibe el arreglo completo mediante la prop `movies`. Incluye un selector de filtro por género y recorre el arreglo con `.map()` renderizando una tarjeta por película.", bold_prefix="4. MovieList.jsx: ")
add_p(doc, "Recibe una película individual mediante `props` y renderiza su poster, valoración en estrellas, badge de clasificación por edad, sinopsis y botones con horarios de funciones.", bold_prefix="5. MovieCard.jsx: ")
add_p(doc, "Pie de página institucional que contiene información de contacto, datos del estudiante (**Israel Angel Huaman Huaman**) y enlace al repositorio de GitHub.", bold_prefix="6. Footer.jsx: ")

add_p(doc, "Código representativo del paso de props e iteración con map en `MovieList.jsx` y `MovieCard.jsx`:")

add_code_block(doc, """// src/components/MovieList/MovieList.jsx (extracto)
export const MovieList = ({ movies }) => {
  return (
    <section id="cartelera" className="movie-list-section container">
      <h2 className="section-title">En Cartelera</h2>
      <div className="movies-grid">
        {movies.map(movie => (
          // Paso 9: Recorrido con map asignando la prop key única
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>
    </section>
  );
};

// src/components/MovieCard/MovieCard.jsx (extracto)
export const MovieCard = ({ movie }) => {
  return (
    <article className="movie-card">
      <img src={movie.poster} alt={movie.title} className="card-poster" />
      <div className="card-body">
        <span className="card-genre">{movie.genre}</span>
        <h3 className="card-title">{movie.title}</h3>
        <span className="card-rating">⭐ {movie.rating} / 10</span>
        <div className="card-schedules">
          {movie.schedules.map((time, idx) => (
            <button key={idx} className="btn-time-slot">{time}</button>
          ))}
        </div>
      </div>
    </article>
  );
};""")

# ==========================================
# V. INTERFAZ Y CARTELERA DE PELÍCULAS
# ==========================================
add_custom_heading(doc, "V. Interfaz de Usuario de la Cartelera de Cine", level=1)

add_p(doc, "Se implementó una interfaz visual moderna y responsiva orientada a salas de cine (CineStar DAE), con soporte para tema oscuro, tarjetas con elevación y sombras, badges de calificación y horarios interactivos:")

add_image_with_caption(doc, "captura_3_cartelera_web.png", "Interfaz de usuario renderizada en el navegador (CineStar DAE).")

add_p(doc, "La cartelera incluye las 8 películas requeridas por la guía, completamente documentadas con horarios y metadatos:")

movies_table_data = [
    ("N°", "Título", "Género", "Clasif.", "Rating", "Duración", "Horarios de Funciones"),
    ("1", "Dune: Parte Dos", "Sci-Fi / Aventura", "+14", "8.9", "166 min", "15:00, 18:15, 21:30, 23:45"),
    ("2", "Oppenheimer", "Drama / Biografía", "+14", "8.9", "180 min", "16:00, 19:40, 22:50"),
    ("3", "Spider-Man: Multiverso", "Animación / Acción", "Apt", "8.7", "140 min", "14:15, 17:00, 19:45"),
    ("4", "Interstellar", "Sci-Fi / Drama", "+14", "8.7", "169 min", "15:30, 18:45, 22:00"),
    ("5", "El Caballero de la Noche", "Acción / Crimen", "+14", "9.0", "152 min", "17:15, 20:30, 23:15"),
    ("6", "Avatar: Camino del Agua", "Aventura / Fantasía", "+14", "7.6", "192 min", "14:00, 17:45, 21:15"),
    ("7", "Blade Runner 2049", "Neo-noir / Sci-Fi", "+18", "8.0", "164 min", "16:45, 20:00, 22:45"),
    ("8", "El Origen (Inception)", "Sci-Fi / Acción", "+14", "8.8", "148 min", "15:15, 18:30, 21:45"),
]

tbl_mov = doc.add_table(rows=len(movies_table_data), cols=7)
tbl_mov.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_mov.autofit = False

col_widths = [Inches(0.4), Inches(1.8), Inches(1.2), Inches(0.6), Inches(0.5), Inches(0.7), Inches(1.3)]
for col_idx, width in enumerate(col_widths):
    tbl_mov.columns[col_idx].width = width

for row_idx, row_data in enumerate(movies_table_data):
    for col_idx, cell_value in enumerate(row_data):
        cell = tbl_mov.cell(row_idx, col_idx)
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
# VI. LOS TRES ERRORES TÍPICOS PROVOCADOS
# ==========================================
add_custom_heading(doc, "VI. Registro de los Tres Errores Provocados a Propósito", level=1)

add_p(doc, "Conforme al punto 11 del procedimiento, se provocaron tres errores conceptuales comunes en React para documentar sus causas, los mensajes exactos arrojados por el motor y la forma correcta de solucionarlos:")

add_image_with_caption(doc, "captura_5_errores.png", "Registro de advertencias y errores en consola de React y compilador Vite.")

add_p(doc, "En JSX, `class` es una palabra reservada de JavaScript. Al escribir `<header class=\"...\">`, React emite una advertencia en la consola de desarrollo: `Warning: Invalid DOM property 'class'. Did you mean 'className'?`. Solución: Usar siempre el atributo sintético `className`.", bold_prefix="1. Error 1 — Uso de 'class' en lugar de 'className': ")

add_p(doc, "Un componente de React debe retornar un único elemento raíz en el árbol del DOM virtual. Si se escriben dos elementos adyacentes como `return (<h1>A</h1> <p>B</p>)`, el compilador de JSX (Rollup / Vite) falla con: `SyntaxError: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX fragment <>...</>?`. Solución: Envolver los elementos en un Fragment `<>...</>` o en una etiqueta contenedora como `<div>`.", bold_prefix="2. Error 2 — Múltiples nodos raíz sin contenedor: ")

add_p(doc, "Al iterar un arreglo con `.map()` para generar elementos dinámicos, omitir la prop `key` impide que el algoritmo de reconciliación de React identifique qué elementos cambiaron o se agregaron. React emite la advertencia: `Warning: Each child in a list should have a unique 'key' prop. Check the render method of MovieList`. Solución: Proveer una clave única y estable como `key={movie.id}`.", bold_prefix="3. Error 3 — Olvidar la prop 'key' en map(): ")

# ==========================================
# VII. CONTROL DE VERSIONES EN GIT
# ==========================================
add_custom_heading(doc, "VII. Control de Versiones e Historial en GitHub", level=1)

add_p(doc, "Para asegurar la máxima nota en el Criterio 4 de la rúbrica y mantener la disciplina de versionado continuo, el desarrollo de la Semana 9 se estructuró en commits atómicos registrados en GitHub:")

add_image_with_caption(doc, "captura_6_git.png", "Historial de commits en GitHub demostrando avance progresivo a nombre de Israel Huaman.")

# ==========================================
# VIII. CONCLUSIONES
# ==========================================
add_custom_heading(doc, "VIII. Conclusiones", level=1)

add_p(doc, "1. La combinación de Vite con ReactJS proporciona un entorno de desarrollo con recarga en caliente (HMR) extremadamente rápido y una compilación de producción optimizada en paquetes estáticos de tamaño mínimo.")
add_p(doc, "2. La arquitectura basada en componentes funcionales promueve la reutilización y el principio de responsabilidad única, facilitando el mantenimiento y la escalabilidad de aplicaciones empresariales complejas.")
add_p(doc, "3. El flujo unidireccional de datos mediante `props` asegura que los componentes hijos sean predecibles e independientes de la procedencia de los datos, mejorando la testeabilidad de la interfaz.")
add_p(doc, "4. La comprensión de las advertencias del Virtual DOM (como la necesidad de `className`, nodos raíz encapsulados y claves únicas en listas iteradas) es crucial para evitar errores de renderizado y degradaciones de rendimiento en producción.")

doc.save(DOCX_PATH)
print("Documento Word guardado exitosamente en:", DOCX_PATH)
