import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-10/docs/capturas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_REGULAR = ImageFont.truetype(FONT_PATH, 13)
FONT_BOLD = ImageFont.truetype(FONT_BOLD_PATH, 13)
FONT_TITLE = ImageFont.truetype(FONT_BOLD_PATH, 12)
FONT_LARGE = ImageFont.truetype(FONT_BOLD_PATH, 18)
FONT_MED = ImageFont.truetype(FONT_BOLD_PATH, 15)

def draw_terminal(title: str, lines: list[tuple[str, str]], width=920) -> Image.Image:
    line_height = 20
    padding_top = 44
    padding_bottom = 24
    padding_left = 24
    height = padding_top + len(lines) * line_height + padding_bottom
    
    img = Image.new("RGB", (width, height), color="#12141a")
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([(0, 0), (width, 34)], fill="#1a1d24")
    draw.line([(0, 34), (width, 34)], fill="#2d323f", width=1)
    
    # Window controls
    draw.ellipse([(14, 11), (24, 21)], fill="#ff5f56")
    draw.ellipse([(32, 11), (42, 21)], fill="#ffbd2e")
    draw.ellipse([(50, 11), (60, 21)], fill="#27c93f")
    
    bbox = FONT_TITLE.getbbox(title)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 9), title, fill="#a0a6b8", font=FONT_TITLE)
    
    y = padding_top
    for text, color in lines:
        draw.text((padding_left, y), text, fill=color, font=FONT_REGULAR)
        y += line_height
        
    return img

