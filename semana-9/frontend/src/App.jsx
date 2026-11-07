import React from 'react';
import { Header } from './components/Header/Header';
import { Hero } from './components/Hero/Hero';
import { MovieList } from './components/MovieList/MovieList';
import { Footer } from './components/Footer/Footer';
import { movies } from './data/movies';
import './styles/global.css';

export function App() {
  // Película seleccionada para el banner destacado (Hero)
  const featuredMovie = movies.find(m => m.featured) || movies[0];

  return (
    <div className="app-layout">
      {/* 1. Header con logo y navegación */}
      <Header />

      <main>
        {/* 2. Hero banner: recibe la película destacada por props */}
        <Hero movie={featuredMovie} />

        {/* 3. MovieList: recibe el listado completo de películas por props y las mapea con clave única */}
        <MovieList movies={movies} />
      </main>

      {/* 4. Footer con información de contacto y metadatos del estudiante */}
      <Footer />
    </div>
  );
}

export default App;
