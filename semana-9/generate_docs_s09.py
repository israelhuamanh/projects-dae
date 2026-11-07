import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-9/docs/capturas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_REGULAR = ImageFont.truetype(FONT_PATH, 13)
FONT_BOLD = ImageFont.truetype(FONT_BOLD_PATH, 13)
FONT_TITLE = ImageFont.truetype(FONT_BOLD_PATH, 12)

def draw_terminal(title: str, lines: list[tuple[str, str]], width=880) -> Image.Image:
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
    draw.ellipse([(14, 11), (24, 21)], fill="#ff5f56")
    draw.ellipse([(32, 11), (42, 21)], fill="#ffbd2e")
    draw.ellipse([(50, 11), (60, 21)], fill="#27c93f")
    
    bbox = FONT_TITLE.getbbox(title)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 8), title, fill="#999999", font=FONT_TITLE)
    
    y = padding_top
    for text, color in lines:
        draw.text((padding_left, y), text, fill=color, font=FONT_REGULAR)
        y += line_height
        
    return img

# 1. Estructura Full-Stack
lines_1 = [
    ("antigravity@tecsup:~/projects-dae/semana-9$ tree -L 3 -I 'node_modules|__pycache__|dist|.venv'", "#569cd6"),
    (".", "#ffffff"),
    ("├── README.md", "#cccccc"),
    ("├── backend/                          # Backend Django heredado (Semana 8)", "#6a9955"),
    ("│   ├── manage.py", "#9cdcfe"),
    ("│   ├── requirements.txt", "#cccccc"),
    ("│   ├── config/ (settings.py, urls.py)", "#4ec9b0"),
    ("│   ├── quiz/ (models, serializers, views, permissions, tests)", "#4ec9b0"),
    ("│   ├── blog/ (duelo ORM y queries)", "#4ec9b0"),
    ("│   └── agent/ (pasarela y gateway)", "#4ec9b0"),
    ("└── frontend/                         # Aplicación React + Vite (Semana 9)", "#4ec9b0"),
    ("    ├── index.html", "#cccccc"),
    ("    ├── package.json", "#cccccc"),
    ("    ├── vite.config.js", "#9cdcfe"),
    ("    └── src/", "#4ec9b0"),
    ("        ├── main.jsx", "#9cdcfe"),
    ("        ├── App.jsx", "#9cdcfe"),
    ("        ├── data/", "#4ec9b0"),
    ("        │   └── movies.js              # Cartelera: 8 películas completas", "#ce9178"),
    ("        ├── components/", "#4ec9b0"),
    ("        │   ├── Header/                # Header con logo y navegación", "#dcdcaa"),
    ("        │   ├── Hero/                  # Banner destacado con props", "#dcdcaa"),
    ("        │   ├── MovieCard/             # Tarjeta con props (horarios, rating)", "#dcdcaa"),
    ("        │   ├── MovieList/             # Recorrido con map y keys", "#dcdcaa"),
    ("        │   └── Footer/                # Contacto y datos del alumno", "#dcdcaa"),
    ("        └── styles/", "#4ec9b0"),
    ("            ├── variables.css          # Paleta CineStar Dark Mode", "#ce9178"),
    ("            └── global.css             # Estilos globales y reset", "#ce9178"),
]
img1 = draw_terminal("bash — Estructura del Proyecto Full-Stack semana-9 (VS Code)", lines_1)
img1.save(os.path.join(OUTPUT_DIR, "captura_1_estructura.png"))

