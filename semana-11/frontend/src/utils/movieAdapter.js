/**
 * Patrón Adaptador para normalización de datos de películas.
 * Transforma estructuras heterogéneas (APIs externas, snake_case, campos en español u opcionales)
 * al modelo interno estandarizado que consume la aplicación CineStar DAE.
 */

/**
 * Adapta un único registro de película al modelo interno.
 * @param {Object} raw - Datos crudos de la película.
 * @returns {Object} Película con formato estandarizado.
 */
export function adaptMovie(raw) {
  if (!raw || typeof raw !== 'object') {
    return null;
  }

  // Normalización del ID
  const id = raw.id ?? raw.movie_id ?? raw.codigo ?? Number(raw.pk) ?? 0;

  // Normalización de títulos
  const title = raw.title ?? raw.nombre ?? raw.titulo ?? 'Título no disponible';
  const originalTitle = raw.originalTitle ?? raw.original_title ?? raw.titulo_original ?? title;

  // Normalización de género
  let genre = raw.genre ?? raw.genero ?? raw.categoria ?? 'General';
  if (Array.isArray(genre)) {
    genre = genre.map(g => (typeof g === 'object' ? g.name : g)).join(', ');
  }

  // Normalización de duración
  let duration = raw.duration ?? raw.duracion ?? '';
  if (!duration && (raw.runtime || raw.runtime_minutes)) {
    duration = `${raw.runtime || raw.runtime_minutes} min`;
  } else if (!duration) {
    duration = '120 min';
  }

  // Normalización de calificación (número flotante a 1 decimal)
  let rating = raw.rating ?? raw.vote_average ?? raw.calificacion ?? 8.0;
  rating = Number(Number(rating).toFixed(1));

  // Normalización de clasificación por edad
  const classification = raw.classification ?? raw.clasificacion ?? raw.censura ?? '+14';

  // Normalización de sinopsis
  const synopsis = raw.synopsis ?? raw.overview ?? raw.sinopsis ?? raw.descripcion ?? 'Sinopsis no disponible en este momento.';

  // Normalización de imágenes (poster y backdrop)
  const poster = raw.poster ?? raw.poster_path ?? raw.imagen_poster ?? 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800';
  const backdrop = raw.backdrop ?? raw.backdrop_path ?? raw.imagen_fondo ?? poster;

  // Normalización de horarios
  let schedules = raw.schedules ?? raw.horarios ?? raw.funciones ?? ['15:00', '18:30', '21:00'];
  if (!Array.isArray(schedules)) {
    schedules = [schedules];
  }

  // Bandera destacada y fecha de estreno
  const featured = Boolean(raw.featured ?? raw.destacada ?? false);
  const premiereDate = raw.premiereDate ?? raw.release_date ?? raw.fecha_estreno ?? null;

  return {
    id,
    title,
    originalTitle,
    genre,
    duration,
    rating,
    classification,
    synopsis,
    poster,
    backdrop,
    schedules,
    featured,
    premiereDate
  };
}

/**
 * Adapta una colección completa de películas.
 * @param {Array} rawList - Lista cruda de películas.
 * @returns {Array} Lista de películas adaptadas.
 */
export function adaptMovieList(rawList) {
  if (!Array.isArray(rawList)) {
    return [];
  }
  return rawList.map(adaptMovie).filter(Boolean);
}

export default {
  adaptMovie,
  adaptMovieList
};
