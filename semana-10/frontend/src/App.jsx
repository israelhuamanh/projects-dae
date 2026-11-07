import React, { useState, useEffect } from 'react';
import Header from './components/Header/Header';
import Hero from './components/Hero/Hero';
import MovieSearch from './components/MovieSearch/MovieSearch';
import MovieList from './components/MovieList/MovieList';
import Footer from './components/Footer/Footer';
import { movies } from './data/movies';
import './styles/global.css';

const FAVORITES_STORAGE_KEY = 'cinestar_dae_favorites';

export function App() {
  // Película seleccionada para el banner destacado (Hero)
  const featuredMovie = movies.find(m => m.featured) || movies[0];

  // =========================================================================
  // ESTADO 1: Películas favoritas con inicialización perezosa (lazy init)
  // Paso 4 y 10: Recupera las favoritas de localStorage para que sobrevivan recargas.
  // =========================================================================
  const [favorites, setFavorites] = useState(() => {
    try {
      const stored = localStorage.getItem(FAVORITES_STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        console.log(`[Storage] ${parsed.length} favoritas recuperadas de localStorage:`, parsed);
        return parsed;
      }
    } catch (err) {
      console.error('[Storage Error] Fallo al leer localStorage:', err);
    }
    // Estado inicial por defecto (Dune 2 e Interstellar como favoritas iniciales de ejemplo)
    return [1, 4];
  });

  // Paso 10: Efecto de persistencia automática en localStorage
  useEffect(() => {
    try {
      localStorage.setItem(FAVORITES_STORAGE_KEY, JSON.stringify(favorites));
      console.log(`[Storage] Guardadas ${favorites.length} favoritas en localStorage:`, favorites);
    } catch (err) {
      console.error('[Storage Error] Fallo al escribir en localStorage:', err);
    }
  }, [favorites]);

  // =========================================================================
  // ESTADO 2: Término de búsqueda global (debounced)
  // =========================================================================
  const [searchTerm, setSearchTerm] = useState('');

  // =========================================================================
  // ESTADO 3: Vista de solo favoritas
  // =========================================================================
  const [onlyFavorites, setOnlyFavorites] = useState(false);

  // =========================================================================
  // FUNCIÓN: toggleFavorite (Comunicación Hijo -> Padre)
  // Paso 4 y 5: Agrega o quita una película de la lista de favoritas.
  // =========================================================================
  const handleToggleFavorite = (movieId) => {
    setFavorites(prevFavorites => {
      const exists = prevFavorites.includes(movieId);
      let updated;
      if (exists) {
        updated = prevFavorites.filter(id => id !== movieId);
        console.log(`%c[Favorite Removed]%c Película ID ${movieId} quitada de favoritas`, 'background: #ef4444; color: #fff; padding: 2px 6px;', '');
      } else {
        updated = [...prevFavorites, movieId];
        console.log(`%c[Favorite Added]%c Película ID ${movieId} agregada a favoritas`, 'background: #10b981; color: #fff; padding: 2px 6px;', '');
      }
      return updated;
    });
  };

  const handleResetFilters = () => {
    setSearchTerm('');
    setOnlyFavorites(false);
  };

  return (
    <div className="app-layout">
      {/* 1. Header con logo, navegación, botón reutilizable y contador dinámico de favoritas */}
      <Header
        favoritesCount={favorites.length}
        onlyFavorites={onlyFavorites}
        onToggleFavoritesFilter={() => setOnlyFavorites(prev => !prev)}
      />

      <main>
        {/* 2. Hero banner: recibe película destacada, estado de favorita y buscador integrado (Paso 9) */}
        <Hero
          movie={featuredMovie}
          isFavorite={favorites.includes(featuredMovie.id)}
          onToggleFavorite={handleToggleFavorite}
          searchValue={searchTerm}
          onSearchChange={setSearchTerm}
        />

        {/* 3. Buscador Controlado con Retardo (Debounce de 350ms) (Pasos 6 y 7) */}
        <section className="container">
          <MovieSearch
            value={searchTerm}
            onSearchChange={setSearchTerm}
            delay={350}
          />
        </section>

        {/* 4. MovieList: filtrado reactivo, comunicación hijo->padre y Estado Vacío (Pasos 5 y 8) */}
        <MovieList
          movies={movies}
          favorites={favorites}
          onToggleFavorite={handleToggleFavorite}
          searchTerm={searchTerm}
          onResetFilters={handleResetFilters}
          onlyFavorites={onlyFavorites}
          onToggleOnlyFavorites={() => setOnlyFavorites(prev => !prev)}
        />
      </main>

      {/* 5. Footer con datos del estudiante Israel Huamán y enlace a semana-10 */}
      <Footer />
    </div>
  );
}

export default App;