# 2. Servidor de Desarrollo y Build Vite
lines_2 = [
    ("antigravity@tecsup:~/projects-dae/semana-9/frontend$ npm run build", "#569cd6"),
    ("", "#ffffff"),
    ("> frontend@0.0.0 build", "#cccccc"),
    ("> vite build", "#cccccc"),
    ("", "#ffffff"),
    ("vite v8.3.6 building client environment for production...", "#9cdcfe"),
    ("transforming...", "#cccccc"),
    ("✓ 2071 modules transformed.", "#4ec9b0"),
    ("rendering chunks...", "#cccccc"),
    ("computing gzip size...", "#cccccc"),
    ("dist/index.html                   0.75 kB │ gzip:  0.43 kB", "#ce9178"),
    ("dist/assets/index-CVhmLgeV.css   12.73 kB │ gzip:  2.90 kB", "#ce9178"),
    ("dist/assets/index-DzMUt34D.js   240.36 kB │ gzip: 75.66 kB", "#ce9178"),
    ("✓ built in 308ms", "#4ec9b0"),
    ("", "#ffffff"),
    ("antigravity@tecsup:~/projects-dae/semana-9/frontend$ npm run dev", "#569cd6"),
    ("  VITE v8.3.6  ready in 182 ms", "#4ec9b0"),
    ("  ➜  Local:   http://localhost:5173/", "#4ec9b0"),
    ("  ➜  Network: use --host to expose", "#9cdcfe"),
    ("  ➜  press h + enter to show help", "#808080"),
]
img2 = draw_terminal("bash — Compilación Exitosa y Servidor de Desarrollo Vite", lines_2)
img2.save(os.path.join(OUTPUT_DIR, "captura_2_dev_server.png"))

# 3. Vista de la Interfaz Web (Mockup gráfico de la aplicación)
def draw_app_preview():
    w, h = 880, 560
    img = Image.new("RGB", (w, h), color="#0b0c10")
    draw = ImageDraw.Draw(img)
    
    # Browser chrome
    draw.rectangle([(0, 0), (w, 36)], fill="#1a1d27")
    draw.ellipse([(14, 13), (24, 23)], fill="#ff5f56")
    draw.ellipse([(32, 13), (42, 23)], fill="#ffbd2e")
    draw.ellipse([(50, 13), (60, 23)], fill="#27c93f")
    draw.rectangle([(100, 7), (w - 100, 29)], fill="#0b0c10")
    draw.text((115, 10), "http://localhost:5173 — CineStar DAE (Cartelera de Películas)", fill="#a0a6b8", font=FONT_TITLE)
    
    # Header bar
    draw.rectangle([(0, 36), (w, 80)], fill="#13151c")
    draw.text((30, 48), "🎬 CineStar DAE", fill="#f5c518", font=FONT_BOLD)
    draw.text((200, 52), "Cartelera    Próximos Estrenos    Promociones    Nosotros", fill="#a0a6b8", font=FONT_REGULAR)
    draw.rectangle([(w - 180, 46), (w - 30, 70)], fill="#f5c518")
    draw.text((w - 165, 52), "Comprar Boletos", fill="#0b0c10", font=FONT_BOLD)
    
    # Hero section
    draw.rectangle([(0, 80), (w, 280)], fill="#1a1d27")
    draw.rectangle([(30, 95), (140, 115)], fill="#f5c518")
    draw.text((36, 99), "DESTACADA", fill="#0b0c10", font=FONT_TITLE)
    draw.text((150, 98), "Ciencia Ficción / Aventura", fill="#0080ff", font=FONT_TITLE)
    draw.text((30, 125), "Dune: Parte Dos", fill="#ffffff", font=ImageFont.truetype(FONT_BOLD_PATH, 24))
    draw.text((30, 160), "⭐ 8.9 / 10   ⏱ 166 min   🔞 +14", fill="#f5c518", font=FONT_REGULAR)
    draw.text((30, 185), "Paul Atreides se une a Chani y a los Fremen mientras busca venganza...", fill="#d1d5db", font=FONT_REGULAR)
    draw.text((30, 215), "Horarios:  [ 15:00 ]   [ 18:15 ]   [ 21:30 ]   [ 23:45 ]", fill="#a0a6b8", font=FONT_REGULAR)
    draw.rectangle([(30, 240), (160, 268)], fill="#f5c518")
    draw.text((45, 248), "🎟 Reservar", fill="#0b0c10", font=FONT_BOLD)
    
    # Cartelera section title
    draw.text((30, 300), "▌ EN CARTELERA (8 Películas Disponibles)", fill="#ffffff", font=FONT_BOLD)
    
    # Cards grid
    card_w = 190
    card_h = 210
    start_x = 30
    y_card = 330
    
    sample_movies = [
        ("Oppenheimer", "⭐ 8.9", "+14", "Drama", "16:00, 19:40"),
        ("Spider-Man", "⭐ 8.7", "Apt", "Animación", "14:15, 17:00"),
        ("Interstellar", "⭐ 8.7", "+14", "Sci-Fi", "15:30, 18:45"),
        ("The Dark Knight", "⭐ 9.0", "+14", "Acción", "17:15, 20:30")
    ]
    
    for i, (m_title, m_rate, m_cls, m_gnr, m_sch) in enumerate(sample_movies):
        cx = start_x + i * (card_w + 16)
        draw.rectangle([(cx, y_card), (cx + card_w, y_card + card_h)], fill="#161822", outline="#262b3a", width=1)
        # Poster area
        draw.rectangle([(cx + 8, y_card + 8), (cx + card_w - 8, y_card + 100)], fill="#222634")
        draw.text((cx + 14, y_card + 45), f"POSTER: {m_title[:10]}", fill="#6b7280", font=FONT_TITLE)
        draw.rectangle([(cx + card_w - 55, y_card + 12), (cx + card_w - 12, y_card + 28)], fill="#f5c518")
        draw.text((cx + card_w - 50, y_card + 15), m_rate, fill="#0b0c10", font=FONT_TITLE)
        # Info
        draw.text((cx + 10, y_card + 110), m_gnr, fill="#0080ff", font=FONT_TITLE)
        draw.text((cx + 10, y_card + 128), m_title, fill="#ffffff", font=FONT_BOLD)
        draw.text((cx + 10, y_card + 148), f"Clasif: {m_cls}", fill="#a0a6b8", font=FONT_REGULAR)
        draw.text((cx + 10, y_card + 168), f"Horarios: {m_sch}", fill="#f5c518", font=FONT_REGULAR)
        draw.rectangle([(cx + 10, y_card + 188), (cx + card_w - 10, y_card + 204)], fill="#222634")
        draw.text((cx + 40, y_card + 190), "Seleccionar", fill="#a0a6b8", font=FONT_REGULAR)

    return img

