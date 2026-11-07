import React, { useState } from 'react';
import { MovieCard } from '../MovieCard/MovieCard';
import { Film, Filter, Search, RotateCcw, Heart, LayoutGrid } from 'lucide-react';
import useWindowSize from '../../hooks/useWindowSize';
import Button from '../Button/Button';
import './MovieList.css';

/**
 * Componente MovieList.
 * Utiliza el custom hook propio useWindowSize (Paso 6 de la guía)
 * para calcular dinámicamente cuántas tarjetas se muestran por fila de acuerdo a la ventana.
 * 
 * @param {Object} props
 * @param {Array} props.movies - Catálogo completo de películas adaptadas.
 * @param {Array} [props.favorites=[]] - Lista de IDs de películas favoritas.
 * @param {Function} [props.onToggleFavorite] - Callback para alternar favoritas hacia el padre.
 * @param {string} [props.searchTerm=''] - Término de búsqueda debounced.
 * @param {Function} [props.onResetFilters] - Función para reiniciar filtros.
 * @param {boolean} [props.onlyFavorites=false] - Indica si se filtran solo favoritas.
 * @param {Function} [props.onToggleOnlyFavorites] - Alterna la vista de favoritas.
 */
export const MovieList = ({
  movies,
  favorites = [],
  onToggleFavorite,
  searchTerm = '',
  onResetFilters,
  onlyFavorites = false,
  onToggleOnlyFavorites
}) => {
  // Estado local para la categoría de género seleccionada
  const [selectedGenre, setSelectedGenre] = useState('Todos');

  // Paso 6 de la guía: uso del custom hook useWindowSize para el grid adaptativo
  const { width, columnsCount, isMobile } = useWindowSize();

  const genres = ['Todos', 'Ciencia Ficción', 'Acción', 'Drama', 'Animación'];

  // Lógica de filtrado combinada
  const filteredMovies = movies.filter(movie => {
    if (onlyFavorites && !favorites.includes(movie.id)) {
      return false;
    }

    const matchesGenre = selectedGenre === 'Todos' || 
      movie.genre.toLowerCase().includes(selectedGenre.toLowerCase());
    if (!matchesGenre) return false;

    if (searchTerm && searchTerm.trim() !== '') {
      const term = searchTerm.toLowerCase().trim();
      const matchesTitle = movie.title.toLowerCase().includes(term);
      const matchesOriginal = movie.originalTitle ? movie.originalTitle.toLowerCase().includes(term) : false;
      const matchesSynopsis = movie.synopsis ? movie.synopsis.toLowerCase().includes(term) : false;
      return matchesTitle || matchesOriginal || matchesSynopsis;
    }

    return true;
  });

  const handleReset = () => {
    setSelectedGenre('Todos');
    if (onResetFilters) {
      onResetFilters();
    }
  };

  return (
    <section id="cartelera" className="movie-list-section container">
      <div className="list-header">
        <div>
          <h2 className="section-title">
            {onlyFavorites ? 'Tus Películas Favoritas' : 'En Cartelera'}
          </h2>
          <p className="list-subtitle">
            {onlyFavorites
              ? `Tienes ${favorites.length} ${favorites.length === 1 ? 'película seleccionada' : 'películas seleccionadas'} en tu lista personal.`
              : 'Explora los títulos disponibles hoy en nuestras salas IMAX, 3D y 2D.'}
          </p>
        </div>

        {/* Grupo de filtros con botones reutilizables */}
        <div className="filter-controls">
          {/* Indicador de layout adaptativo provisto por el hook useWindowSize */}
          <div className="window-size-badge" title={`Ancho de pantalla: ${width}px`}>
            <LayoutGrid size={14} />
            <span>{columnsCount} {columnsCount === 1 ? 'columna' : 'columnas'}</span>
          </div>

          {/* Botón toggle de Favoritas */}
          <Button
            variant={onlyFavorites ? 'favorite' : 'secondary'}
            size="sm"
            active={onlyFavorites}
            onClick={onToggleOnlyFavorites}
            className="filter-fav-btn"
            title="Alternar filtro de películas favoritas"
          >
            <Heart
              size={15}
              fill={favorites.length > 0 ? '#f5c518' : 'none'}
              color={favorites.length > 0 ? '#f5c518' : 'currentColor'}
            />
            <span>Solo Favoritas ({favorites.length})</span>
          </Button>

          {/* Filtros por género con Button reutilizable */}
          <div className="filter-group">
            <Filter size={16} className="filter-icon" />
            <div className="filter-pills">
              {genres.map(genre => (
                <Button
                  key={genre}
                  variant={selectedGenre === genre ? 'primary' : 'secondary'}
                  size="sm"
                  active={selectedGenre === genre}
                  onClick={() => setSelectedGenre(genre)}
                  className="filter-pill-btn"
                >
                  {genre}
                </Button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Indicador de resultados activos cuando hay filtros */}
      {(searchTerm || selectedGenre !== 'Todos' || onlyFavorites) && (
        <div className="active-filters-bar">
          <div className="active-filters-info">
            <span>Resultados encontrados: <strong>{filteredMovies.length}</strong></span>
            {searchTerm && <span className="filter-chip">Búsqueda: "{searchTerm}"</span>}
            {selectedGenre !== 'Todos' && <span className="filter-chip">Género: {selectedGenre}</span>}
            {onlyFavorites && <span className="filter-chip">★ Solo Favoritas</span>}
          </div>
          <Button
            variant="ghost"
            size="sm"
            onClick={handleReset}
            className="btn-reset-filters"
          >
            <RotateCcw size={14} />
            <span>Limpiar filtros</span>
          </Button>
        </div>
      )}

      {/* Renderizado condicional: Grid adaptativo o Estado Vacío */}
      {filteredMovies.length === 0 ? (
        <div className="empty-state animate-fade-in">
          <div className="empty-state__icon-wrapper">
            {onlyFavorites ? (
              <Heart size={48} className="empty-state__icon empty-state__icon--heart" />
            ) : (
              <Search size={48} className="empty-state__icon" />
            )}
          </div>
          <h3 className="empty-state__title">No se encontraron películas</h3>
          <p className="empty-state__description">
            {onlyFavorites
              ? 'Aún no has agregado películas a tu lista de favoritas. Haz clic en el ícono de corazón o estrella en cualquier película de la cartelera.'
              : searchTerm
                ? `No encontramos títulos que coincidan con "${searchTerm}" ${selectedGenre !== 'Todos' ? `en la categoría ${selectedGenre}` : ''}.`
                : `No hay funciones disponibles en la categoría "${selectedGenre}".`}
          </p>
          <div className="empty-state__actions">
            <Button
              variant="primary"
              size="md"
              onClick={handleReset}
            >
              <RotateCcw size={16} />
              <span>Restablecer Búsqueda y Filtros</span>
            </Button>
          </div>
        </div>
      ) : (
        <div
          className="movies-grid"
          style={{ gridTemplateColumns: `repeat(${columnsCount}, minmax(0, 1fr))` }}
        >
          {filteredMovies.map(movie => (
            <MovieCard
              key={movie.id}
              movie={movie}
              isFavorite={favorites.includes(movie.id)}
              onToggleFavorite={onToggleFavorite}
            />
          ))}
        </div>
      )}
    </section>
  );
};

export default MovieList;
