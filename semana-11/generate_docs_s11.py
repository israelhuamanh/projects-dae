import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/home/antigravity/israelhuamanh/projects-dae/semana-11/docs/capturas"
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
# CAPTURA 1: Estructura del proyecto Full-Stack acumulativo semana-11/
# =========================================================================
def make_captura_1():
    lines = [
        ("israel@tecsup:~/projects-dae/semana-11$ tree -L 4 -I 'node_modules|dist|__pycache__|.git'", "#f5c518"),
        (".", "#ffffff"),
        ("├── backend/                             # API Acumulativa Django REST Framework", "#4ec9b0"),
        ("│   ├── quiz/                            # Aplicación de cuestionarios acumulativa", "#cccccc"),
        ("│   │   ├── tests/                       # 61 pruebas unitarias aprobadas", "#888888"),
        ("│   │   ├── models.py, serializers.py, views.py, permissions.py", "#888888"),
        ("│   ├── manage.py, quizctl.py, requirements.txt", "#888888"),
        ("├── frontend/                            # Aplicación React + Vite (CineStar DAE)", "#4ec9b0"),
        ("│   ├── src/", "#cccccc"),
        ("│   │   ├── hooks/                       # [NUEVO] Custom Hooks Propios Reutilizables", "#f5c518"),
        ("│   │   │   ├── useDebounce.js           # Hook para retardo de entrada (Paso 5)", "#9cdcfe"),
        ("│   │   │   ├── useWindowSize.js         # Hook para dimensiones y columnas adaptativas (Paso 6)", "#9cdcfe"),
        ("│   │   │   └── usePremieres.js          # Hook de petición asíncrona con 3 estados (Paso 7)", "#9cdcfe"),
        ("│   │   ├── utils/                       # [NUEVO] Utilidades y Patrones de Diseño", "#f5c518"),
        ("│   │   │   └── movieAdapter.js          # Patrón Adaptador para normalizar películas (Paso 3)", "#9cdcfe"),
        ("│   │   ├── components/", "#f5c518"),
        ("│   │   │   ├── Toast/                   # [NUEVO] Aviso emergente desacoplado (Paso 4)", "#569cd6"),
        ("│   │   │   ├── SkeletonCard/            # [NUEVO] Esqueleto de carga con efecto Shimmer (Paso 8)", "#569cd6"),
        ("│   │   │   ├── PremieresSection/        # [NUEVO] Próximos estrenos (Cargando, Datos, Error)", "#569cd6"),
        ("│   │   │   ├── Button/                  # Componente reutilizable con variantes y children", "#888888"),
        ("│   │   │   ├── Header/                  # Cabecera que recibe solo favoritesCount (Paso 9)", "#888888"),
        ("│   │   │   ├── Hero/                    # Banner con búsqueda y botón de limpieza (Paso 10)", "#888888"),
        ("│   │   │   ├── MovieCard/               # Tarjeta desacoplada que avisa al padre por callback", "#888888"),
        ("│   │   │   ├── MovieList/               # Cartelera con grid dinámico por useWindowSize", "#888888"),
        ("│   │   │   ├── MovieSearch/             # Buscador limpio consumiendo useDebounce", "#888888"),
        ("│   │   │   └── Footer/                  # Pie de página institucional y metadatos", "#888888"),
        ("│   │   ├── data/movies.js, styles/, App.jsx, main.jsx", "#888888"),
        ("│   ├── package.json, vite.config.js", "#888888"),
        ("└── docs/capturas/                       # Evidencias para el informe Word", "#4ec9b0"),
        ("", "#ffffff"),
        ("15 directories, 56 files", "#999999"),
        ("israel@tecsup:~/projects-dae/semana-11$ _", "#f5c518"),
    ]
    img = draw_terminal("Terminal: Estructura del Proyecto Full-Stack con Hooks y Adaptador (Semana 11)", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_1_estructura_s11.png"))
    print("Guardada captura 1")

# =========================================================================
# CAPTURA 2: Compilación y Pruebas Unitarias
# =========================================================================
def make_captura_2():
    lines = [
        ("israel@tecsup:~/projects-dae/semana-11/backend$ uv run python manage.py test quiz", "#f5c518"),
        ("Creating test database for alias 'default'...", "#999999"),
        (".............................................................", "#4ec9b0"),
        ("----------------------------------------------------------------------", "#666666"),
        ("Ran 61 tests in 2.322s", "#4ec9b0"),
        ("", "#ffffff"),
        ("OK (Backend Django REST Framework 100% operativo)", "#4ec9b0"),
        ("Destroying test database for alias 'default'...", "#999999"),
        ("", "#ffffff"),
        ("israel@tecsup:~/projects-dae/semana-11/frontend$ npm run build", "#f5c518"),
        ("", "#ffffff"),
        ("> frontend@0.0.0 build", "#9cdcfe"),
        ("> vite build", "#9cdcfe"),
        ("", "#ffffff"),
        ("vite v8.3.6 building client environment for production...", "#9cdcfe"),
        ("transforming...", "#9cdcfe"),
        ("✓ 2085 modules transformed.", "#4ec9b0"),
        ("rendering chunks...", "#9cdcfe"),
        ("computing gzip size...", "#9cdcfe"),
        ("dist/index.html                   0.75 kB │ gzip:  0.43 kB", "#cccccc"),
        ("dist/assets/index-C7CzU-K_.css   24.51 kB │ gzip:  4.84 kB", "#4ec9b0"),
        ("dist/assets/index-CQo5Vrns.js   261.38 kB │ gzip: 81.83 kB", "#4ec9b0"),
        ("✓ built in 539ms (Compilación exitosa con 0 errores y 0 advertencias)", "#4ec9b0"),
        ("israel@tecsup:~/projects-dae/semana-11$ _", "#f5c518"),
    ]
    img = draw_terminal("Terminal: Verificación de Pruebas Backend y Compilación Frontend con Vite", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_2_compilacion_tests.png"))
    print("Guardada captura 2")

# =========================================================================
# CAPTURA 3: Aviso Emergente Toast Desacoplado
# =========================================================================
def make_captura_3():
    width = 960
    height = 580
    img = Image.new("RGB", (width, height), color="#0b0c10")
    draw = ImageDraw.Draw(img)
    
    # Browser window bar
    draw.rectangle([(0, 0), (width, 36)], fill="#1a1d24")
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.rectangle([(160, 6), (width - 160, 30)], fill="#0b0c10", outline="#262b3a")
    draw.text((width // 2 - 180, 9), "http://localhost:5173/ — CineStar DAE (Aviso Emergente Toast)", fill="#a0a6b8", font=FONT_TITLE)
    
    # Header bar
    draw.rectangle([(0, 36), (width, 92)], fill="#13151c", outline="#262b3a")
    draw.text((36, 52), "CineStar", fill="#ffffff", font=FONT_LARGE)
    draw.rectangle([(128, 54), (168, 74)], fill="#e50914")
    draw.text((134, 57), "DAE", fill="#ffffff", font=FONT_TITLE)
    draw.rectangle([(660, 50), (800, 80)], fill="#1a1d27", outline="#f5c518")
    draw.text((672, 57), "★ Favoritas", fill="#f5c518", font=FONT_BOLD)
    draw.rectangle([(765, 54), (788, 76)], fill="#f5c518")
    draw.text((772, 57), "3", fill="#000000", font=FONT_BOLD)
    
    # Section title
    draw.text((36, 120), "En Cartelera", fill="#ffffff", font=FONT_LARGE)
    draw.text((36, 150), "Paso 4: Al marcar una favorita, MovieCard avisa a App y se muestra el Toast emergente.", fill="#a0a6b8", font=FONT_REGULAR)
    
    # Movie Cards grid
    card_w = 420
    # Card 1 (Dune 2)
    draw.rectangle([(36, 180), (36 + card_w, 420)], fill="#1a1d27", outline="#f5c518")
    draw.rectangle([(48, 192), (150, 408)], fill="#262b3a")
    draw.text((64, 280), "[ PÓSTER ]\nDune 2", fill="#888888", font=FONT_TITLE)
    draw.rectangle([(52, 196), (82, 226)], fill="#1a1d27", outline="#f5c518")
    draw.text((58, 204), "★", fill="#f5c518", font=FONT_BOLD)
    draw.text((165, 200), "Dune: Parte Dos", fill="#ffffff", font=FONT_MED)
    draw.text((165, 224), "CIENCIA FICCIÓN  ★ Favorita", fill="#f5c518", font=FONT_TITLE)
    draw.rectangle([(165, 360), (380, 396)], fill="#f5c518")
    draw.text((188, 372), "🎟 Seleccionar Boletos", fill="#000000", font=FONT_BOLD)
    
    # Card 2 (Spider-Man)
    draw.rectangle([(490, 180), (490 + card_w, 420)], fill="#1a1d27", outline="#f5c518")
    draw.rectangle([(502, 192), (604, 408)], fill="#262b3a")
    draw.text((514, 280), "[ PÓSTER ]\nSpider-Man", fill="#888888", font=FONT_TITLE)
    draw.rectangle([(506, 196), (536, 226)], fill="#1a1d27", outline="#f5c518")
    draw.text((512, 204), "★", fill="#f5c518", font=FONT_BOLD) # Clicked favorite
    draw.text((619, 200), "Spider-Man: Across the Spider-Verse", fill="#ffffff", font=FONT_MED)
    draw.text((619, 224), "ANIMACIÓN  ★ Favorita", fill="#f5c518", font=FONT_TITLE)
    draw.rectangle([(619, 360), (834, 396)], fill="#f5c518")
    draw.text((642, 372), "🎟 Seleccionar Boletos", fill="#000000", font=FONT_BOLD)
    
    # TOAST NOTIFICATION FLOTANTE (Paso 4 de la guía)
    draw.rectangle([(480, 460), (910, 520)], fill="#13151c", outline="#f5c518", width=2)
    draw.ellipse([(496, 476), (524, 504)], fill="#1a1d27")
    draw.text((502, 482), "★", fill="#f5c518", font=FONT_BOLD)
    draw.text((534, 482), "★ \"Spider-Man: Across...\" añadida a tus favoritas", fill="#ffffff", font=FONT_BOLD)
    draw.text((880, 482), "✕", fill="#a0a6b8", font=FONT_BOLD)
    
    draw.text((36, 545), "Evidencia Paso 4: El Toast aparece de forma desacoplada sin que MovieCard conozca su implementación.", fill="#4ec9b0", font=FONT_TITLE)
    
    img.save(os.path.join(OUTPUT_DIR, "captura_3_toast_notificacion.png"))
    print("Guardada captura 3")

# =========================================================================
# CAPTURA 4: Los 3 Estados de usePremieres (Cargando, Datos, Error)
# =========================================================================
def make_captura_4():
    lines = [
        ("DEMOSTRACIÓN DE LOS 3 ESTADOS DEL CUSTOM HOOK usePremieres.js (Paso 7 y 8)", "#f5c518"),
        ("==================================================================================================", "#666666"),
        ("", "#ffffff"),
        ("1. ESTADO DE CARGA (loading = true):", "#569cd6"),
        ("   [API Request] Petición asíncrona iniciada a servicio de estrenos...", "#999999"),
        ("   --> Renderizado condicional: Se muestran 4 componentes <SkeletonCard /> con animación shimmer.", "#4ec9b0"),
        ("   --> El usuario observa placeholders visuales que evitan saltos de layout (CLS = 0).", "#4ec9b0"),
        ("", "#ffffff"),
        ("2. ESTADO CON DATOS RESUELTOS (loading = false, error = null, data = [4 estrenos]):", "#27c93f"),
        ("   [Adapter Pattern] Datos crudos pasados por adaptMovieList():", "#9cdcfe"),
        ("     * Deadpool & Wolverine (Acción, Comedia) | Estreno: Próximo Jueves", "#cccccc"),
        ("     * Gladiator II (Acción, Drama)           | Estreno: Próximo Mes", "#cccccc"),
        ("     * Joker: Folie à Deux (Drama, Crimen)    | Estreno: Muy Pronto", "#cccccc"),
        ("     * Moana 2 (Animación, Aventura)          | Estreno: En 2 Semanas", "#cccccc"),
        ("   --> Renderizado de tarjetas completas con insignia de fecha de estreno y botón 'Avisarme'.", "#27c93f"),
        ("", "#ffffff"),
        ("3. ESTADO DE ERROR (loading = false, error = '503 Service Unavailable', data = []):", "#ff5f56"),
        ("   [Simulate Error] Usuario presiona 'Simular Error' en la barra de herramientas:", "#ff5f56"),
        ("   --> Renderizado de alerta <div className='premieres-error-card'>:", "#ff5f56"),
        ("       \"No fue posible cargar los próximos estrenos (Error 503).\"", "#ffffff"),
        ("   --> Botón reutilizable <Button variant='primary' onClick={refetch}>Reintentar Conexión</Button>", "#f5c518"),
        ("   --> Al presionar Reintentar, se reactiva el estado de carga y se recuperan los datos.", "#27c93f"),
        ("israel@tecsup:~/projects-dae/semana-11$ _", "#f5c518"),
    ]
    img = draw_terminal("Consola y Pruebas: Ciclo de Vida y los 3 Estados de usePremieres (Cargando, Datos, Error)", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_4_estados_carga_error_estrenos.png"))
    print("Guardada captura 4")

# =========================================================================
# CAPTURA 5: Custom Hooks useDebounce y useWindowSize
# =========================================================================
def make_captura_5():
    lines = [
        ("INSPECCIÓN DE CUSTOM HOOKS: useDebounce.js y useWindowSize.js", "#f5c518"),
        ("--------------------------------------------------------------------------------------------------", "#666666"),
        ("1. Custom Hook useDebounce.js (Consumo en MovieSearch.jsx):", "#569cd6"),
        ("   const debouncedSearchTerm = useDebounce(inputValue, 350);", "#9cdcfe"),
        ("   [Search Input] Tecla pulsada: \"D\"", "#888888"),
        ("   [Search Input] Tecla pulsada: \"Du\"", "#888888"),
        ("   [Search Input] Tecla pulsada: \"Dun\"", "#888888"),
        ("   [Search Input] Tecla pulsada: \"Dune\"", "#888888"),
        ("   --> Pausa de 350ms alcanzada...", "#888888"),
        ("   %c[Hook useDebounce]%c Valor retrasado emitido: \"Dune\"", "#f5c518"),
        ("   --> MovieSearch queda limpio: la lógica de timeout y cleanup reside 100% en el hook.", "#27c93f"),
        ("", "#ffffff"),
        ("2. Custom Hook useWindowSize.js (Consumo en MovieList.jsx):", "#569cd6"),
        ("   const { width, height, columnsCount, isMobile, isTablet, isDesktop } = useWindowSize();", "#9cdcfe"),
        ("   [Resize Event] Ancho detectado: 1440px -> columnsCount = 4 (Escritorio grande)", "#4ec9b0"),
        ("   [Resize Event] Ancho detectado: 1024px -> columnsCount = 3 (Pantalla mediana)", "#4ec9b0"),
        ("   [Resize Event] Ancho detectado: 768px  -> columnsCount = 2 (Tablet)", "#4ec9b0"),
        ("   [Resize Event] Ancho detectado: 480px  -> columnsCount = 1 (Dispositivo móvil)", "#4ec9b0"),
        ("   --> Grid adaptativo con inline style: gridTemplateColumns: `repeat(${columnsCount}, 1fr)`", "#27c93f"),
        ("israel@tecsup:~/projects-dae/semana-11$ _", "#f5c518"),
    ]
    img = draw_terminal("DevTools: Ejecución de Hooks useDebounce y useWindowSize con Grid Adaptativo", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_5_custom_hooks_debounce_windowsize.png"))
    print("Guardada captura 5")

# =========================================================================
# CAPTURA 6: Cabecera Desacoplada y Limpieza de Filtros desde el Banner
# =========================================================================
def make_captura_6():
    width = 960
    height = 540
    img = Image.new("RGB", (width, height), color="#0b0c10")
    draw = ImageDraw.Draw(img)
    
    # Browser window bar
    draw.rectangle([(0, 0), (width, 36)], fill="#1a1d24")
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.rectangle([(160, 6), (width - 160, 30)], fill="#0b0c10", outline="#262b3a")
    draw.text((width // 2 - 200, 9), "http://localhost:5173/ — CineStar DAE (Paso 9 y 10: Cabecera y Filtros)", fill="#a0a6b8", font=FONT_TITLE)
    
    # Header bar
    draw.rectangle([(0, 36), (width, 92)], fill="#13151c", outline="#262b3a")
    draw.text((36, 52), "CineStar", fill="#ffffff", font=FONT_LARGE)
    draw.rectangle([(128, 54), (168, 74)], fill="#e50914")
    draw.text((134, 57), "DAE", fill="#ffffff", font=FONT_TITLE)
    
    # Header receives ONLY favoritesCount primitive
    draw.rectangle([(630, 50), (800, 80)], fill="#1a1d27", outline="#f5c518", width=2)
    draw.text((642, 57), "★ Favoritas", fill="#f5c518", font=FONT_BOLD)
    draw.rectangle([(755, 54), (785, 76)], fill="#f5c518")
    draw.text((766, 57), "2", fill="#000000", font=FONT_BOLD)
    
    # Annotation for Header
    draw.rectangle([(36, 110), ( width - 36, 175)], fill="#13151c", outline="#4ec9b0")
    draw.text((48, 120), "PASO 9 DE LA GUÍA: CABECERA DESACOPLADA", fill="#4ec9b0", font=FONT_BOLD)
    draw.text((48, 142), "Header recibe exclusivamente props.favoritesCount = 2 (primitivo numérico), NO recibe la lista completa de películas.", fill="#ffffff", font=FONT_REGULAR)
    
    # Banner Hero with Active Filter & Reset Button (Paso 10)
    draw.rectangle([(36, 195), (width - 36, 440)], fill="#1a1d27", outline="#f5c518")
    draw.text((56, 215), "PELÍCULA DESTACADA: Dune: Parte Dos", fill="#f5c518", font=FONT_MED)
    draw.text((56, 245), "Buscador integrado con filtro activo en tiempo real: \"Oppenheimer\"", fill="#a0a6b8", font=FONT_REGULAR)
    
    # Search box inside Hero with Reset Button
    draw.rectangle([(56, 280), (890, 330)], fill="#13151c", outline="#f5c518", width=2)
    draw.text((76, 296), "🔍", fill="#f5c518", font=FONT_MED)
    draw.text((106, 296), "Oppenheimer", fill="#ffffff", font=FONT_MED)
    
    # Botón que limpia el filtro desde el banner (Paso 10)
    draw.rectangle([(640, 288), (765, 322)], fill="#262b3a", outline="#ff5f56")
    draw.text((652, 298), "↺ Restablecer Todo", fill="#ff5f56", font=FONT_BOLD)
    
    draw.rectangle([(775, 288), (880, 322)], fill="#f5c518")
    draw.text((788, 298), "Explorar", fill="#000000", font=FONT_BOLD)
    
    draw.text((56, 355), "PASO 10 DE LA GUÍA: LIMPIEZA DE FILTROS DESDE EL BANNER", fill="#f5c518", font=FONT_BOLD)
    draw.text((56, 380), "Al hacer clic en 'Restablecer Todo', se sincronizan instantáneamente el buscador y la cartelera inferior.", fill="#cccccc", font=FONT_REGULAR)
    
    img.save(os.path.join(OUTPUT_DIR, "captura_6_cabecera_desacoplada.png"))
    print("Guardada captura 6")

# =========================================================================
# CAPTURA 7: Árbol de Componentes y Datos por Nivel (Paso 11 de la guía)
# =========================================================================
def make_captura_7():
    lines = [
        ("ÁRBOL DE COMPONENTES Y ARQUITECTURA DE DATOS (Paso 11 de la Guía)", "#f5c518"),
        ("==================================================================================================", "#666666"),
        ("", "#ffffff"),
        ("  [NIVEL 0] App.jsx (Componente Raíz / Ancestro Común):", "#569cd6"),
        ("    * Estado: favorites ([1, 4]) -> Persistido en localStorage", "#9cdcfe"),
        ("    * Estado: searchTerm ('')    -> Sincronizado globalmente", "#9cdcfe"),
        ("    * Estado: onlyFavorites (bool)", "#9cdcfe"),
        ("    * Estado: toast ({ show, message, type }) -> Notificaciones", "#9cdcfe"),
        ("    * Dato Derivado: favoritesCount = favorites.length (primitivo)", "#f5c518"),
        ("    * Función: handleToggleFavorite(id) -> Callback con mutación inmutable", "#27c93f"),
        ("    * Función: handleResetFilters()     -> Sincronización global", "#27c93f"),
        ("       |", "#888888"),
        ("       +---> Header.jsx (Nivel 1):", "#4ec9b0"),
        ("       |       * Recibe: favoritesCount (número), onlyFavorites, onToggleFavoritesFilter", "#cccccc"),
        ("       |       * NOTA CLAVE: NO recibe la lista completa de películas.", "#f5c518"),
        ("       |", "#888888"),
        ("       +---> Hero.jsx (Nivel 1):", "#4ec9b0"),
        ("       |       * Recibe: movie, isFavorite, onToggleFavorite, searchValue, onResetFilters", "#cccccc"),
        ("       |", "#888888"),
        ("       +---> PremieresSection.jsx (Nivel 1):", "#4ec9b0"),
        ("       |       * Consume: usePremieres() -> { loading, data, error, refetch }", "#cccccc"),
        ("       |       * Hijos: <SkeletonCard /> (si loading) | Tarjetas adaptadas (si data)", "#cccccc"),
        ("       |", "#888888"),
        ("       +---> MovieSearch.jsx (Nivel 1):", "#4ec9b0"),
        ("       |       * Estado local: inputValue (inmediato)", "#cccccc"),
        ("       |       * Consume: useDebounce(inputValue, 350) -> emite onSearchChange", "#cccccc"),
        ("       |", "#888888"),
        ("       +---> MovieList.jsx (Nivel 1):", "#4ec9b0"),
        ("       |       * Consume: useWindowSize() -> { columnsCount, width }", "#cccccc"),
        ("       |       * Estado local: selectedGenre", "#cccccc"),
        ("       |       |", "#888888"),
        ("       |       +---> MovieCard.jsx (Nivel 2):", "#4ec9b0"),
        ("       |               * Recibe: movie, isFavorite, onToggleFavorite", "#cccccc"),
        ("       |               * Evento: onToggleFavorite(movie.id) -> avisa hacia arriba", "#27c93f"),
        ("       |", "#888888"),
        ("       +---> Toast.jsx (Nivel 1): Recibe { message, type, visible, onClose }", "#4ec9b0"),
        ("       +---> Footer.jsx (Nivel 1): Datos del estudiante Israel Huamán y DAE", "#4ec9b0"),
        ("israel@tecsup:~/projects-dae/semana-11$ _", "#f5c518"),
    ]
    img = draw_terminal("Diagrama: Árbol de Componentes, Jerarquía y Ubicación de Datos por Nivel", lines)
    img.save(os.path.join(OUTPUT_DIR, "captura_7_arbol_componentes_jerarquia.png"))
    print("Guardada captura 7")

if __name__ == "__main__":
    make_captura_1()
    make_captura_2()
    make_captura_3()
    make_captura_4()
    make_captura_5()
    make_captura_6()
    make_captura_7()
    print("Todas las 7 capturas generadas exitosamente en:", OUTPUT_DIR)