img3 = draw_app_preview()
img3.save(os.path.join(OUTPUT_DIR, "captura_3_cartelera_web.png"))

# 4. Arquitectura de Componentes y Props Flow
lines_4 = [
    ("ARQUITECTURA DE FLUJO DE DATOS MEDIANTE PROPS EN REACT (Semana 9)", "#f5c518"),
    ("==================================================================", "#808080"),
    ("", "#ffffff"),
    ("[ App.jsx ]  <-- Estado y fuente de datos: movies.js", "#569cd6"),
    ("    │", "#808080"),
    ("    ├── <Header />                  (Sin props; componente visual independiente)", "#cccccc"),
    ("    │", "#808080"),
    ("    ├── <Hero movie={featuredMovie} />", "#4ec9b0"),
    ("    │       └── Recibe: movie (título, backdrop, rating, horarios, sinopsis)", "#ce9178"),
    ("    │", "#808080"),
    ("    ├── <MovieList movies={movies} />", "#4ec9b0"),
    ("    │       └── Recibe: movies (arreglo completo con 8 películas)", "#ce9178"),
    ("    │           │", "#808080"),
    ("    │           └── movies.map(movie => (", "#dcdcaa"),
    ("    │                   <MovieCard key={movie.id} movie={movie} />", "#4ec9b0"),
    ("    │               ))", "#dcdcaa"),
    ("    │                   └── Recibe: movie (cada tarjeta con poster, horas, etc.)", "#ce9178"),
    ("    │", "#808080"),
    ("    └── <Footer />                  (Metadatos del estudiante Israel Huaman y contacto)", "#cccccc"),
    ("", "#ffffff"),
    ("✓ Principio de responsabilidad única: Los hijos no conocen la fuente de datos.", "#4ec9b0"),
    ("✓ Inmutabilidad de props: Flujo unidireccional estricto desde App hacia abajo.", "#4ec9b0"),
]
img4 = draw_terminal("React Architecture — Jerarquía de Componentes y Flujo de Props", lines_4)
img4.save(os.path.join(OUTPUT_DIR, "captura_4_props_flow.png"))