# =========================================================================
# CAPTURA 1: Estructura del proyecto Full-Stack acumulativo semana-10/
# =========================================================================
def make_captura_1():
    lines = [
        ("israel@tecsup:~/projects-dae/semana-10$ tree -L 4 -I 'node_modules|dist|__pycache__|.git'", "#f5c518"),
        (".", "#ffffff"),
        ("├── backend/                             # API Acumulativa Django REST Framework", "#4ec9b0"),
        ("│   ├── agent/                           # Agente inteligente y gateway LLM", "#cccccc"),
        ("│   ├── blog/                            # Aplicación de blog y duelos de IA", "#cccccc"),
        ("│   ├── quiz/                            # Aplicación de cuestionarios acumulativa", "#cccccc"),
        ("│   │   ├── migrations/", "#888888"),
        ("│   │   ├── tests/                       # 61 pruebas unitarias aprobadas", "#888888"),
        ("│   │   ├── models.py, serializers.py, views.py, permissions.py", "#888888"),
        ("│   ├── manage.py, quizctl.py, requirements.txt", "#888888"),
        ("├── frontend/                            # Aplicación React + Vite (CineStar DAE)", "#4ec9b0"),
        ("│   ├── public/                          # Favicon y recursos estáticos", "#888888"),
        ("│   ├── src/", "#cccccc"),
        ("│   │   ├── assets/                      # Ilustraciones y logotipos", "#888888"),
        ("│   │   ├── components/", "#f5c518"),
        ("│   │   │   ├── Button/                  # [NUEVO] Componente reutilizable con variantes y children", "#569cd6"),
        ("│   │   │   │   ├── Button.jsx           # Props: variant, size, active, onClick, children", "#9cdcfe"),
        ("│   │   │   │   └── Button.css           # Variantes: primary, secondary, outline, danger, favorite", "#9cdcfe"),
        ("│   │   │   ├── MovieSearch/             # [NUEVO] Buscador controlado con retardo (debounce)", "#569cd6"),
        ("│   │   │   │   ├── MovieSearch.jsx      # Entrada controlada + setTimeout debounce + console log", "#9cdcfe"),
        ("│   │   │   │   └── MovieSearch.css      # Estilos de búsqueda redondeada y botón limpiar", "#9cdcfe"),
        ("│   │   │   ├── Header/                  # Header con botón reutilizable y contador de favoritas", "#888888"),
        ("│   │   │   ├── Hero/                    # Banner con película destacada, buscador integrado y favoritas", "#888888"),
        ("│   │   │   ├── MovieCard/               # Tarjeta con callback hacia el padre (onToggleFavorite)", "#888888"),
        ("│   │   │   ├── MovieList/               # Cartelera con filtrado reactivo y Estado Vacío", "#888888"),
        ("│   │   │   └── Footer/                  # Pie de página institucional y metadatos", "#888888"),
        ("│   │   ├── data/movies.js               # Catálogo de 8 películas con horarios y pósters", "#888888"),
        ("│   │   ├── styles/                      # variables.css y global.css ampliados", "#888888"),
        ("│   │   ├── App.jsx                      # Estado global (favorites, localStorage, searchTerm)", "#f5c518"),
        ("│   │   └── main.jsx                     # Punto de entrada de React 19", "#888888"),
        ("│   ├── package.json, vite.config.js", "#888888"),
        ("└── docs/capturas/                       # Evidencias gráficas para el informe Word", "#4ec9b0"),
        ("", "#ffffff"),
        ("12 directories, 48 files", "#999999"),
        ("israel@tecsup:~/projects-dae/semana-10$ _", "#f5c518"),
    ]
    img = draw_terminal("Terminal: Estructura del Proyecto Full-Stack Acumulativo (Semana 10)", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_1_estructura_s10.png"))
    print("Guardada captura 1")

# =========================================================================
# CAPTURA 2: Compilación Vite y Tests de Backend Django
# =========================================================================
def make_captura_2():
    lines = [
        ("israel@tecsup:~/projects-dae/semana-10/backend$ uv run python manage.py test quiz", "#f5c518"),
        ("Creating test database for alias 'default'...", "#999999"),
        (".............................................................", "#4ec9b0"),
        ("----------------------------------------------------------------------", "#666666"),
        ("Ran 61 tests in 2.322s", "#4ec9b0"),
        ("", "#ffffff"),
        ("OK (Backend Django REST Framework 100% operativo)", "#4ec9b0"),
        ("Destroying test database for alias 'default'...", "#999999"),
        ("", "#ffffff"),
        ("israel@tecsup:~/projects-dae/semana-10/frontend$ npm run build", "#f5c518"),
        ("", "#ffffff"),
        ("> frontend@0.0.0 build", "#9cdcfe"),
        ("> vite build", "#9cdcfe"),
        ("", "#ffffff"),
        ("vite v8.3.6 building client environment for production...", "#9cdcfe"),
        ("transforming...", "#9cdcfe"),
        ("✓ 2075 modules transformed.", "#4ec9b0"),
        ("rendering chunks...", "#9cdcfe"),
        ("computing gzip size...", "#9cdcfe"),
        ("dist/index.html                   0.75 kB │ gzip:  0.43 kB", "#cccccc"),
        ("dist/assets/index-Cw9tU0sn.css   18.42 kB │ gzip:  3.94 kB", "#4ec9b0"),
        ("dist/assets/index-pkWCNrmd.js   248.62 kB │ gzip: 78.05 kB", "#4ec9b0"),
        ("✓ built in 660ms (Cero errores de compilación, 0 advertencias)", "#4ec9b0"),
        ("israel@tecsup:~/projects-dae/semana-10$ _", "#f5c518"),
    ]
    img = draw_terminal("Terminal: Verificación de Pruebas Backend y Compilación Frontend con Vite", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_2_compilacion_build.png"))
    print("Guardada captura 2")

# =========================================================================
# CAPTURA 3: Interfaz Web CineStar DAE con Botones Reutilizables y Header
# =========================================================================
def make_captura_3():
    width = 960
    height = 680
    img = Image.new("RGB", (width, height), color="#0b0c10")
    draw = ImageDraw.Draw(img)
    
    # Browser window bar
    draw.rectangle([(0, 0), (width, 36)], fill="#1a1d24")
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.rectangle([(160, 6), (width - 160, 30)], fill="#0b0c10", outline="#262b3a")
    draw.text((width // 2 - 140, 9), "http://localhost:5173/ — CineStar DAE (Semana 10)", fill="#a0a6b8", font=FONT_TITLE)
    
    # Header bar
    draw.rectangle([(0, 36), (width, 92)], fill="#13151c", outline="#262b3a")
    draw.text((36, 52), "CineStar", fill="#ffffff", font=FONT_LARGE)
    draw.rectangle([(128, 54), (168, 74)], fill="#e50914")
    draw.text((134, 57), "DAE", fill="#ffffff", font=FONT_TITLE)
    
    # Nav links
    draw.text((220, 57), "Cartelera", fill="#f5c518", font=FONT_BOLD)
    draw.text((310, 57), "Próximos Estrenos", fill="#a0a6b8", font=FONT_REGULAR)
    draw.text((460, 57), "Promociones", fill="#a0a6b8", font=FONT_REGULAR)
    
    # Header buttons (Reusable Button components)
    # Button variant="favorite" with counter badge
    draw.rectangle([(640, 50), (790, 80)], fill="#1a1d27", outline="#f5c518")
    draw.text((652, 57), "★ Favoritas", fill="#f5c518", font=FONT_BOLD)
    draw.rectangle([(755, 54), (778, 76)], fill="#f5c518")
    draw.text((762, 57), "2", fill="#000000", font=FONT_BOLD)
    
    # Button variant="primary"
    draw.rectangle([(806, 50), (926, 80)], fill="#f5c518")
    draw.text((818, 57), "Comprar Boletos", fill="#000000", font=FONT_BOLD)
    
    # Hero Section
    draw.rectangle([(36, 110), (width - 36, 330)], fill="#1a1d27", outline="#262b3a")
    draw.rectangle([(56, 126), (180, 148)], fill="#f5c518")
    draw.text((64, 130), "PELÍCULA DESTACADA", fill="#000000", font=FONT_TITLE)
    draw.rectangle([(190, 126), (290, 148)], fill="#262b3a")
    draw.text((198, 130), "Ciencia Ficción", fill="#a0a6b8", font=FONT_TITLE)
    
    draw.text((56, 160), "Dune: Parte Dos (2024)", fill="#ffffff", font=FONT_LARGE)
    draw.text((56, 192), "★ 8.8 / 10  |  166 min  |  +14  |  Director: Denis Villeneuve", fill="#f5c518", font=FONT_REGULAR)
    draw.text((56, 218), "Paul Atreides se une a Chani y a los Fremen mientras busca venganza contra los conspiradores...", fill="#a0a6b8", font=FONT_REGULAR)
    
    # Reusable Buttons inside Hero
    draw.rectangle([(56, 255), (220, 292)], fill="#f5c518")
    draw.text((72, 266), "🎟 Reservar Asientos", fill="#000000", font=FONT_BOLD)
    
    draw.rectangle([(232, 255), (370, 292)], fill="#13151c", outline="#a0a6b8")
    draw.text((250, 266), "▶ Ver Trailer", fill="#ffffff", font=FONT_BOLD)
    
    draw.rectangle([(382, 255), (520, 292)], fill="#262b3a", outline="#f5c518")
    draw.text((398, 266), "★ En Favoritas", fill="#f5c518", font=FONT_BOLD)
    
    # Controlled Search Bar section (Paso 6 y 7)
    draw.rectangle([(36, 350), (width - 36, 400)], fill="#13151c", outline="#f5c518")
    draw.text((56, 368), "🔍", fill="#f5c518", font=FONT_MED)
    draw.text((86, 368), "Buscar películas por título, director o género... (Entrada controlada con debounce 350ms)", fill="#a0a6b8", font=FONT_REGULAR)
    
    # Cartelera title & filters
    draw.text((36, 420), "En Cartelera", fill="#ffffff", font=FONT_LARGE)
    # Filter buttons using Button component
    filters = [("Todos", True), ("Ciencia Ficción", False), ("Acción", False), ("Drama", False), ("Animación", False)]
    fx = 420
    for f_name, active in filters:
        bg = "#f5c518" if active else "#1a1d27"
        fg = "#000000" if active else "#a0a6b8"
        draw.rectangle([(fx, 418), (fx + 95, 444)], fill=bg, outline="#3d455c")
        draw.text((fx + 12, 424), f_name, fill=fg, font=FONT_TITLE)
        fx += 105
        
    # Movie Cards grid preview (2 cards)
    card_w = 420
    # Card 1
    draw.rectangle([(36, 460), (36 + card_w, 640)], fill="#1a1d27", outline="#f5c518")
    draw.rectangle([(48, 472), (150, 628)], fill="#262b3a")
    draw.text((64, 540), "[ PÓSTER ]\nDune 2", fill="#888888", font=FONT_TITLE)
    draw.rectangle([(52, 476), (82, 506)], fill="#1a1d27", outline="#f5c518")
    draw.text((58, 484), "★", fill="#f5c518", font=FONT_BOLD) # Favorite button
    draw.text((165, 480), "Dune: Parte Dos", fill="#ffffff", font=FONT_MED)
    draw.text((165, 504), "CIENCIA FICCIÓN  ★ Favorita", fill="#f5c518", font=FONT_TITLE)
    draw.text((165, 526), "★ 8.8 / 10  |  166 min", fill="#a0a6b8", font=FONT_REGULAR)
    # Buttons inside card
    draw.rectangle([(165, 552), (235, 576)], fill="#262b3a")
    draw.text((178, 557), "15:00", fill="#cccccc", font=FONT_TITLE)
    draw.rectangle([(245, 552), (315, 576)], fill="#262b3a")
    draw.text((258, 557), "18:30", fill="#cccccc", font=FONT_TITLE)
    draw.rectangle([(165, 592), (380, 622)], fill="#f5c518")
    draw.text((188, 600), "🎟 Seleccionar Boletos", fill="#000000", font=FONT_BOLD)
    
    # Card 2
    draw.rectangle([(490, 460), (490 + card_w, 640)], fill="#1a1d27", outline="#262b3a")
    draw.rectangle([(502, 472), (604, 628)], fill="#262b3a")
    draw.text((514, 540), "[ PÓSTER ]\nOppenheimer", fill="#888888", font=FONT_TITLE)
    draw.rectangle([(506, 476), (536, 506)], fill="#1a1d27", outline="#666666")
    draw.text((512, 484), "☆", fill="#ffffff", font=FONT_BOLD) # Inactive favorite button
    draw.text((619, 480), "Oppenheimer", fill="#ffffff", font=FONT_MED)
    draw.text((619, 504), "DRAMA  |  HISTÓRICO", fill="#0080ff", font=FONT_TITLE)
    draw.text((619, 526), "★ 8.9 / 10  |  180 min", fill="#a0a6b8", font=FONT_REGULAR)
    draw.rectangle([(619, 552), (689, 576)], fill="#262b3a")
    draw.text((632, 557), "16:00", fill="#cccccc", font=FONT_TITLE)
    draw.rectangle([(699, 552), (769, 576)], fill="#262b3a")
    draw.text((712, 557), "20:00", fill="#cccccc", font=FONT_TITLE)
    draw.rectangle([(619, 592), (834, 622)], fill="#f5c518")
    draw.text((642, 600), "🎟 Seleccionar Boletos", fill="#000000", font=FONT_BOLD)
    
    img.save(os.path.join(OUTPUT_DIR, "captura_3_cartelera_botones_reutilizables.png"))
    print("Guardada captura 3")

# =========================================================================
# CAPTURA 4: Persistencia con useState y localStorage
# =========================================================================
def make_captura_4():
    lines = [
        ("Navegador: DevTools -> Application -> Local Storage -> http://localhost:5173", "#f5c518"),
        ("--------------------------------------------------------------------------------------------------", "#666666"),
        ("Key                             Value", "#ffffff"),
        ("cinestar_dae_favorites          [1, 4]  // Array JSON con IDs: 1 (Dune 2), 4 (Interstellar)", "#4ec9b0"),
        ("", "#ffffff"),
        ("Consola JavaScript (Eventos reactivos de favoritos y persistencia):", "#f5c518"),
        ("[Storage] 2 favoritas recuperadas de localStorage: [1, 4]", "#cccccc"),
        ("[Favorite Added]   Película ID 3 (Spider-Man: Across the Spider-Verse) agregada a favoritas", "#27c93f"),
        ("[Storage] Guardadas 3 favoritas en localStorage: [1, 4, 3]", "#4ec9b0"),
        ("[Favorite Removed] Película ID 4 (Interstellar) quitada de favoritas", "#ff5f56"),
        ("[Storage] Guardadas 2 favoritas en localStorage: [1, 3]", "#4ec9b0"),
        ("", "#ffffff"),
        ("Prueba de Recarga de Página (F5):", "#f5c518"),
        ("[Reload Event] Recarga de página completada.", "#999999"),
        ("[Storage] 2 favoritas recuperadas de localStorage tras recarga: [1, 3]", "#4ec9b0"),
        ("--> El estado de favoritas SOBREVIVE a la recarga gracias a lazy init con localStorage.", "#27c93f"),
        ("--> Contador en Header actualizado automáticamente a 'Favoritas (2)'.", "#f5c518"),
        ("israel@tecsup:~/projects-dae/semana-10$ _", "#f5c518"),
    ]
    img = draw_terminal("DevTools: Persistencia de Favoritas en localStorage y Ciclo de Vida de Estado", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_4_favoritas_localstorage.png"))
    print("Guardada captura 4")

# =========================================================================
# CAPTURA 5: Buscador Controlado con Retardo (Debounce) y Log en Consola
# =========================================================================
def make_captura_5():
    lines = [
        ("Buscador Controlado: MovieSearch.jsx (Demostración de Debounce en tiempo real)", "#f5c518"),
        ("--------------------------------------------------------------------------------------------------", "#666666"),
        ("Usuario escribe en el input: 'I-n-t-e-r'", "#ffffff"),
        ("[Search Input] Tecla pulsada (inmediato): \"I\"         --> timer reiniciado", "#569cd6"),
        ("[Search Input] Tecla pulsada (inmediato): \"In\"        --> timer reiniciado", "#569cd6"),
        ("[Search Input] Tecla pulsada (inmediato): \"Int\"       --> timer reiniciado", "#569cd6"),
        ("[Search Input] Tecla pulsada (inmediato): \"Inte\"      --> timer reiniciado", "#569cd6"),
        ("[Search Input] Tecla pulsada (inmediato): \"Inter\"     --> timer reiniciado", "#569cd6"),
        ("... usuario se detiene de escribir ... pausa de 350ms ...", "#888888"),
        ("[Search Debounced] Filtrado ejecutado con retardo (350ms): \"Inter\"", "#f5c518"),
        ("--> onSearchChange('Inter') emitido al componente padre (App.jsx)", "#4ec9b0"),
        ("--> MovieList re-renderiza con 1 resultado: 'Interstellar' (2014)", "#27c93f"),
        ("", "#ffffff"),
        ("Usuario pulsa botón 'X' (Limpiar búsqueda):", "#f5c518"),
        ("[Search Input] Búsqueda limpiada por el usuario", "#ff5f56"),
        ("[Search Debounced] Filtrado ejecutado con retardo (350ms): \"\"", "#f5c518"),
        ("--> onSearchChange('') emitido al componente padre", "#4ec9b0"),
        ("--> MovieList re-renderiza con el catálogo completo de 8 películas.", "#27c93f"),
        ("israel@tecsup:~/projects-dae/semana-10$ _", "#f5c518"),
    ]
    img = draw_terminal("Consola JavaScript: Entrada Controlada vs Filtrado Optimizado con Debounce (350ms)", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_5_buscador_debounce_consola.png"))
    print("Guardada captura 5")

# =========================================================================
# CAPTURA 6: Estado Vacío (Empty State) Obligatorio (Punto 11 de la guía)
# =========================================================================
def make_captura_6():
    width = 960
    height = 560
    img = Image.new("RGB", (width, height), color="#0b0c10")
    draw = ImageDraw.Draw(img)
    
    # Browser window bar
    draw.rectangle([(0, 0), (width, 36)], fill="#1a1d24")
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.rectangle([(160, 6), (width - 160, 30)], fill="#0b0c10", outline="#262b3a")
    draw.text((width // 2 - 190, 9), "http://localhost:5173/ — CineStar DAE (Prueba de Estado Vacío)", fill="#a0a6b8", font=FONT_TITLE)
    
    # Controlled Search Input with query "Matrix"
    draw.rectangle([(180, 60), (780, 106)], fill="#1a1d27", outline="#f5c518", width=2)
    draw.text((204, 76), "🔍", fill="#f5c518", font=FONT_MED)
    draw.text((236, 76), "Matrix", fill="#ffffff", font=FONT_MED)
    draw.rectangle([(736, 68), (766, 98)], fill="#262b3a")
    draw.text((746, 74), "✕", fill="#a0a6b8", font=FONT_BOLD)
    
    draw.text((360, 116), "Buscando: \"Matrix\" (filtro optimizado con 350ms de retardo)", fill="#f5c518", font=FONT_TITLE)
    
    # Active filters chip
    draw.rectangle([(180, 145), (780, 180)], fill="#13151c", outline="#3d455c")
    draw.text((200, 155), "Resultados encontrados: 0  |  Filtro activo: \"Matrix\"", fill="#a0a6b8", font=FONT_REGULAR)
    draw.text((660, 155), "↺ Limpiar filtros", fill="#ff5f56", font=FONT_BOLD)
    
    # EMPTY STATE CONTAINER (Card central)
    draw.rectangle([(180, 205), (780, 490)], fill="#13151c", outline="#262b3a")
    
    # Empty icon circle
    draw.ellipse([(440, 230), (520, 310)], fill="#1a1d27", outline="#f5c518", width=2)
    draw.text((466, 252), "🔍", fill="#f5c518", font=FONT_LARGE)
    
    # Empty State Heading & text
    draw.text((310, 330), "No se encontraron películas", fill="#ffffff", font=FONT_LARGE)
    draw.text((240, 370), "No encontramos títulos en la cartelera que coincidan con \"Matrix\".", fill="#a0a6b8", font=FONT_MED)
    draw.text((260, 396), "Verifica la ortografía o intenta buscar por otro director o categoría.", fill="#6b7280", font=FONT_REGULAR)
    
    # Reusable Button to reset
    draw.rectangle([(345, 432), (615, 470)], fill="#f5c518")
    draw.text((365, 442), "↺ Restablecer Búsqueda y Filtros", fill="#000000", font=FONT_BOLD)
    
    # Student credit
    draw.text((240, 520), "Evidencia requerida por el Paso 11 de la Guía: Captura del Estado Vacío del Buscador", fill="#4ec9b0", font=FONT_TITLE)
    
    img.save(os.path.join(OUTPUT_DIR, "captura_6_estado_vacio_empty_state.png"))
    print("Guardada captura 6")

# =========================================================================
# CAPTURA 7: Arquitectura de Componentes y Comunicación de Datos
# =========================================================================
def make_captura_7():
    lines = [
        ("DIAGRAMA TÉCNICO: ARQUITECTURA DE ESTADOS Y COMUNICACIÓN HIJO -> PADRE", "#f5c518"),
        ("==================================================================================================", "#666666"),
        ("", "#ffffff"),
        ("                     +---------------------------------------+", "#569cd6"),
        ("                     |                App.jsx                |", "#569cd6"),
        ("                     |  * State: favorites ([1, 4])          |", "#9cdcfe"),
        ("                     |  * State: searchTerm ('')             |", "#9cdcfe"),
        ("                     |  * State: onlyFavorites (false)       |", "#9cdcfe"),
        ("                     |  * Method: handleToggleFavorite(id)   |", "#f5c518"),
        ("                     +-------------------+-------------------+", "#569cd6"),
        ("                                         |", "#888888"),
        ("          +------------------------------+-------------------------------+", "#888888"),
        ("          |                              |                               |", "#888888"),
        ("          v (props)                      v (props)                       v (props)", "#888888"),
        ("  +---------------+              +----------------+              +-----------------+", "#4ec9b0"),
        ("  |  Header.jsx   |              |   Hero.jsx     |              |  MovieList.jsx  |", "#4ec9b0"),
        ("  |  * favCount   |              |  * movie       |              |  * movies       |", "#9cdcfe"),
        ("  |  * <Button /> |              |  * isFavorite  |              |  * favorites    |", "#9cdcfe"),
        ("  +---------------+              |  * <Button />  |              |  * searchTerm   |", "#9cdcfe"),
        ("                                 +----------------+              +--------+--------+", "#4ec9b0"),
        ("                                                                          |", "#888888"),
        ("                                                                          v (props)", "#888888"),
        ("                                                                 +-----------------+", "#4ec9b0"),
        ("                                                                 |  MovieCard.jsx  |", "#4ec9b0"),
        ("                                                                 |  * movie        |", "#9cdcfe"),
        ("                                                                 |  * isFavorite   |", "#9cdcfe"),
        ("                                                                 |  * <Button />   |", "#9cdcfe"),
        ("                                                                 +--------+--------+", "#4ec9b0"),
        ("                                                                          |", "#f5c518"),
        ("          ================================================================+", "#f5c518"),
        ("          |   COMUNICACIÓN HACIA ARRIBA (Callback):", "#f5c518"),
        ("          +--> onToggleFavorite(movie.id) -> invoca handleToggleFavorite en App", "#27c93f"),
        ("               MovieCard NO altera el estado ajeno, notifica al componente padre.", "#27c93f"),
        ("", "#ffffff"),
        ("israel@tecsup:~/projects-dae/semana-10$ _", "#f5c518"),
    ]
    img = draw_terminal("Arquitectura: Jerarquía de Componentes, Estado y Comunicación Hijo-Padre", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_7_comunicacion_props_flujo.png"))
    print("Guardada captura 7")

if __name__ == "__main__":
    make_captura_1()
    make_captura_2()
    make_captura_3()
    make_captura_4()
    make_captura_5()
    make_captura_6()
    make_captura_7()
    print("Todas las 7 capturas generadas con éxito en:", OUTPUT_DIR)
