import React, { useState } from 'react';
import { MovieCard } from '../MovieCard/MovieCard';
import { Film, Filter } from 'lucide-react';
import './MovieList.css';

export const MovieList = ({ movies }) => {
  const [selectedGenre, setSelectedGenre] = useState('Todos');

  const genres = ['Todos', 'Ciencia Ficción', 'Acción', 'Drama', 'Animación'];

  const filteredMovies = selectedGenre === 'Todos'
    ? movies
    : movies.filter(movie => movie.genre.toLowerCase().includes(selectedGenre.toLowerCase()));

  return (
    <section id="cartelera" className="movie-list-section container">
      <div className="list-header">
        <div>
          <h2 className="section-title">En Cartelera</h2>
          <p className="list-subtitle">Explora los títulos disponibles hoy en nuestras salas IMAX y 3D.</p>
        </div>

        <div className="filter-group">
          <Filter size={16} className="filter-icon" />
          <div className="filter-pills">
            {genres.map(genre => (
              <button
                key={genre}
                className={`filter-pill ${selectedGenre === genre ? 'active' : ''}`}
                onClick={() => setSelectedGenre(genre)}
              >
                {genre}
              </button>
            ))}
          </div>
        </div>
      </div>

      {filteredMovies.length === 0 ? (
        <div className="empty-state">
          <Film size={40} />
          <p>No se encontraron películas en esta categoría.</p>
        </div>
      ) : (
        <div className="movies-grid">
          {filteredMovies.map(movie => (
            /* Punto 9 de la guía: recorre con map y asigna la prop key única */
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      )}
    </section>
  );
};