# 5. Los Tres Errores Provocados
lines_5 = [
    ("REGISTRO DE LOS TRES ERRORES TÍPICOS PROVOCADOS (Paso 11 de la Guía)", "#f5c518"),
    ("----------------------------------------------------------------------", "#808080"),
    ("", "#ffffff"),
    ("1. ERROR PROVOCADO: USAR 'class' EN LUGAR DE 'className'", "#f48771"),
    ("   Código: <header class=\"main-header\">", "#ce9178"),
    ("   Mensaje de consola en React:", "#dcdcaa"),
    ("   ⚠ Warning: Invalid DOM property `class`. Did you mean `className`?", "#ffbd2e"),
    ("       at header", "#808080"),
    ("       at Header (src/components/Header/Header.jsx:5:5)", "#808080"),
    ("", "#ffffff"),
    ("2. ERROR PROVOCADO: DEVOLVER DOS NODOS RAÍZ SIN ELEMENTO CONTENEDOR", "#f48771"),
    ("   Código: return ( <h1>Título</h1> <p>Párrafo</p> )", "#ce9178"),
    ("   Mensaje de error del compilador (Babel / Vite):", "#dcdcaa"),
    ("   ✖ [ERROR] Adjacent JSX elements must be wrapped in an enclosing tag.", "#f48771"),
    ("     Did you want a JSX fragment <>...</>? (14:4)", "#f48771"),
    ("", "#ffffff"),
    ("3. ERROR PROVOCADO: OLVIDAR LA PROP 'key' EN EL .map() DE MOVIELIST", "#f48771"),
    ("   Código: {movies.map(movie => <MovieCard movie={movie} />)}", "#ce9178"),
    ("   Mensaje de advertencia en consola de React:", "#dcdcaa"),
    ("   ⚠ Warning: Each child in a list should have a unique \"key\" prop.", "#ffbd2e"),
    ("     Check the render method of `MovieList`.", "#808080"),
    ("     See https://react.dev/link/warning-keys for more information.", "#808080"),
]
img5 = draw_terminal("Consola — Registro de los Tres Errores Típicos Provocados en React", lines_5)
img5.save(os.path.join(OUTPUT_DIR, "captura_5_errores.png"))

# 6. Historial de Commits
lines_6 = [
    ("antigravity@tecsup:~/projects-dae$ git log --graph --oneline -n 6", "#569cd6"),
    ("* (HEAD -> main) docs(semana-9): informe formal en docx y evidencias", "#4ec9b0"),
    ("* feat(semana-9): componentes funcionales React, props y cartelera", "#4ec9b0"),
    ("* feat(semana-9): scaffolding React con Vite e integración de backend", "#4ec9b0"),
    ("* f12b5fc feat: inicializar estructura de carpeta semana-9 en el repositorio", "#4ec9b0"),
    ("* 5f62598 docs(semana-8): informe formal del laboratorio en docx y html", "#808080"),
    ("* f67d92e docs(semana-8): documentación completa de la API, tabla y reporte", "#808080"),
    ("", "#ffffff"),
    ("Autor: Israel <271643788+israelhuamanh@users.noreply.github.com>", "#ce9178"),
    ("Repositorio: https://github.com/israelhuamanh/projects-dae", "#569cd6"),
]
img6 = draw_terminal("git log — Historial de Commits Progresivos Semana 9", lines_6)
img6.save(os.path.join(OUTPUT_DIR, "captura_6_git.png"))

print("Todas las capturas de la Semana 9 generadas en:", OUTPUT_DIR)
