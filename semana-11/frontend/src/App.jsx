import React, { useState, useEffect, useMemo } from 'react';
import Header from './components/Header/Header';
import Hero from './components/Hero/Hero';
import MovieSearch from './components/MovieSearch/MovieSearch';
import MovieList from './components/MovieList/MovieList';
import PremieresSection from './components/PremieresSection/PremieresSection';
import Toast from './components/Toast/Toast';
import Footer from './components/Footer/Footer';
import { movies as rawMovies } from './data/movies';
import { adaptMovieList } from './utils/movieAdapter';
import './styles/global.css';

const FAVORITES_STORAGE_KEY = 'cinestar_dae_favorites_s11';

export function App() {
  // =========================================================================
  // PASO 3: Patrón Adaptador
  // Pasar los datos de la cartelera por la utilidad adaptMovieList
  // =========================================================================
  const adaptedMovies = useMemo(() => adaptMovieList(rawMovies), []);

  // Película destacada para el banner Hero
  const featuredMovie = adaptedMovies.find(m => m.featured) || adaptedMovies[0];

  // =========================================================================
  // PASO 9: Estado de favoritas elevado a la raíz (App.jsx)
  // =========================================================================
  const [favorites, setFavorites] = useState(() => {
    try {
      const stored = localStorage.getItem(FAVORITES_STORAGE_KEY);
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (err) {
      console.error('[Storage Error] Fallo al leer localStorage:', err);
    }
    return [1, 4]; // Favoritas iniciales por defecto (Dune 2 e Interstellar)
  });

  useEffect(() => {
    try {
      localStorage.setItem(FAVORITES_STORAGE_KEY, JSON.stringify(favorites));
    } catch (err) {
      console.error('[Storage Error] Fallo al escribir en localStorage:', err);
    }
  }, [favorites]);

  // Paso 9 de la guía: El contador es un valor primitivo derivado que se envía a la cabecera
  // sin que la cabecera reciba la lista completa de películas ni de IDs
  const favoritesCount = favorites.length;

  // =========================================================================
  // ESTADO 2: Término de búsqueda global debounced
  // =========================================================================
  const [searchTerm, setSearchTerm] = useState('');

  // =========================================================================
  // ESTADO 3: Vista de solo favoritas
  // =========================================================================
  const [onlyFavorites, setOnlyFavorites] = useState(false);

  // =========================================================================
  // PASO 4: Aviso emergente (Toast) desacoplado
  // =========================================================================
  const [toast, setToast] = useState({
    visible: false,
    message: '',
    type: 'success'
  });

  const showToast = (message, type = 'success') => {
    setToast({
      visible: true,
      message,
      type
    });
  };

  const handleCloseToast = () => {
    setToast(prev => ({ ...prev, visible: false }));
  };

  // =========================================================================
  // FUNCIÓN: toggleFavorite (Comunicación Hijo -> Padre)
  // Paso 4: Agrega o quita favorita y dispara el Toast sin que MovieCard
  // sepa cómo se implementa o renderiza el aviso emergente.
  // =========================================================================
  const handleToggleFavorite = (movieId) => {
    const movie = adaptedMovies.find(m => m.id === movieId);
    const movieTitle = movie ? movie.title : `Película #${movieId}`;

    setFavorites(prevFavorites => {
      const exists = prevFavorites.includes(movieId);
      let updated;
      if (exists) {
        updated = prevFavorites.filter(id => id !== movieId);
        showToast(`"${movieTitle}" quitada de tus favoritas`, 'danger');
        console.log(`%c[Toast Event]%c Desmarcada: "${movieTitle}"`, 'background: #ef4444; color: #fff;', '');
      } else {
        updated = [...prevFavorites, movieId];
        showToast(`★ "${movieTitle}" añadida a tus favoritas`, 'success');
        console.log(`%c[Toast Event]%c Marcada: "${movieTitle}"`, 'background: #10b981; color: #fff;', '');
      }
      return updated;
    });
  };

  // Paso 10: Función que limpia filtros y sincroniza el banner con el listado
  const handleResetFilters = () => {
    setSearchTerm('');
    setOnlyFavorites(false);
    showToast('Filtros de búsqueda y categorías restablecidos', 'info');
  };

  const hasActiveFilters = Boolean(searchTerm || onlyFavorites);

  return (
    <div className="app-layout">
      {/* 1. Header: Recibe ÚNICAMENTE el contador primitivo favoritesCount (Paso 9) */}
      <Header
        favoritesCount={favoritesCount}
        onlyFavorites={onlyFavorites}
        onToggleFavoritesFilter={() => setOnlyFavorites(prev => !prev)}
      />

      <main>
        {/* 2. Hero banner: recibe película adaptada, buscador integrado y botón de limpieza (Paso 10) */}
        <Hero
          movie={featuredMovie}
          isFavorite={favorites.includes(featuredMovie.id)}
          onToggleFavorite={handleToggleFavorite}
          searchValue={searchTerm}
          onSearchChange={setSearchTerm}
          onResetFilters={handleResetFilters}
          hasActiveFilters={hasActiveFilters}
        />

        {/* 3. Próximos Estrenos: Paso 8 (Skeletons con shimmer, datos y error con usePremieres) */}
        <PremieresSection />

        {/* 4. Buscador Controlado con Hook useDebounce (Paso 5) */}
        <section className="container">
          <MovieSearch
            value={searchTerm}
            onSearchChange={setSearchTerm}
            delay={350}
          />
        </section>

        {/* 5. MovieList: filtrado reactivo, uso de useWindowSize y comunicación hacia arriba */}
        <MovieList
          movies={adaptedMovies}
          favorites={favorites}
          onToggleFavorite={handleToggleFavorite}
          searchTerm={searchTerm}
          onResetFilters={handleResetFilters}
          onlyFavorites={onlyFavorites}
          onToggleOnlyFavorites={() => setOnlyFavorites(prev => !prev)}
        />
      </main>

      {/* 6. Toast emergente desacoplado (Paso 4) */}
      <Toast
        message={toast.message}
        type={toast.type}
        visible={toast.visible}
        onClose={handleCloseToast}
      />

      {/* 7. Footer con datos institucionales y enlace a semana-11 */}
      <Footer />
    </div>
  );
}

export default App;
